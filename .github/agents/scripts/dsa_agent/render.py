"""Deterministic Markdown rendering. The AI supplies content; the layout,
section order, links and practice instructions always come from here, so every
lesson has the same predictable structure."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Sequence

from .languages import LanguageProfile
from .select_topic import LessonPlan


def _bullets(items: Sequence[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def _unfence(text: str) -> str:
    lines = text.strip("\n").splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)


def lesson_type_label(plan: LessonPlan) -> str:
    return "New topic" if plan.kind == "new" else f"Revision (stage {plan.revision_stage})"


def problem_paths(profile: LanguageProfile, number: int) -> Dict[str, str]:
    nn = f"{number:02d}"
    return {
        "exercise": f"exercises/problem-{nn}.md",
        "notes": f"solutions/problem-{nn}.md",
        "solution": f"solutions/{profile.solution_file(number)}",
        "tests": f"tests/{profile.test_file(number)}",
        "practice": f"practice/{profile.solution_file(number)}",
    }


def practice_commands(profile: LanguageProfile, day_path: str, number: int = 1) -> str:
    nn = f"{number:02d}"
    if profile.name == "python":
        return (
            f"cd {day_path}\n"
            "# run the reference solutions\n"
            "python -m unittest discover -s tests -v\n"
            f"# test YOUR solution for problem {nn} (edit practice/{profile.solution_file(number)} first)\n"
            f"DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p {profile.test_file(number)} -v"
        )
    return (
        f"cd {day_path}\n"
        "# run the reference solutions\n"
        "node --test tests/*.test.js\n"
        f"# test YOUR solution for problem {nn} (edit practice/{profile.solution_file(number)} first)\n"
        f"DSA_SOLUTIONS_DIR=practice node --test tests/{profile.test_file(number)}"
    )


def render_readme(
    plan: LessonPlan, lesson: Dict[str, Any], problems: List[Dict[str, Any]], profile: LanguageProfile, day_path: str
) -> str:
    c = lesson["concept"]
    rows = "\n".join(
        f"| {p['number']} | [{p['title']}]({p['paths']['exercise']}) | {p['difficulty']} | {p['concept']} "
        f"| [tests]({p['paths']['tests']}) | [solution]({p['paths']['notes']}) |"
        for p in problems
    )
    interview = "\n".join(
        f"{i}. **{q['question']}**\n   <details><summary>What a strong answer covers</summary>\n\n   {q['answerHint']}\n\n   </details>"
        for i, q in enumerate(lesson["interview"], 1)
    )
    revision_note = ""
    if plan.kind == "revision":
        revision_note = (
            f"\n> **Revision day.** You first studied this topic earlier; today recaps the essentials and "
            f"gives you brand-new problems. ({plan.reason})\n"
        )
    return f"""# Day {plan.day}: {lesson['title']}

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| {plan.day} | {plan.date} | {plan.topic.phase_title} | {lesson_type_label(plan)} | {plan.difficulty} | {profile.display_name} |
{revision_note}
{lesson['summary']}

## Topic

**{plan.topic.title}**: {', '.join(plan.topic.concepts) or plan.topic.title}

## Learning Objectives

By the end of this lesson you should be able to:

{_bullets(lesson['objectives'])}

## Concept Explanation

### What it is

{c['whatItIs']}

### Why it exists

{c['whyItExists']}

### When to use it

{c['whenToUse']}

### When NOT to use it

{c['whenNotToUse']}

### How it works internally

{c['howItWorks']}

### Common mistakes

{_bullets(lesson['commonMistakes'])}

### Real-world applications

{_bullets(lesson['realWorldApplications'])}

## Example

{lesson['example']}

## Visual Explanation

```text
{_unfence(lesson['visual'])}
```

## Complexity

- **Time Complexity:** {lesson['complexity']['time']}
- **Space Complexity:** {lesson['complexity']['space']}

{lesson['complexity']['notes']}

## Interview Perspective

{interview}

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
{rows}

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
{practice_commands(profile, day_path)}
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: {', '.join(lesson['conceptsCovered'])}*
"""


def render_exercise(plan: LessonPlan, problem: Dict[str, Any], profile: LanguageProfile) -> str:
    examples = "\n\n".join(
        f"**Example {i}**\n\n```text\nInput:  {ex['input']}\nOutput: {ex['output']}\n```"
        + (f"\n\n{ex['explanation']}" if ex["explanation"] else "")
        for i, ex in enumerate(problem["examples"], 1)
    )
    paths = problem["paths"]
    return f"""# Problem {problem['number']}: {problem['title']}

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| {problem['difficulty']} | {problem['concept']} | [Day {plan.day}: {plan.topic.title}](../README.md) |

## Problem Statement

{problem['statement']}

## Input

{problem['input']}

## Output

{problem['output']}

## Constraints

{_bullets(problem['constraints'])}

## Examples

{examples}

## Function Signature

```{profile.fence}
{_unfence(problem['signature'])}
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

{problem['expectedApproach']}

</details>

## Your Turn

- Write your solution in [`{paths['practice']}`](../{paths['practice']}).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`{paths['notes']}`](../{paths['notes']}), but try first!
"""


def render_solution_notes(problem: Dict[str, Any], code: Dict[str, Any], solution_source: str, profile: LanguageProfile) -> str:
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(code["algorithm"], 1))
    return f"""# Solution {problem['number']}: {problem['title']}

> Spoiler warning: try [the exercise](../exercises/problem-{problem['number']:02d}.md) first.

**Difficulty:** {problem['difficulty']} | **Concept:** {problem['concept']}

## Approach

{code['approach']}

## Thought Process

{code['reasoning']}

## Algorithm

{steps}

## Complexity Analysis

- **Time:** {code['complexity']['time']}
- **Space:** {code['complexity']['space']}

## Edge Cases

{_bullets(code['edgeCases'])}

## Implementation

Source: [`{problem['paths']['solution']}`](../{problem['paths']['solution']}) · Tests: [`{problem['paths']['tests']}`](../{problem['paths']['tests']})

```{profile.fence}
{solution_source.rstrip()}
```
"""


def render_index(progress: Dict[str, Any], lessons_dir_name: str) -> str:
    lessons = progress["lessons"]
    stats = progress.get("stats", {})
    rows = "\n".join(
        f"| [{l['day']}](day-{l['day']:03d}/README.md) | {l['date']} | {l.get('topicTitle', l['topic'])} "
        f"| {'Revision' if l['kind'] == 'revision' else 'New'} | {l['problemsCompleted']}/{l['problemsGenerated']} "
        f"| {l['status']} |"
        for l in reversed(lessons)
    ) or "| - | - | No lessons yet: the first one arrives with the next scheduled run | - | - | - |"
    upcoming = progress.get("upcomingRevisions") or []
    upcoming_text = _bullets(
        [f"`{r['topic']}`: " + ("requested by you" if r["requested"] else f"due on day {r['dueDay']}") for r in upcoming[:10]]
    ) or "_None scheduled yet._"
    return f"""# DSA Lessons

Generated automatically by the [DSA learning agent](../.github/agents/README.md). Do not edit this file by hand; it is rebuilt from [`progress.json`](progress.json).

| Current day | Roadmap progress | Problems solved | Next new topic |
|-------------|------------------|-----------------|----------------|
| {progress.get('currentDay', 0)} | {progress.get('roadmapProgress', '0/0')} topics | {stats.get('problemsCompleted', 0)}/{stats.get('problemsGenerated', 0)} | {progress.get('nextRoadmapTopic') or 'roadmap complete'} |

## Upcoming revisions

{upcoming_text}

## All lessons

| Day | Date | Topic | Type | Solved | Status |
|-----|------|-------|------|--------|--------|
{rows}
"""


def problem_json_for_prompt(problem: Dict[str, Any]) -> str:
    keys = ("title", "concept", "statement", "input", "output", "constraints", "examples", "signature", "exports")
    return json.dumps({k: problem[k] for k in keys}, indent=2, ensure_ascii=False)
