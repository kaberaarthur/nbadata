from datetime import datetime

# Assuming 'time_string' is the time in the format '11.10. 05:00'
time_string = '11.10. 05:00'

# Parse the time string into a Python datetime object
date_format = "%m.%d. %H:%M"  # Month-Day Hour:Minute
parsed_time = datetime.strptime(time_string, date_format)

# Convert the parsed time to a string in the required format for Firestore timestamp
formatted_time = parsed_time.strftime("%Y-%m-%dT%H:%M:%SZ")

print("Formatted Time:", formatted_time)
