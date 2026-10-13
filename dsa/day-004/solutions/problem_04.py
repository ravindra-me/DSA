import sys

def nested_sum(nested_list: list) -> int:
    """Calculates sum of all integers in a nested list structure."""
    # Increase recursion depth for deep nesting scenarios
    sys.setrecursionlimit(2000)
    
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += nested_sum(element)
        else:
            total += element
    return total
