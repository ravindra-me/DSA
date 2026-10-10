# Student Guide

A new Data Structures & Algorithms lesson is published to this course repository every day. You work in **your own fork**: your own copy of the repository, where you solve the problems and push your code. Your fork pulls each new lesson in automatically.

```
 course repo (read-only for you)          your fork (yours to edit)
 ┌──────────────────────────┐   daily    ┌──────────────────────────────┐
 │ bot adds dsa/day-NNN/    │ ─────────► │ read lesson → solve → test   │
 │ every day                │    sync    │ → push → ✅ / ❌ on GitHub    │
 └──────────────────────────┘            └──────────────────────────────┘
```

---

## One-time setup (about 5 minutes)

1. **Fork the course repository.** Open it on GitHub and click **Fork** (top right), then **Create fork**.
2. **Enable Actions in your fork.** Open the **Actions** tab of *your fork* and click **"I understand my workflows, go ahead and enable them"**. Without this, there's no automatic sync and no test results.
3. **Clone your fork** (replace `YOUR-NAME`):
   ```bash
   git clone https://github.com/YOUR-NAME/DSA.git
   cd DSA
   ```
4. **Install Python 3.12** (3.10 or newer is required). Check with `python3 --version`.

> No laptop handy? Open your fork on GitHub and press `.` for the web editor, or use **Code → Codespaces** for a full environment in the browser.

---

## Every day

### 1. Get the new lesson

Your fork syncs automatically every day at about 13:30 IST. Then pull it to your computer:

```bash
git pull
```

If the sync didn't happen (or you want the lesson earlier), open your fork on GitHub, click **Sync fork → Update branch**, then `git pull`.

### 2. Learn

Open `dsa/day-NNN/README.md` (the newest day). It covers the concept, examples, diagrams, complexity and interview questions. Then read the problems in `dsa/day-NNN/exercises/`.

### 3. Solve

Write your code in **`dsa/day-NNN/practice/problem_01.py`**, `problem_02.py`, ... Each file already contains the function signature to implement.

Only edit files inside `practice/`. Don't change other files (lessons, tests, `progress.json`), or syncing new lessons can run into conflicts.

### 4. Test your solution

From the day's folder:

```bash
cd dsa/day-001
DSA_SOLUTIONS_DIR=practice python3 -m unittest discover -s tests -p test_problem_01.py -v   # one problem
DSA_SOLUTIONS_DIR=practice python3 -m unittest discover -s tests -v                        # all problems
cd ../..
```

`OK` means every test passed. Failures show the input, the expected answer and what your code returned.

Stuck? The full walkthrough is in `dsa/day-NNN/solutions/problem-NN.md`, but give it a real try first.

### 5. Push your work

```bash
git add dsa/
git commit -m "day 1: solved problems 1-3"
git push
```

On GitHub, open the **Actions** tab of your fork. The **DSA Validation → Check my solutions** run shows a table of your attempted problems:

| Result | Meaning |
|--------|---------|
| ✅ green run | Every problem you attempted passes its tests |
| ❌ red run | At least one attempted problem fails; the run log shows the test output |

Problems you haven't touched are ignored, so it's fine to push partial work.

---

## FAQ

**I get `TypeError: unsupported operand type(s) for |`**
Your Python is too old. Install Python 3.12.

**"Sync fork" says there's a conflict.**
You probably edited a file outside `practice/`. Click **Discard commits** only if you have nothing to keep. Otherwise, ask for help, or copy your `practice/` files somewhere safe, re-sync, and copy them back.

**Can I see other students' solutions?**
No, each fork is separate. The course's reference solutions are in `solutions/` of every lesson.

**Can I redo an old day?**
Yes. Every day's folder stays in your fork. Just edit its `practice/` files again and push.
