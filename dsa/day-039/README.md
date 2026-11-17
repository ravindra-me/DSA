# Day 39: Day 39: Binary Trees — Terminology, Representation, and Structural Recursion

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 39 | 2026-11-17 | Trees | New topic | progressive | Python 3.12 |

Until now, linear structures like arrays and linked lists have organized data sequentially. A binary tree introduces hierarchical relationships where each element can branch into two distinct sub-paths: left and right. This lesson establishes the fundamental vocabulary of trees, demonstrates how linked nodes model branching hierarchies, and reveals how recursion mirrors the recursive definition of a tree itself.

## Topic

**Binary Trees**: nodes and children, tree terminology, building trees, recursive tree functions

## Learning Objectives

By the end of this lesson you should be able to:

- Define core tree terminology: root, leaf, parent, child, ancestor, descendant, depth, and height.
- Model binary trees in Python using reference-linked node classes.
- Formulate tree algorithms recursively using the fundamental divide-and-conquer paradigm (base case on null/leaf, recursive call on children, combine results).
- Analyze time and auxiliary space complexity across both balanced and degenerate (skewed) trees.
- Implement core structural operations including height calculation, tree equality, symmetry verification, inversion, and path validation.

## Concept Explanation

### What it is

A binary tree is a hierarchical data structure composed of nodes. Unlike a linked list node which has a single `next` reference, a binary tree node holds a value and up to two references: `left` and `right`. If a reference points to nothing, it is empty (`None`).

The structure is inherently recursive: a binary tree is either empty (`None`), or it is a root node containing data along with two subtrees (left subtree and right subtree), each of which is itself a binary tree.

### Why it exists

Linear structures enforce a single predecessor and successor. While simple, searching an unsorted linear structure requires $O(n)$ time, and maintaining sorted order in dynamic arrays takes $O(n)$ time per insertion/deletion.

Binary trees introduce branching. In balanced configurations, dividing decisions into left and right branches cuts the search space in half at each step, achieving $O(\log n)$ access, search, and update speeds while modeling hierarchical relationships such as file systems, syntax trees in compilers, and decision processes.

### When to use it

Use binary trees when:
- Data is inherently hierarchical (e.g., expression trees, organizational charts).
- You need to dynamically maintain sorted data with logarithmic search, insertion, and deletion (via Binary Search Trees or self-balancing variants).
- The problem asks about branching choices, path aggregations, or structural symmetry over divided subsets.

### When NOT to use it

Do not use general binary trees when:
- You only need simple sequential iteration or index-based random access (use an array/list).
- You need strict constant-time lookups without ordering requirements (use a hash map or hash set).
- Each node must branch into an arbitrary, unbounded number of children (use an n-ary tree or adjacency list graph).

### How it works internally

1. **Anatomy of a Tree**:
   - **Root**: The topmost node with no incoming edges.
   - **Edge**: The link connecting a parent to a child.
   - **Leaf**: A node with both `left` and `right` set to `None`.
   - **Depth**: The number of edges from the root down to a given node (root depth is 0).
   - **Height**: The number of edges on the longest downward path from a node to a leaf (a leaf has height 0, and an empty tree is conventionally height -1 or 0 depending on whether nodes or edges are counted).

2. **The Recursive Blueprint**:
   Because every child of a binary tree is the root of its own binary subtree, virtually every binary tree algorithm follows this template:
   - **Base Case**: Handle the empty tree (`if root is None: return ...`). Often leaf nodes are also handled explicitly.
   - **Recurse**: Compute results on `root.left` and `root.right` independently.
   - **Combine**: Combine the left and right answers with `root.val` to produce the result for the current subtree.

### Common mistakes

- Forgetting the base case when `root is None`, causing an `AttributeError: 'NoneType' object has no attribute 'left'` on empty trees or leaf children.
- Confusing node count with edge count when computing tree height (be clear on whether a single-node tree has height 0 or height 1 for the given problem context).
- Treating the recursion call stack as $O(\log n)$ in all cases; a degenerate (skewed) tree behaves like a linked list, degrading the call stack space to $O(n)$.
- Attempting to modify tree links before reading both child references, causing loss of references to unvisited subtrees.
- Re-computing values redundantly across children (e.g., calling height repeatedly inside another recursive function), leading to unintentional $O(n^2)$ runtimes.

### Real-world applications

- Abstract Syntax Trees (ASTs): Compilers and interpreters parse code into tree structures to evaluate expressions and verify grammar.
- DOM (Document Object Model): Web browsers represent HTML elements and their nested components as a tree structure.
- Compression (Huffman Coding): Binary prefix trees represent variable-length encodings for characters based on frequency.
- Routing Tables and Network Packet Classification: IP prefix trees (tries / radix trees) route network traffic efficiently.

## Example

Consider computing the maximum depth (number of nodes along the longest root-to-leaf path) of this tree:

```
       1
      / \
     2   3
        /
       4
```

Recursive evaluation trace for `max_depth(root)`:
1. `max_depth(1)`:
   - Calls `max_depth(2)`:
     - Calls `max_depth(None)` for left child $\to$ returns `0`.
     - Calls `max_depth(None)` for right child $\to$ returns `0`.
     - Returns `1 + max(0, 0) = 1`.
   - Calls `max_depth(3)`:
     - Calls `max_depth(4)`:
       - Both children of 4 are `None` $\to$ returns `1 + max(0, 0) = 1`.
     - Right child of 3 is `None` $\to$ returns `0`.
     - Returns `1 + max(1, 0) = 2`.
   - Returns `1 + max(1, 2) = 3`.

The maximum depth is `3`.

## Visual Explanation

```text
Binary Tree Structure and Terminology:

         [ 10 ]  <-- Root (Depth = 0, Height = 2)
        /      \
    [ 5 ]      [ 15 ]  <-- Internal Node / Subtree Root
    /   \        \
  [ 2 ] [ 7 ]    [ 20 ]  <-- Leaves (Depth = 2, Height = 0)
  
  Tree Height = 2 (edges from root to deepest leaf)
  Total Node Count = 5

Degenerate (Skewed) Tree (Degrades to Linked List):
  [ 1 ]
     \
     [ 2 ]
        \
        [ 3 ]  <-- Height = 2, Space Complexity = O(N) stack frames
```

## Complexity

- **Time Complexity:** O(N) for standard traversals and structural inspections, where N is the number of nodes, because every node must be visited at least once.
- **Space Complexity:** O(H) auxiliary call stack space, where H is the height of the tree. H = O(log N) for balanced trees, and H = O(N) for degenerate skewed trees.

Always analyze tree algorithms in terms of both balanced ($H = \lfloor \log_2 N \rfloor$) and degenerate ($H = N$) shapes. When building algorithms that return multiple values (e.g., both height and balance status), use a single pass bottom-up recursion to avoid the common $O(N^2)$ trap of redundant traversals.

## Interview Perspective

1. **What is the difference between a complete, a full, and a perfect binary tree?**
   <details><summary>What a strong answer covers</summary>

   A full binary tree requires every node to have 0 or 2 children. A complete binary tree has all levels completely filled except possibly the last, which is filled from left to right without gaps. A perfect binary tree has all interior nodes with 2 children and all leaves at the exact same depth ($2^{h+1}-1$ total nodes).

   </details>
2. **Why is the space complexity of tree recursion O(H) rather than O(N)?**
   <details><summary>What a strong answer covers</summary>

   The call stack only holds frames for the nodes along the current root-to-leaf path being explored. Once a subtree returns, its frames are popped. Thus, the maximum stack depth equals the height of the tree $H$. In balanced trees $H = O(\log N)$, but in skewed trees $H = O(N)$.

   </details>
3. **How can you convert a recursive tree traversal into an iterative one?**
   <details><summary>What a strong answer covers</summary>

   By managing an explicit `list` as a stack (for depth-first traversals like preorder, inorder, postorder) or a `collections.deque` as a queue (for breadth-first / level-order traversal).

   </details>
4. **What is the difference between node depth and node height?**
   <details><summary>What a strong answer covers</summary>

   Depth is measured top-down: the number of edges from the root to that node (root depth is 0). Height is measured bottom-up: the number of edges on the longest path from that node down to a leaf (leaf height is 0).

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Calculate Maximum Tree Depth](exercises/problem-01.md) | Easy | Fundamental bottom-up tree recursion | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Same Tree Verification](exercises/problem-02.md) | Easy/Medium | Dual-node recursive traversal and structural identity | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Invert Binary Tree](exercises/problem-03.md) | Medium | In-place structural transformation via recursive swap | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Check Symmetric Tree](exercises/problem-04.md) | Medium/Hard | Mirror recursion / symmetric divide and conquer | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Path Sum Validation and Target Matching](exercises/problem-05.md) | Hard | Root-to-leaf recursive path tracking and backtracking accumulation | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-039
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: TreeNode class structure, Tree terminology (root, leaf, height, depth), Bottom-up recursion, Tree equivalence and structural isomorphism, Symmetry and tree reflection, In-place tree mutation, Root-to-leaf path verification*
