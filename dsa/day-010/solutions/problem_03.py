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
