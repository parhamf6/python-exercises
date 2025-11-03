# https://www.codewars.com/kata/52742f58faf5485cae000b9a/python
def format_duration(s):
    if s == 0:
        return "now"
    SECONDS_IN_YEAR = 365 * 24 * 3600
    SECONDS_IN_DAY = 24 * 3600
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    years = s // SECONDS_IN_YEAR
    s %= SECONDS_IN_YEAR
    days = s // SECONDS_IN_DAY
    s %= SECONDS_IN_DAY
    hours = s // SECONDS_IN_HOUR
    s %= SECONDS_IN_HOUR
    minutes = s // SECONDS_IN_MINUTE
    seconds = s % SECONDS_IN_MINUTE
    parts = []
    if years:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if days:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds:
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")
    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return " and ".join(parts)
    else:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
