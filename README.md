# DSA, One Day at a Time

A self-driving Data Structures & Algorithms course. Every day a GitHub Actions workflow writes a new lesson into [`dsa/`](dsa/README.md). Each lesson has a beginner-friendly explanation, five progressively harder problems, starter files, reference solutions and automated tests. The workflow commits the lesson only after every test passes in an isolated sandbox.

It runs entirely on GitHub, so your computer doesn't need to be on.

## How to use this repository

1. **Open today's lesson.** The newest day is at the top of [`dsa/README.md`](dsa/README.md). Each `dsa/day-NNN/README.md` covers:
   - what the topic is and why it exists
   - when to use it, and when not to
   - how it works internally
   - common mistakes and real-world uses
   - a worked example and an ASCII diagram
   - complexity
   - interview questions
2. **Solve the exercises yourself.** Each `exercises/problem-NN.md` has the statement, constraints, examples, function signature and a hidden hint, but no solution.
3. **Write your code in `practice/`.** A starter file with the signature is already there.
4. **Run the tests against your code**, from the day folder:
   ```bash
   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
   ```
   You can also commit from github.com or a Codespace; the *DSA Validation* workflow reports which of your practice solutions pass.
5. **Compare** with `solutions/problem-NN.md`. It covers the approach, thought process, algorithm, complexity, edge cases and a clean implementation.
6. **Track progress** by setting `status` / `problemsCompleted` for the day in [`dsa/progress.json`](dsa/progress.json). Set `"requestRevision": true` to get a topic revised soon.

## Curriculum

The agent follows an ordered [59-topic roadmap](.github/agents/roadmap/roadmap.json):

1. Fundamentals: Big O, arrays, strings, recursion, maths, bits
2. Linear structures: linked lists, stacks, queues, deques
3. Hashing
4. Two pointers and sliding window
5. Searching
6. Sorting
7. Trees
8. Heaps
9. Graphs: BFS/DFS through Dijkstra, Bellman-Ford, DSU and MST
10. Greedy, backtracking and dynamic programming
11. Tries, segment trees, Fenwick trees, string algorithms and advanced graphs

Earlier topics come back as **spaced revision** lessons with new problems (by default 7, 21 and 45 lesson-days later).

## Setup (one time)

1. Add a `GEMINI_API_KEY` secret (free tier works; get a key at [Google AI Studio](https://aistudio.google.com/apikey)), **or** an `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` secret (*Settings → Secrets and variables → Actions*).
2. Under *Settings → Actions → General → Workflow permissions*, choose **Read and write permissions**.
3. Done. Lessons arrive daily at 06:00 UTC. To get one right away, use *Actions → DSA Daily Lesson → Run workflow*. You can also pick a topic, difficulty and number of problems there.

Full documentation covers architecture, security model, configuration, schedule, revision logic and troubleshooting: [`.github/agents/README.md`](.github/agents/README.md).

## Repository layout

```
.github/workflows/dsa-daily.yml       daily lesson pipeline (generate → validate → publish)
.github/workflows/dsa-validation.yml  CI for the agent and every lesson
.github/agents/                       the agent: config, roadmap, prompts, scripts, self-tests
dsa/                                  your lessons + progress.json
```
