def stable_multikey_sort(records: list[dict]) -> list[dict]:
    """Sorts records by department ascending, then salary descending, stably without built-in sort."""
    # Create a copy so we do not mutate the input list
    arr = list(records)
    n = len(arr)

    def precedes(a: dict, b: dict) -> bool:
        """Returns True if record `a` strictly precedes record `b`."""
        if a["department"] != b["department"]:
            return a["department"] < b["department"]
        return a["salary"] > b["salary"]

    # Stable insertion sort
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and precedes(current, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr
