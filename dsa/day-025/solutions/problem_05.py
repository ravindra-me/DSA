class StreamPeakFinder:
    """Detects local peaks in a stream of numbers using a sliding 3-element window."""

    def __init__(self):
        self._prev_prev: int | None = None
        self._prev: int | None = None

    def process(self, val: int) -> int | None:
        """Process a new stream value and return a peak if finalized, else None."""
        peak = None
        if self._prev_prev is not None and self._prev is not None:
            if self._prev_prev < self._prev and self._prev > val:
                peak = self._prev

        self._prev_prev = self._prev
        self._prev = val
        return peak
