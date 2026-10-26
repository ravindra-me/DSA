def kth_grammar(n: int, k: int) -> int:
    """Return the k-th symbol in the n-th row of the grammar table."""
    if n == 1:
        return 0
    mid = 1 << (n - 2)
    if k <= mid:
        return kth_grammar(n - 1, k)
    else:
        return 1 - kth_grammar(n - 1, k - mid)
