from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams together and sort groups according to specifications."""
    if not words:
        return []

    grouped: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        signature = "".join(sorted(word))
        grouped[signature].append(word)

    result: list[list[str]] = []
    for group in grouped.values():
        group.sort()
        result.append(group)

    result.sort(key=lambda g: (-len(g), g[0]))
    return result
