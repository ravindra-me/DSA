class StreamFirstUnique:
    def __init__(self) -> None:
        """Initialize the stream data structure."""
        raise NotImplementedError

    def add(self, ch: str) -> None:
        """Add character ch to the stream."""
        raise NotImplementedError

    def get_first_unique(self) -> str:
        """Return the first unique character in the stream, or empty string."""
        raise NotImplementedError
