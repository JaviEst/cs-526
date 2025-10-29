CONSECUTIVE_DAYS = 3

def calculate_snowfall(snowfall_data: list[int]) -> str:
    """
    Calculate if there exists a period of three consecutive days
    where the total snowfall exceeds half of the total snowfall recorded.

    Args:
        snowfall_data: List of integers representing cumulative snowfall data

    Returns:
        "Yes" if such a period exists, otherwise "No"
    """
    
    snowfall_data_per_day: list[int] = (
        [snowfall_data[0]] + [snowfall_data[i] - snowfall_data[i-1]
        for i in range(1, len(snowfall_data))]
    )
    result = 0
    target = snowfall_data[-1] / 2

    for idx, _ in enumerate(snowfall_data_per_day):
        if idx > (len(snowfall_data_per_day) - CONSECUTIVE_DAYS):
            break

        result = snowfall_data_per_day[idx] + snowfall_data_per_day[idx + 1] + snowfall_data_per_day[idx + 2]

        if result > target:
            return "Yes"
        
        result = 0

    return "No"