def decode_string(s: str) -> str:
    """Decode an encoded string formatted as k[encoded_string]."""
    stack: list[tuple[str, int]] = []
    current_str: list[str] = []
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append(("".join(current_str), current_num))
            current_str = []
            current_num = 0
        elif char == "]":
            prev_str, repeat_count = stack.pop()
            decoded_chunk = prev_str + repeat_count * "".join(current_str)
            current_str = [decoded_chunk]
        else:
            current_str.append(char)

    return "".join(current_str)
