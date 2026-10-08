The code you generated for problem {{number}} ("{{title}}") of the Day {{day}} lesson on **{{topic_title}}** failed automated validation. Diagnose the root cause and fix it.

## Problem
{{problem_json}}

## Language: {{language}}
{{language_conventions}}

## Current solutionCode (solutions/{{solution_file}})
{{solution_code}}

## Current starterCode (practice/{{solution_file}})
{{starter_code}}

## Current testCode (tests/{{test_file}}, below the generated header that imports {{exports}})
{{test_code}}

## Validation failure (attempt {{attempt}} of {{max_attempts}})
{{failure}}

## Instructions
1. Decide whether the bug is in the solution, the tests, or both. A test is wrong only if its expected value contradicts the problem statement; never weaken tests just to make them pass.
2. Keep at least as many test cases as before (minimum {{min_tests}}), and keep covering normal, edge, boundary, empty, duplicate, negative and large inputs where applicable.
3. The tests must pass against the solution and fail against the starter stub.
4. Return complete files, not diffs.

## Required JSON schema
{
  "diagnosis": "string: what was wrong and what you changed",
  "solutionCode": "string: complete corrected solution",
  "starterCode": "string: complete starter stub",
  "testCode": "string: complete corrected tests (without the generated header)"
}
