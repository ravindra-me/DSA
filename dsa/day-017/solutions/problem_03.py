def decode_string(s: str) -> str:
    """Decodes an encoded string using recursive descent parsing."""
    def parse(index: int) -> tuple[str, int]:
        result: list[str] = []
        k = 0
        
        while index < len(s):
            char = s[index]
            if char.isdigit():
                k = k * 10 + int(char)
                index += 1
            elif char == '[':
                sub_str, index = parse(index + 1)
                result.append(sub_str * k)
                k = 0
            elif char == ']':
                return "".join(result), index + 1
            else:
                result.append(char)
                index += 1
                
        return "".join(result), index

    decoded, _ = parse(0)
    return decoded
