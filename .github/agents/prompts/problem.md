Write the reference solution, the starter stub and the automated tests for this problem from the Day {{day}} lesson on **{{topic_title}}**.

## Problem {{number}} ({{difficulty}})
{{problem_json}}

## Language: {{language}}
{{language_conventions}}

## How the code is assembled and run
- `solutionCode` is saved as `solutions/{{solution_file}}` and must define: {{exports}}.
- `starterCode` is saved as `practice/{{solution_file}}` for the learner to fill in. {{starter_hint}}
- `testCode` is saved as `tests/{{test_file}}` BELOW a generated header that already imports the test framework and {{exports}}. Write only the test classes/functions.
- Tests run in an isolated sandbox with no network or filesystem access, a {{timeout}}-second total time limit, and must be deterministic.
- The tests must PASS against `solutionCode` and must FAIL against `starterCode`.

## Test requirements
Write at least {{min_tests}} separate test cases (separate test methods/functions, not one big test). Cover, where applicable:
- normal cases, including every example from the problem statement
- edge cases and boundary values (minimum/maximum sizes and values)
- empty input
- single element
- duplicate values
- negative numbers and zero
- a large input that would time out with a naive approach that is much slower than the expected complexity (keep it under ~1 second for the correct solution)
Each test should have a descriptive name and assert on exact expected results. Compute expected values for large inputs with a simple, obviously-correct reference (e.g. a brute force on a smaller slice, or a mathematical property), not by calling the solution itself.

## Solution requirements
- Optimal or near-optimal complexity matching the expected approach, written as clean production code: clear names, small helpers where useful, comments only where they add insight.
- Handle all edge cases in the constraints. Do not print anything.

## Required JSON schema
{
  "approach": "Markdown: the key idea of the solution in a few sentences",
  "reasoning": "Markdown: the thought process - how to discover this approach from the problem statement, including a brute-force baseline and why it is improved upon",
  "algorithm": ["string: numbered algorithm steps, one per item"],
  "complexity": { "time": "string with justification", "space": "string with justification" },
  "edgeCases": ["string: edge case and how the solution handles it"],
  "solutionCode": "string: complete solution source code",
  "starterCode": "string: starter stub source code",
  "testCode": "string: test source code (without the generated header)"
}
