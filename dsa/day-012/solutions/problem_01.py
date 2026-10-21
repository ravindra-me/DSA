def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return the number of days until a warmer temperature."""
    n = len(temperatures)
    answer = [0] * n
    stack: list[int] = []  # stores indices of unresolved days

    for current_day, current_temp in enumerate(temperatures):
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = current_day - prev_day
        stack.append(current_day)

    return answer
