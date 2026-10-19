class TextEditor:
    def __init__(self) -> None:
        """Initialize the text editor."""
        raise NotImplementedError

    def type_char(self, ch: str) -> None:
        """Append character ch to the text."""
        raise NotImplementedError

    def delete_char(self) -> None:
        """Delete the last character if non-empty."""
        raise NotImplementedError

    def undo(self) -> None:
        """Undo the most recent modifying operation."""
        raise NotImplementedError

    def get_text(self) -> str:
        """Return the current text as a string."""
        raise NotImplementedError
