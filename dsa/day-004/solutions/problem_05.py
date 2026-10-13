from typing import List

def generate_parentheses(n: int) -> List[str]:
    """Generates all combinations of well-formed parentheses for n pairs."""
    if n <= 0:
        return []
    
    results = []
    
    def backtrack(current: str, open_count: int, closed_count: int) -> None:
        if len(current) == 2 * n:
            results.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, closed_count)
            
        if closed_count < open_count:
            backtrack(current + ")", open_count, closed_count + 1)
            
    backtrack("", 0, 0)
    return results
