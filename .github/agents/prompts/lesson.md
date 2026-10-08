Create Day {{day}} of a structured DSA course.

## Lesson
- Topic: **{{topic_title}}** (id: `{{topic_id}}`)
- Roadmap phase: {{phase_title}}
- Key concepts to cover: {{concepts}}
- Lesson type: {{lesson_type}}
- Topics the learner has already studied (you may rely on these; avoid depending on anything not listed): {{learned_topics}}
- Programming language for signatures: {{language}}

{{revision_guidance}}

## Problems
Design exactly {{problem_count}} problems with these difficulties, in this order: {{difficulties}}.
- Each problem must exercise a DIFFERENT aspect or pattern of the topic. No trivial variations of each other.
- Progress genuinely in difficulty. The last problems should be interview-grade.
- Problems must be solvable as pure functions (or small classes) with deterministic results, so they can be unit-tested.
- Do not reuse these previously generated problems for this topic: {{previous_problems}}
- `expectedApproach` gives a HINT about the technique to use (e.g. "two pointers moving inward"), never the full solution or code.
- `signature` is the exact {{language}} signature(s) the learner must implement (code only, no body; include helper type definitions such as ListNode only by name).
- `exports` lists every symbol tests need to import: the function(s) or class(es) to implement plus any helper types (e.g. ListNode) the solution file must define.

Language conventions that the signatures must follow:
{{language_conventions}}

## Required JSON schema
{
  "title": "string: lesson title",
  "summary": "string: 2-4 sentence motivating introduction (Markdown)",
  "objectives": ["string: what the learner can do by the end (3-6 items)"],
  "concept": {
    "whatItIs": "Markdown: beginner-friendly explanation with intuition, not just a definition",
    "whyItExists": "Markdown: the problem it solves / what goes wrong without it",
    "whenToUse": "Markdown: signals in a problem statement that suggest this technique",
    "whenNotToUse": "Markdown: situations where it is the wrong tool and what to use instead",
    "howItWorks": "Markdown: step-by-step internals, invariants, and why it is correct",
    "commonMistakes": ["string: concrete pitfall and how to avoid it (3-6 items)"],
    "realWorldApplications": ["string: real systems/products where this is used (2-5 items)"]
  },
  "example": "Markdown: one small worked example traced step by step (code allowed in fenced blocks)",
  "visual": "plain-text ASCII diagram(s) of the algorithm/data structure in action (no Markdown fences)",
  "complexity": {
    "time": "string: time complexity per key operation with a one-line justification each",
    "space": "string: space complexity with justification",
    "notes": "Markdown: best/average/worst case nuances, amortization, trade-offs"
  },
  "interview": [
    { "question": "string: a common interview question or follow-up on this topic", "answerHint": "string: what a strong answer covers" }
  ],
  "conceptsCovered": ["string: short concept names covered today"],
  "problems": [
    {
      "title": "string: short unique title",
      "concept": "string: the specific aspect of the topic this problem tests",
      "statement": "Markdown: clear problem statement",
      "input": "Markdown: input format and types",
      "output": "Markdown: output format and types",
      "constraints": ["string: e.g. 1 <= n <= 10^5"],
      "examples": [ { "input": "string", "output": "string", "explanation": "string (optional, may be empty)" } ],
      "expectedApproach": "string: hint at the technique and target complexity, NOT the solution",
      "signature": "string: exact code signature(s) to implement",
      "exports": ["identifier", "..."]
    }
  ]
}

Include at least 4 interview questions and at least 2 examples per problem (one should be an edge case).
