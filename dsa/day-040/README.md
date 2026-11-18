# Day 40: Day 40: Tree Traversals

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 40 | 2026-11-18 | Trees | New topic | progressive | Python 3.12 |

Traversing a tree means systematically visiting every node exactly once. Unlike linear data structures like arrays or linked lists, trees branch, requiring deliberate strategies to determine order of visitation. Today we master Depth-First Search (preorder, inorder, postorder) both recursively and iteratively, along with Breadth-First Search (level-order traversal).

## Topic

**Tree Traversals**: preorder, inorder, postorder, level order (BFS), iterative traversals

## Learning Objectives

By the end of this lesson you should be able to:

- Distinguish between Preorder, Inorder, Postorder, and Level-order traversal orders and their use cases
- Implement all recursive Depth-First Search (DFS) traversals cleanly on binary trees
- Implement Breadth-First Search (BFS) level-order traversal using an explicit queue
- Convert recursive DFS algorithms into iterative implementations using an explicit stack
- Analyze time and auxiliary space complexities across balanced and skewed trees

## Concept Explanation

### What it is

A tree traversal is a systematic process of visiting each node in a tree data structure exactly once. While linear structures have an obvious beginning and end, trees branch outward into child nodes. Tree traversals provide standard linear sequences for exploring these hierarchical structures, categorized broadly into Depth-First Search (DFS: going deep along branches before backtracking) and Breadth-First Search (BFS: exploring level by level).

### Why it exists

Without systematic traversal protocols, processing tree-based data—such as evaluating an expression tree, rendering an XML/HTML DOM, copying a file directory, or finding elements in a binary search tree—becomes chaotic. You could easily loop infinitely, skip nodes, or process dependencies out of order. Traversal algorithms define exact guarantees about when parent nodes are evaluated relative to their subtrees.

### When to use it

Use **Preorder (Node -> Left -> Right)** when you need to clone or serialize a tree, or when parent configuration must precede child operations. Use **Inorder (Left -> Node -> Right)** primarily on Binary Search Trees (BSTs) to retrieve elements in non-decreasing sorted order. Use **Postorder (Left -> Right -> Node)** when children must be processed before their parent (such as bottom-up calculations like subtree sizes, node deletions, or mathematical expression evaluation). Use **Level-order (BFS)** when distance from the root matters (such as finding the shortest path or grouping nodes by depth).

### When NOT to use it

Do not use standard DFS when searching for the shallowest occurrence or shortest path in an unbounded or deep tree, as DFS may dive down infinite or very deep irrelevant branches first; use BFS instead. Conversely, avoid BFS if memory is constrained and the tree has a large branching factor, because BFS stores an entire level in memory (up to O(N) nodes at the widest level).

### How it works internally

1. **Preorder DFS**: Process the current node, recursively traverse the left subtree, then recursively traverse the right subtree.
2. **Inorder DFS**: Recursively traverse the left subtree, process the current node, then recursively traverse the right subtree.
3. **Postorder DFS**: Recursively traverse the left subtree, recursively traverse the right subtree, then process the current node.
4. **Iterative DFS**: Use an explicit `stack` data structure to simulate the call stack. For preorder, push the root, then repeatedly pop a node, process it, and push its right child before its left child (so left is popped first).
5. **Level-Order BFS**: Use an explicit FIFO `queue` (e.g., `collections.deque`). Enqueue the root. While the queue is not empty, record the current queue length (number of nodes in the current layer), pop that many nodes, append their values to the current level list, and enqueue any non-null children.

### Common mistakes

- Forgetting to check for `None`/null root at the very beginning of the traversal function.
- In iterative preorder traversal, pushing the left child before the right child onto the stack (since stacks are LIFO, pushing right first ensures left is popped and processed first).
- Confusing level-by-level batching in BFS: forgetting to snapshot `len(queue)` at the start of a level loop, causing children of the next level to be mixed into the current level.
- Exceeding Python's recursion limit on skewed trees (where depth reaches O(N)) when an iterative approach or `sys.setrecursionlimit` is necessary.
- Modifying the tree structure during traversal without taking into account pointer invalidation.

### Real-world applications

- Compilers and interpreters: Abstract Syntax Tree (AST) evaluation uses postorder traversal to evaluate operands before applying operators.
- File systems: Computing directory sizes (`du` command) requires postorder traversal (children sizes must be summed before reporting parent folder size).
- Document Object Model (DOM): Rendering and styling web pages use preorder and level-order traversals to cascade styles from parent to children.
- Serialization and Deserialization: Storing hierarchical configurations (JSON/XML/Protobuf) into linear byte streams and reconstructing them.

## Example

Consider the binary tree:
```
       1
      / \
     2   3
    / \
   4   5
```

1. **Preorder (Root, Left, Right)**:
   - Visit 1 -> Visit 2 -> Visit 4 -> Visit 5 -> Visit 3
   - Order: `[1, 2, 4, 5, 3]`

2. **Inorder (Left, Root, Right)**:
   - Subtree 2: Left 4 -> Root 2 -> Right 5 (`4, 2, 5`)
   - Root 1
   - Subtree 3: Root 3 (`3`)
   - Order: `[4, 2, 5, 1, 3]`

3. **Postorder (Left, Right, Root)**:
   - Subtree 2: Left 4 -> Right 5 -> Root 2 (`4, 5, 2`)
   - Subtree 3: Root 3 (`3`)
   - Root 1
   - Order: `[4, 5, 2, 3, 1]`

4. **Level-Order (BFS)**:
   - Level 0: `[1]`
   - Level 1: `[2, 3]`
   - Level 2: `[4, 5]`
   - Order: `[[1], [2, 3], [4, 5]]`

## Visual Explanation

```text
Tree Structure:             Queue state during BFS:
            (1)                   Initial:   [1]
           /   \                  Pop 1:     []       -> Push 2, 3 -> [2, 3]
         (2)   (3)                Pop 2:     [3]      -> Push 4, 5 -> [3, 4, 5]
        /   \                     Pop 3:     [4, 5]   -> No children
      (4)   (5)                   Pop 4:     [5]      -> No children
                                  Pop 5:     []       -> Done!

Iterative Preorder Stack State (LIFO):
Start: Push 1                Stack: [1]
Pop 1, Push 3, Push 2        Stack: [3, 2]       Processed: [1]
Pop 2, Push 5, Push 4        Stack: [3, 5, 4]    Processed: [1, 2]
Pop 4                        Stack: [3, 5]       Processed: [1, 2, 4]
Pop 5                        Stack: [3]          Processed: [1, 2, 4, 5]
Pop 3                        Stack: []           Processed: [1, 2, 4, 5, 3]
```

## Complexity

- **Time Complexity:** O(N) for all traversals (preorder, inorder, postorder, level-order) because every node is visited a constant number of times.
- **Space Complexity:** O(H) auxiliary space for DFS (where H is the height of tree: O(log N) average/balanced, O(N) worst-case skewed). O(W) auxiliary space for BFS (where W is the maximum width of the tree, up to O(N) for a full binary tree).

In a balanced binary tree, DFS uses O(log N) stack space while BFS uses O(N) queue space for the bottom level. In a degenerate linked-list tree, DFS uses O(N) stack frames while BFS uses O(1) queue space.

## Interview Perspective

1. **Can you uniquely reconstruct a binary tree given its preorder and postorder traversal sequences?**
   <details><summary>What a strong answer covers</summary>

   Generally no, unless you are guaranteed that every non-leaf node has exactly two children (a full binary tree). Without that guarantee, you cannot distinguish whether a single child is a left child or a right child. However, Preorder + Inorder or Postorder + Inorder can uniquely reconstruct any binary tree.

   </details>
2. **How do you implement an inorder traversal iteratively without recursion?**
   <details><summary>What a strong answer covers</summary>

   Use an explicit stack. Push the current node and move to its left child repeatedly until reaching `None`. Then pop from the stack, visit the popped node, and set current to its right child before repeating.

   </details>
3. **When would you choose BFS level-order traversal over DFS recursion?**
   <details><summary>What a strong answer covers</summary>

   When searching for the shortest path or nearest target to the root, when level-by-level aggregation is required, or when the tree is very deep and call stack overflow is a risk.

   </details>
4. **What is Morris Traversal and why is it notable?**
   <details><summary>What a strong answer covers</summary>

   Morris Traversal achieves O(N) time and O(1) auxiliary space without recursion or an explicit stack by temporarily modifying tree pointers (creating threaded binary trees pointing back from the in-order predecessor to the current node) and restoring them before completion.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Binary Tree Level Order Traversal](exercises/problem-01.md) | Easy | Level Order (BFS) with layer separation | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Iterative Inorder Traversal](exercises/problem-02.md) | Easy/Medium | Iterative DFS using an explicit stack | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Zigzag Level Order Traversal](exercises/problem-03.md) | Medium | Level Order BFS with alternating direction | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Iterative Postorder Traversal](exercises/problem-04.md) | Medium/Hard | Iterative Postorder with two-pointer tracking or two-stack approach | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Vertical Order Traversal of a Binary Tree](exercises/problem-05.md) | Hard | Coordinate-based BFS / DFS with multi-key sorting | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-040
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Preorder Traversal, Inorder Traversal, Postorder Traversal, Level Order Traversal (BFS), Iterative Stack Traversals*
