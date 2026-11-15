def stable_sort_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Stably sorts pairs by score using prefix-sum counting sort."""
    if len(records) <= 1:
        return list(records)

    max_score = 100
    count = [0] * (max_score + 1)

    # 1. Count frequencies
    for _, score in records:
        count[score] += 1

    # 2. Compute prefix sums (cumulative counts)
    for score in range(1, max_score + 1):
        count[score] += count[score - 1]

    # 3. Build output array iterating right-to-left to ensure stability
    output: list[tuple[str, int]] = [("", 0)] * len(records)
    for i in range(len(records) - 1, -1, -1):
        item = records[i]
        score = item[1]
        output[count[score] - 1] = item
        count[score] -= 1

    return output
