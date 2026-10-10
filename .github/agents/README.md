# DSA Learning Agent

An autonomous agent that writes one Data Structures & Algorithms lesson per day into this repository. It runs entirely on **GitHub Actions**: once it is set up, your own computer can stay switched off.

Each lesson contains a concept explanation, progressively harder exercises, reference solutions with walkthroughs, starter files for your own attempts, and automated tests. The tests must pass in an isolated sandbox before anything is committed.

---

## Contents

1. [Quick start](#1-quick-start)
2. [Architecture](#2-architecture)
3. [How a daily run works](#3-how-a-daily-run-works)
4. [Security model](#4-security-model)
5. [Configuration](#5-configuration)
6. [Changing the schedule](#6-changing-the-schedule)
7. [Manually triggering a lesson](#7-manually-triggering-a-lesson)
8. [Progress tracking](#8-progress-tracking)
9. [Spaced revision](#9-spaced-revision)
10. [Practising](#10-practising)
11. [Troubleshooting](#11-troubleshooting)
12. [Local development (optional)](#12-local-development-optional)
13. [Extending the agent](#13-extending-the-agent)

---

## 1. Quick start

You only need a GitHub repository and an AI API key.

1. **Push this repository to GitHub** (public or private).
2. **Add an API key as a secret**: *Settings → Secrets and variables → Actions → New repository secret*.
   - `GEMINI_API_KEY` for Google Gemini. **The free tier works.** Create a key at [Google AI Studio](https://aistudio.google.com/apikey). **Or**
   - `OPENAI_API_KEY` for OpenAI (or any OpenAI-compatible endpoint, see [§5](#5-configuration)), **or**
   - `ANTHROPIC_API_KEY` for Anthropic Claude (billed to your Anthropic API account, separate from a Claude.ai subscription).
3. **Allow the workflow to push**: *Settings → Actions → General → Workflow permissions* → select **Read and write permissions**. (The workflow still asks for write access only in the single job that needs it.)
4. **Enable Actions** if prompted on the *Actions* tab.
5. Optional: run it now via *Actions → DSA Daily Lesson → Run workflow*. Otherwise the first lesson arrives at the next scheduled time (06:00 UTC by default).

The default branch must allow pushes from `github-actions[bot]`. If you protect it with required reviews, see [§11](#11-troubleshooting).

---

## 2. Architecture

```
.github/
├── workflows/
│   ├── dsa-daily.yml          # scheduled + manual lesson pipeline (generate → validate → publish)
│   └── dsa-validation.yml     # CI: lint workflows, agent self-tests, re-validate every lesson
└── agents/
    ├── README.md              # this file
    ├── config/agent.json      # all tunables (language, problem count, revision, AI, sandbox)
    ├── roadmap/roadmap.json   # ordered curriculum: phases → topics (59 topics)
    ├── prompts/               # Markdown prompt templates ({{placeholders}})
    │   ├── system.md          #   role + strict JSON output rules
    │   ├── lesson.md          #   lesson outline + problem statements
    │   ├── problem.md         #   solution + starter + tests for one problem
    │   └── repair.md          #   fix code that failed validation
    ├── scripts/
    │   ├── agent.py           # CLI entry point (workflows call only this + publish.sh)
    │   ├── publish.sh         # apply → commit → push, with retry on a moved branch
    │   └── dsa_agent/         # stdlib-only Python package
    │       ├── cli.py               commands: check, plan, generate, validate, apply, run, practice, ...
    │       ├── config.py            loads agent.json + environment overrides
    │       ├── roadmap.py           curriculum model
    │       ├── select_topic.py      what to teach today (idempotency, roadmap, revisions)
    │       ├── revision.py          spaced-repetition schedule derived from history
    │       ├── generate_lesson.py   AI calls → validation → repair loop → staging folder
    │       ├── validate_solution.py static checks + sandboxed tests + vacuous-test detection
    │       ├── sandbox.py           Docker sandbox (CI) / process sandbox (local dev)
    │       ├── update_progress.py   merges a staged lesson into dsa/ (idempotent)
    │       ├── progress.py          dsa/progress.json schema + derived summary
    │       ├── ai.py                provider abstraction (Gemini, OpenAI-compatible, Anthropic), retries
    │       ├── schema.py            validates AI JSON responses
    │       ├── languages.py         per-language layout, test runner, safety rules
    │       ├── render.py            deterministic Markdown templates
    │       ├── prompts.py           template rendering
    │       ├── fsutil.py            atomic file writes / directory swaps
    │       └── log.py               GitHub Actions annotations, groups, outputs, summaries
    └── tests/                 # agent self-tests (fake AI provider, real sandboxed runs)

dsa/
├── README.md                  # auto-generated index of all lessons
├── progress.json              # learning history (source of truth)
└── day-001/                   # one folder per lesson (see below)
```

Each lesson folder looks like this (Python shown; JavaScript uses `problem-01.js` / `problem-01.test.js`):

```
dsa/day-001/
├── README.md                 # topic, objectives, concept explanation, example, ASCII visual,
│                             # complexity, interview questions, exercise table, how to practise
├── lesson.json               # machine-readable metadata (used for re-validation)
├── exercises/problem-01.md   # statement, I/O, constraints, examples, signature, hidden hint (no solution)
├── practice/problem_01.py    # starter stub: write YOUR solution here
├── solutions/problem-01.md   # approach, thought process, algorithm, complexity, edge cases, code
├── solutions/problem_01.py   # reference implementation
└── tests/test_problem_01.py  # normal / edge / boundary / empty / duplicate / negative / large cases
```

**Design principles**

- **Thin YAML, testable Python.** Workflows only orchestrate; all logic lives in `dsa_agent/` and is covered by self-tests.
- **No third-party dependencies.** The agent uses only the Python standard library, so nothing extra is installed next to your API key or write token.
- **Generate into staging, then merge.** Generation never touches the repository. A lesson becomes visible only after it passes validation and is merged atomically.
- **History is the source of truth.** Summaries (current day, completed topics, revision queue) are recomputed from the lesson list on every save, so they cannot drift.

---

## 3. How a daily run works

```
          ┌──────────────────────────── dsa-daily.yml ────────────────────────────┐
schedule ─┤                                                                       │
 or manual│  generate (contents: read, AI secret)                                 │
          │   1. checkout latest branch tip (no stored credentials)               │
          │   2. agent.py check        → config/roadmap/prompts/progress valid?   │
          │   3. agent.py generate                                                │
          │      a. plan: lesson for today's date exists? → skip (exit 0)         │
          │      b. choose topic: manual > due revision > next roadmap topic      │
          │      c. AI: lesson outline + N problem statements (JSON, validated)   │
          │      d. per problem: AI → solution + starter + tests                  │
          │         → static safety checks → tests in Docker sandbox              │
          │         → tests must FAIL against the starter (no vacuous tests)      │
          │         → on failure: AI repair with the failure log (≤ 3 rounds)     │
          │      e. render Markdown, re-run all tests on the assembled folder     │
          │   4. upload staging folder as an artifact                             │
          │                                                                       │
          │  validate (contents: read, NO secrets)                                │
          │   5. re-run every test in a fresh sandbox (independent check)         │
          │                                                                       │
          │  publish (contents: write, never executes generated code)             │
          │   6. fetch latest tip → apply (re-checks duplicates) → commit → push  │
          │      push rejected? → refetch, re-apply, retry (3×)                   │
          └───────────────────────────────────────────────────────────────────────┘
```

**Idempotency.** A lesson is keyed by its date in the configured timezone.

- If `progress.json` already has a lesson for today, `generate` exits successfully without calling the AI.
- `apply` repeats that check against the *latest* branch tip, so two overlapping runs, or a retried publish job, never add a duplicate.
- A `concurrency` group queues runs instead of running them in parallel.

**Failure handling.**

| Failure | Behaviour |
|---------|-----------|
| AI API rate limit / 5xx / timeout | Retried with exponential backoff + jitter (honours `Retry-After`), bounded by `ai.maxAttempts`. |
| Invalid / malformed AI JSON | Re-asked with the exact validation error, bounded by `ai.maxAttempts`. |
| Bad API key (401/403) | Fails immediately with a hint to check the secret. |
| Generated tests fail | AI repair loop with the failure output, bounded by `maxRepairAttempts`; then the run fails. |
| Any failure before publish | Nothing is committed and `progress.json` is untouched. The next run simply tries again. |
| Push race | Refetch, re-apply on the new tip, retry; never force-pushes. |

Logs use collapsible groups, warning/error annotations and a **job summary** listing the topic, the reason it was chosen, the model used and the generated problems.

---

## 4. Security model

| Concern | Mitigation |
|---------|------------|
| Token scope | Workflow-level `permissions: {}`. Only `publish` gets `contents: write`; `generate`/`validate` are read-only and check out with `persist-credentials: false`. |
| Secret exposure | API keys are passed only to the generate step's environment, sent only in HTTPS headers, never logged (GitHub also masks them). The validate and publish jobs have no secrets. |
| Untrusted generated code | Runs only inside Docker with `--network none`, read-only root FS, read-only code mount, unprivileged user (`65534`), all capabilities dropped, `no-new-privileges`, memory/CPU/PID limits and a timeout. The host environment (keys, tokens) is not passed in. Verified: no network, no writes, no env leakage, fork bombs and memory bombs contained. |
| Defence in depth | Static checks reject generated code that imports OS/network/process modules or uses `eval`/`exec`/`open`/`require`/`process` etc. The model never chooses file paths. `publish.sh` refuses to commit changes outside `dsa/`. |
| Write job | `publish` copies files and edits JSON only; it never runs generated code. |
| Supply chain | Every action is pinned to a full commit SHA; sandbox images and actionlint are pinned by digest. |
| Script injection | `workflow_dispatch` inputs reach scripts via environment variables, never `${{ }}` interpolation inside `run:`. |
| Process sandbox | Refused inside GitHub Actions; it exists only for local development. |

---

## 5. Configuration

### Secrets (Settings → Secrets and variables → Actions → *Secrets*)

| Secret | Purpose |
|--------|---------|
| `GEMINI_API_KEY` | Google Gemini via the native API. Works on the **free tier**. |
| `OPENAI_API_KEY` | OpenAI or any OpenAI-compatible endpoint. |
| `ANTHROPIC_API_KEY` | Anthropic Claude. |

With `ai.provider: "auto"` (the default) the agent uses whichever key exists (order: OpenAI, Anthropic, Gemini). Set `DSA_AI_PROVIDER` if you store more than one.

**Gemini free tier notes.** A daily run makes only about 6–8 requests, well within the free daily quota. Rate-limit (429) responses are retried after the wait time Gemini asks for. If you exhaust the daily quota, that day's run fails cleanly and the next run tries again. On the free tier, Google may use prompts to improve its products; that is harmless for DSA lessons, but don't put private data in prompts.

### Repository variables (same page → *Variables*; all optional)

| Variable | Example | Effect |
|----------|---------|--------|
| `DSA_AI_PROVIDER` | `gemini` | Force a provider (`gemini`, `openai`, `anthropic`). |
| `DSA_AI_MODEL` | `gemini-3.5-flash` | Override the model from `agent.json`. |
| `DSA_AI_FALLBACK_MODELS` | `gemini-3.5-flash,gemini-3.1-flash-lite` | Override the fallback list (`none` disables fallbacks). |
| `OPENAI_BASE_URL` | `https://openrouter.ai/api/v1` | Use any OpenAI-compatible API (OpenRouter, Azure OpenAI, Groq, ...). Must be HTTPS. |
| `DSA_LANGUAGE` | `javascript` | Lesson language for *new* lessons (`python`, `javascript`). |
| `DSA_TIMEZONE` | `Asia/Kolkata` | Timezone that defines "today" for idempotency. |
| `DSA_PAUSED` | `true` | Pause scheduled lessons (manual runs still work). |

### `config/agent.json`

| Key | Default | Meaning |
|-----|---------|---------|
| `language` | `python` | `python` (unittest) or `javascript` (node:test). Neither needs packages. |
| `timezone` | `UTC` | IANA timezone for the lesson date. |
| `lessonsDir` | `dsa` | Where lessons and `progress.json` live. |
| `problemsPerDay` / `maxProblemsPerDay` | `5` / `8` | Problems per lesson and the upper bound for manual requests. |
| `defaultDifficulty` | `progressive` | `progressive` (Easy → Hard ladder), `easy`, `medium`, `hard`. |
| `minTestsPerProblem` | `6` | Minimum number of test cases that must actually run per problem. |
| `maxRepairAttempts` | `3` | AI repair rounds per problem before the run fails. |
| `revision.enabled` | `true` | Turn spaced revision on or off. |
| `revision.intervalsInDays` | `[7, 21, 45]` | Revision offsets, counted in lesson days after a topic is learned. |
| `revision.minNewLessonsBetweenRevisions` | `2` | Keeps revisions from crowding out new material. |
| `ai.models` | `gpt-5`, `claude-sonnet-5-5`, `gemini-3.8-flash` | Model per provider. |
| `ai.fallbackModels` | `gemini`: `gemini-3.5-flash`, `gemini-3.1-flash-lite` | Used in order when the main model stays overloaded (HTTP 503/429 after retries) or doesn't exist (404). The switch lasts for the rest of the run. |
| `ai.geminiThinkingLevel` | `low` | Gemini "thinking" effort (`minimal`/`low`/`medium`/`high`, or `null` for the model default). Lower is much faster; dropped automatically if a model rejects it. |
| `ai.temperature` | `null` | `null` = provider default (some reasoning models reject custom values). |
| `ai.maxOutputTokens` | `24000` | Increase if logs say a response was truncated. |
| `ai.requestTimeoutSeconds` / `ai.maxAttempts` | `600` / `4` | Per-request timeout and bounded retries. |
| `sandbox.mode` | `docker` | `docker` (always in CI) or `process` (local only, no isolation). |
| `sandbox.timeoutSeconds`, `memory`, `cpus`, `pidsLimit` | `120`, `512m`, `1`, `128` | Sandbox limits per test run. |

The CI workflow validates every change to these files (`agent.py check`).

---

## 6. Changing the schedule

GitHub only reads the cron expression from the workflow file. Edit `.github/workflows/dsa-daily.yml`:

```yaml
on:
  schedule:
    - cron: "0 6 * * *"     # minute hour day-of-month month day-of-week, in UTC
```

Examples: `"30 1 * * *"` = 07:00 IST daily; `"0 6 * * 1-5"` = weekdays only; `"0 6 */2 * *"` = every other day.

Notes:

- Cron times are **UTC**, and GitHub may start scheduled runs some minutes late.
- Set `DSA_TIMEZONE` so the lesson *date* matches your day.
- Scheduled workflows run from the default branch only.
- In public repositories, GitHub disables schedules after 60 days without repository activity. If that happens, re-enable the workflow on the Actions tab.

---

## 7. Manually triggering a lesson

*Actions → DSA Daily Lesson → Run workflow*, with these optional inputs:

| Input | Effect |
|-------|--------|
| `topic` | A roadmap id (e.g. `binary-search`) or exact title. If you have already studied it, you get a revision lesson. Unknown ids fail with the list of valid ids. |
| `difficulty` | `default`, `progressive`, `easy`, `medium`, `hard`. |
| `problems` | Number of problems (1 to `maxProblemsPerDay`). |
| `force` | Regenerate **today's** lesson in place (same day number; same topic unless `topic` is set). |
| `extra_lesson` | Add an **additional** lesson today, e.g. to go faster. |

Without `force` or `extra_lesson`, a manual run on a day that already has a lesson does nothing.

From a terminal with the GitHub CLI:

```bash
gh workflow run dsa-daily.yml -f topic=binary-search -f difficulty=medium -f problems=5
gh workflow run dsa-daily.yml -f force=true
```

---

## 8. Progress tracking

`dsa/progress.json` is the agent's memory. The agent reads it before every run and only ever appends to it, or replaces a day when you use `force`.

```jsonc
{
  "schemaVersion": 1,
  "currentDay": 12,                       // ─┐
  "lastLessonDate": "2026-10-19",         //  │ derived: recomputed from
  "topicsCompleted": ["big-o", "arrays"], //  │ "lessons" on every save
  "nextRoadmapTopic": "strings",          //  │
  "roadmapProgress": "11/59",             //  │
  "upcomingRevisions": [{ "topic": "big-o", "dueDay": 15, "stage": 2, "requested": false }],
  "stats": { "lessons": 12, "problemsGenerated": 60, "problemsCompleted": 23, ... }, // ─┘
  "lessons": [
    {
      "day": 1, "date": "2026-10-08", "topic": "big-o", "topicTitle": "Big O Notation & Complexity Analysis",
      "phase": "Fundamentals", "kind": "new", "revisionStage": 0, "difficulty": "progressive",
      "language": "python", "problemsGenerated": 5, "problems": [ ... ], "conceptsCovered": [ ... ],
      "revisionRequired": true,          // derived: further revisions are scheduled
      "status": "generated",             // ✏️ you: generated | in-progress | completed | skipped
      "problemsCompleted": 0,            // ✏️ you: how many you solved yourself
      "requestRevision": false,          // ✏️ you: true = revise this topic as soon as possible
      "generatedAt": "...", "generationId": "...", "generator": { "provider": "...", "model": "..." }
    }
  ]
}
```

You can edit the ✏️ fields directly on github.com. The validation workflow checks the file, and the next run recomputes the summary. After a hand edit you can also run `python .github/agents/scripts/agent.py reindex` to refresh `dsa/README.md`.

---

## 9. Spaced revision

When a topic is first taught on day **L**, revisions are scheduled for days **L+7**, **L+21** and **L+45** (`revision.intervalsInDays`). Days are *lesson days*, so a paused schedule doesn't create a backlog of overdue revisions.

Each run picks, in order:

1. a topic you asked for (`topic` input);
2. a topic you flagged with `"requestRevision": true`;
3. the most overdue revision, provided at least `minNewLessonsBetweenRevisions` new lessons happened since the last revision;
4. otherwise the next new roadmap topic.

Revision lessons give a concise recap and **new, harder problems**. The prompt lists every earlier problem title for that topic so the AI doesn't repeat them. A late revision counts towards every stage already due, so the queue can't grow without bound. When the roadmap is finished, the agent keeps revising the topic you practised least recently.

---

## 10. Practising

For each problem:

1. Read `exercises/problem-NN.md`. The hint is collapsed.
2. Write your solution in `practice/problem_NN.py`, which already contains the signature.
3. Run the tests against **your** code, from the day folder:
   ```bash
   cd dsa/day-001
   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
   # JavaScript: DSA_SOLUTIONS_DIR=practice node --test tests/problem-01.test.js
   ```
4. Compare with `solutions/problem-NN.md`.

No local machine? Edit `practice/` files on github.com or in a Codespace and commit. The **DSA Validation** workflow runs a *practice report* (pass/fail per attempted problem) in its job summary. It never fails the build because of your work in progress.

---

## 11. Troubleshooting

Open the failed run on the Actions tab. Read the job summary first, then expand the log groups.

| Symptom | Fix |
|---------|-----|
| `no AI API key found` | Add `GEMINI_API_KEY`, `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` as a repository **secret** (not a variable). |
| Gemini `HTTP 503 ... experiencing high demand` | Google-side overload, common on the free tier. The agent retries, then switches to the next model in `ai.fallbackModels`. If runs are often slow, make a fallback model the main one via `DSA_AI_MODEL`. |
| Gemini `HTTP 429 ... RESOURCE_EXHAUSTED` after retries | Free-tier quota used up; the next scheduled run retries. Or pick a model with a higher free quota via `DSA_AI_MODEL`. See your limits in AI Studio. |
| `HTTP 401/403 ... check that the API key secret` | Key is wrong, expired, or lacks access to the model; set `DSA_AI_MODEL` to a model you can use. |
| `HTTP 404` / `model not found` | The model name is unavailable; set `DSA_AI_MODEL`. |
| `response was truncated` | Raise `ai.maxOutputTokens` in `agent.json`. |
| `problem N still fails validation after 3 repair attempts` | The model could not produce correct code; nothing was committed. Re-run, or use a stronger model. |
| `Only N tests ran` / `tests PASS against the unimplemented starter` | Quality gates working as intended; the repair loop usually fixes it. Persisting? Use a stronger model. |
| Run says "already exists; nothing to do" | Idempotency: today's lesson exists. Use `force` or `extra_lesson`. |
| Publish fails with `403` / `Permission denied` | Enable *Read and write permissions* (Settings → Actions → General). |
| Publish fails on a protected branch | Allow `github-actions[bot]` to bypass the rule, or run the workflow on an unprotected branch (it pushes to the branch it runs on). |
| `day N already exists in progress.json (another run published first)` | Two runs raced; just re-run. Nothing was corrupted. |
| Scheduled runs stopped | Check that `DSA_PAUSED` isn't `true` and the workflow isn't disabled on the Actions tab. |
| Validation workflow fails after you edited `progress.json` | The log names the invalid field (e.g. `problemsCompleted` larger than `problemsGenerated`). |

Generated lessons from a failed run are kept as a workflow artifact (`dsa-lesson-<run id>-<attempt>`) for 7 days when the failure happened after generation.

---

## 12. Local development (optional)

Nothing here is needed for normal use; GitHub runs everything. To hack on the agent (Python ≥ 3.9 and optionally Docker):

```bash
python .github/agents/scripts/agent.py check
python .github/agents/scripts/agent.py plan                    # what would run today (no AI calls)
python -m unittest discover -s .github/agents/tests -v         # self-tests (fake AI, real test runs)

# full local run (uses your key; Docker sandbox by default)
OPENAI_API_KEY=... python .github/agents/scripts/agent.py run
# without Docker (NO isolation; only for code you trust)
DSA_SANDBOX=process OPENAI_API_KEY=... python .github/agents/scripts/agent.py run

python .github/agents/scripts/agent.py validate --all          # re-validate every lesson
python .github/agents/scripts/agent.py practice --day 1        # test your practice/ solutions
```

---

## 13. Extending the agent

- **Curriculum**: edit `roadmap/roadmap.json`. Order defines teaching order; never rename an id that has already been taught.
- **Prompts**: edit `prompts/*.md`. Placeholders use `{{name}}`; unknown placeholders fail fast in `check` and the self-tests.
- **New language**: add a `LanguageProfile` in `scripts/dsa_agent/languages.py`. It defines the file names, test command, sandbox image (pin by digest), test-count regex, prompt conventions, import header and static safety rules.
- **New AI provider**: subclass `Provider` in `scripts/dsa_agent/ai.py` (one `complete(system, user)` method), add its key to `KEY_ENV`, register it in `create_provider`, add it to `PROVIDERS` in `config.py`, and pass its secret in `dsa-daily.yml`.
