def _insert_at_bottom(stack: list[int], item: int) -> None:
    """Recursively insert an element at the bottom of the stack."""
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    _insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack: list[int]) -> None:
    """Reverse a stack in-place using only recursion."""
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, top)
