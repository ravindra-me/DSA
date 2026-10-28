from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams together using character frequency signatures."""
    groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
    base_ord = ord('a')

    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - base_ord] += 1
        groups[tuple(count)].append(s)

    result = list(groups.values())
    result.sort(key=lambda group: (-len(group), group[0]))
    return result
