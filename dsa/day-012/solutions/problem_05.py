def sum_subarray_mins(arr: list[int]) -> int:
    """Compute sum of all contiguous subarray minimums modulo 10^9 + 7."""
    MOD = 1_000_000_007
    n = len(arr)
    if n == 0:
        return 0

    # ple[i] stores the index of the previous strictly less element
    ple = [-1] * n
    # nle[i] stores the index of the next less or equal element
    nle = [n] * n

    # Compute PLE
    stack: list[int] = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            ple[i] = stack[-1]
        stack.append(i)

    # Compute NLE
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            nle[i] = stack[-1]
        stack.append(i)

    total = 0
    for i in range(n):
        left_count = i - ple[i]
        right_count = nle[i] - i
        total = (total + arr[i] * left_count * right_count) % MOD

    return total
