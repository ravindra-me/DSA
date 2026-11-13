def count_visible_mountains(heights: list[int]) -> list[int]:
    """Calculates the number of visible mountains to the right for each mountain."""
    n = len(heights)
    if n <= 1:
        return [0] * n
    
    ans = [0] * n
    stack = []  # stores indices
    
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and heights[stack[-1]] < heights[i]:
            count += 1
            stack.pop()
            
        if stack:
            if heights[stack[-1]] == heights[i]:
                count += 1
                stack.pop()
            else:
                count += 1
                
        ans[i] = count
        stack.append(i)
        
    return ans
