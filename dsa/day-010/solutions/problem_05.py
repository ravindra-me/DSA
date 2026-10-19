def decode_string(s: str) -> str:
    """Decode the nested encoded string."""
    stack: list[tuple[str, int]] = []
    curr_str = ""
    curr_k = 0

    for char in s:
        if char.isdigit():
            curr_k = curr_k * 10 + int(char)
        elif char == "[":
            stack.append((curr_str, curr_k))
            curr_str = ""
            curr_k = 0
        elif char == "]":
            prev_str, repeat_count = stack.pop()
            curr_str = prev_str + (curr_str * repeat_count)
        else:
            curr_str += char

    return curr_str
