# Solution 3: Text Editor with Undo History

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** State restoration and history management via dual stacks

## Approach

Represent the editor's text as a list of characters and record inverse operations on an undo stack. When `type_char` is invoked, record a delete operation. When `delete_char` succeeds, record an append operation with the removed character. `undo` simply pops the most recent inverse action from the stack and executes it without recording.

## Thought Process

A naive approach might store a full snapshot of the text string after each operation. However, with up to $10^5$ operations, storing snapshots of length up to $O(N)$ would take $O(N^2)$ memory and time, which is too slow and would lead to out-of-memory errors.

Instead of snapshotting the entire state, we can use the Command pattern / inverse delta logging using a stack. Because operations are strictly LIFO (last-in, first-out), a stack is the ideal data structure:
- `type_char(ch)` appends `ch` to the text list. Its inverse is removing the character at the end. We push `('DELETE',)` onto the undo stack.
- `delete_char()` pops the character `ch` from the end of the text list. If text was empty, nothing happened, so nothing is pushed. If text was not empty, its inverse is re-appending `ch`. We push `('TYPE', ch)` onto the undo stack.
- `undo()` pops the top action from the undo stack and applies it directly to the text list without recording anything onto the undo stack.

All mutating operations run in $O(1)$ time, and `get_text()` runs in $O(L)$ time where $L$ is the length of the string.

## Algorithm

1. Initialize an empty list `self._text` to store the characters and an empty list `self._history` for the undo stack.
2. For `type_char(ch)`: append `ch` to `self._text` and push `('DELETE',)` to `self._history`.
3. For `delete_char()`: if `self._text` is empty, return immediately without recording anything. Otherwise, pop the last character `ch` from `self._text` and push `('TYPE', ch)` to `self._history`.
4. For `undo()`: if `self._history` is empty, do nothing. Otherwise, pop `(action, *args)` from `self._history`. If `action == 'DELETE'`, pop from `self._text`. If `action == 'TYPE'`, append `args[0]` to `self._text`.
5. For `get_text()`: return `''.join(self._text)`.

## Complexity Analysis

- **Time:** O(1) amortized for `type_char`, `delete_char`, and `undo`. O(L) for `get_text()`, where L is the current text length.
- **Space:** O(N) total space, where N is the total number of valid mutating operations stored in `self._history` and `self._text`.

## Edge Cases

- Calling `delete_char()` on empty text: It is a no-op and must not push any action to the undo history.
- Calling `undo()` when the history stack is empty: It does nothing gracefully.
- Chained undos: Undoing all operations back to the empty state correctly restores initial state.
- Multiple deletes followed by undos: Each deleted character is restored in the correct reverse order.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class TextEditor:
    def __init__(self) -> None:
        """Initialize the text editor."""
        self._text: list[str] = []
        self._history: list[tuple] = []

    def type_char(self, ch: str) -> None:
        """Append character ch to the text."""
        self._text.append(ch)
        self._history.append(("DELETE",))

    def delete_char(self) -> None:
        """Delete the last character if non-empty."""
        if not self._text:
            return
        removed = self._text.pop()
        self._history.append(("TYPE", removed))

    def undo(self) -> None:
        """Undo the most recent modifying operation."""
        if not self._history:
            return
        action = self._history.pop()
        if action[0] == "DELETE":
            self._text.pop()
        elif action[0] == "TYPE":
            self._text.append(action[1])

    def get_text(self) -> str:
        """Return the current text as a string."""
        return "".join(self._text)
```
