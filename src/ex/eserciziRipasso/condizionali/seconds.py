def seconds_since_noon(hours: int, minutes: int, seconds: int) -> int:
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def time_difference(hours1: int, minutes1: int, seconds1: int, hours2: int, minutes2: int, seconds2: int) -> int:
    total_seconds1 = seconds_since_noon(hours1, minutes1, seconds1)
    total_seconds2 = seconds_since_noon(hours2, minutes2, seconds2)
    
    return abs(total_seconds1 - total_seconds2)