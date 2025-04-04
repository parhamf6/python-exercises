from datetime import datetime, timedelta

def time_difference(time1_str, time2_str):
    # Define the time format
    time_format = "%H:%M:%S"

    # Convert string inputs to datetime objects
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)

    # Calculate the difference
    if time2 > time1:
        delta = time2 - time1
    else:
        delta = (time2 + timedelta(days=1)) - time1

    # Extract hours, minutes, and seconds from the difference
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return hours, minutes, seconds

# Get user input for two times
time1_str = input("")
time2_str = input("")

# Calculate the difference
hours, minutes, seconds = time_difference(time1_str, time2_str)

# Display the result
print(f"{hours:02}:{minutes:02}:{seconds:02}")
