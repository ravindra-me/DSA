def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    """Validate if popped sequence could result from push/pop operations on pushed sequence."""
    stack = []
    pop_idx = 0
    
    for val in pushed:
        stack.append(val)
        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1
            
    return pop_idx == len(popped)
