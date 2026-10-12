def compress_string(chars: list[str]) -> int:
    """Compress consecutive identical characters in-place and return new length."""
    write_idx = 0
    read_idx = 0
    n = len(chars)

    while read_idx < n:
        char = chars[read_idx]
        run_end = read_idx
        while run_end < n and chars[run_end] == char:
            run_end += 1

        count = run_end - read_idx
        chars[write_idx] = char
        write_idx += 1

        if count > 1:
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1

        read_idx = run_end

    return write_idx
