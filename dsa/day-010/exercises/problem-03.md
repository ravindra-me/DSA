# Problem 3: Text Editor with Undo History

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | State restoration and history management via dual stacks | [Day 10: Stack](../README.md) |

## Problem Statement

Design a simplified text editor class `TextEditor` that supports typing characters, deleting characters, and undoing previous operations.

The editor starts with an empty string and supports:
- `type_char(ch: str) -> None`: Appends character `ch` to the end of the text.
- `delete_char() -> None`: Deletes the last character in the text. If text is empty, does nothing.
- `undo() -> None`: Reverts the most recent `type_char` or `delete_char` action. If there are no actions to undo, does nothing.
- `get_text() -> str`: Returns the current text string.

Note: Calling `undo()` should not be recorded as an action that can itself be undone (this editor only requires undo, not redo). If an action had no effect (e.g. deleting from empty text), it should not be stored as an undoable action.

## Input

Method calls on `TextEditor` instance.

## Output

`get_text()` returns `str`. Other mutating methods return `None`.

## Constraints

- At most 10^5 total method calls.
- ch is a single ASCII character.

## Examples

**Example 1**

```text
Input:  editor = TextEditor()
editor.type_char('a')
editor.type_char('b')
editor.get_text() -> 'ab'
editor.delete_char()
editor.get_text() -> 'a'
editor.undo()
editor.get_text() -> 'ab'
Output: 'ab'
```

Deleting 'b' was undone, restoring 'b'.

**Example 2**

```text
Input:  editor = TextEditor()
editor.delete_char()
editor.undo()
editor.get_text() -> ''
Output: ''
```

Deleting from empty text was a no-op, so undo also does nothing.

## Function Signature

```python
class TextEditor:
    def __init__(self) -> None:
        """Initialize the text editor."""
        pass

    def type_char(self, ch: str) -> None:
        """Append character ch to the text."""
        pass

    def delete_char(self) -> None:
        """Delete the last character if non-empty."""
        pass

    def undo(self) -> None:
        """Undo the most recent modifying operation."""
        pass

    def get_text(self) -> str:
        """Return the current text as a string."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain the current text (e.g., as a list of characters) and an undo stack recording inverse operations (e.g., ('delete') to invert a type, or ('type', char) to invert a delete). Target O(1) amortized time per operation.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
