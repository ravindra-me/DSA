#!/usr/bin/env bash
# Merges a validated staging lesson into the branch and pushes it.
#
# Usage: publish.sh <staging-dir>
#
# Each attempt starts from the latest remote branch tip, re-applies the lesson
# (apply is idempotent and re-checks for duplicates), commits only if there is
# a change, and pushes. A push rejected because the branch moved is retried
# from the new tip, so concurrent edits (e.g. you updating progress.json) are
# never overwritten. This script never executes generated code.
set -euo pipefail

# Everything lives in main() so bash parses the whole script before running it:
# `git reset --hard` below may rewrite this very file on disk.
main() {
  staging="${1:?usage: publish.sh <staging-dir>}"
  branch="${GITHUB_REF_NAME:?GITHUB_REF_NAME must be set}"
  agent="$(dirname "$0")/agent.py"
  result_file="$(mktemp)"
  python_bin="$(command -v python || command -v python3)"
  max_attempts=3

  git config user.name "github-actions[bot]"
  git config user.email "41898732+github-actions[bot]@users.noreply.github.com"

  read_result() {
    "$python_bin" -c 'import json,sys; print(json.load(open(sys.argv[1]))[sys.argv[2]])' "$result_file" "$1"
  }

  for attempt in $(seq 1 "$max_attempts"); do
    echo "::group::Publish attempt ${attempt}/${max_attempts}"
    git fetch --no-tags --depth=1 origin "$branch"
    git reset --hard "origin/${branch}"

    "$python_bin" "$agent" apply --staging "$staging" --result-file "$result_file"
    if [[ "$(read_result applied)" != "True" ]]; then
      echo "Nothing to publish: $(read_result message)"
      echo "::endgroup::"
      exit 0
    fi

    lessons_dir="$(read_result lessonsDir)"
    git add --all -- "$lessons_dir"
    # Defence in depth: the agent must only ever change the lessons directory.
    if [[ -n "$(git status --porcelain -- . ":(exclude)${lessons_dir}")" ]]; then
      echo "::error::Unexpected changes outside ${lessons_dir}/:"
      git status --porcelain -- . ":(exclude)${lessons_dir}"
      exit 1
    fi
    if git diff --cached --quiet; then
      echo "No changes to commit."
      echo "::endgroup::"
      exit 0
    fi

    git commit --quiet -m "$(read_result commitMessage)"
    if git push origin "HEAD:${branch}"; then
      echo "::notice::Published: $(read_result commitMessage)"
      echo "### Published"$'\n\n'"$(read_result commitMessage)" >> "${GITHUB_STEP_SUMMARY:-/dev/null}"
      echo "::endgroup::"
      exit 0
    fi
    echo "::warning::Push rejected (branch moved?); retrying from the new tip"
    echo "::endgroup::"
    sleep $((attempt * 5))
  done

  echo "::error::Could not push after ${max_attempts} attempts"
  exit 1
}

main "$@"
