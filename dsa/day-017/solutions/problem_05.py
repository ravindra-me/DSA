import sys

sys.setrecursionlimit(30000)

def parse_bool_expr(expression: str) -> bool:
    """Parses and evaluates a boolean expression string recursively."""
    i = 0
    
    def parse() -> bool:
        nonlocal i
        char = expression[i]
        i += 1
        
        if char == 't':
            return True
        if char == 'f':
            return False
            
        op = char
        i += 1  # Skip '(' 
        
        children = []
        while True:
            children.append(parse())
            if expression[i] == ')':
                i += 1  # Skip ')'
                break
            elif expression[i] == ',':
                i += 1  # Skip ','
                
        if op == '!':
            return not children[0]
        elif op == '&':
            return all(children)
        else:  # op == '|'
            return any(children)
            
    return parse()
