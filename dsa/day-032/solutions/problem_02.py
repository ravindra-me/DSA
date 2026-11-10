def calculate_basic_expression(s: str) -> int:
    """Evaluate a basic expression string containing digits, '+', '-', '(', ')', and spaces."""
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            res += sign * num
            num = 0
            sign = 1
        elif char == '-':
            res += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif char == ')':
            res += sign * num
            num = 0
            prev_sign = stack.pop()
            prev_res = stack.pop()
            res = prev_res + prev_sign * res
            
    res += sign * num
    return res
