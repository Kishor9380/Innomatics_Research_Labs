
# List of log messages from the system
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

# This variable will store how many times ERROR appears
error_total = 0

# Go through each message one by one
for message in logs:
    
    # Check if the message is exactly "ERROR"
    if message == "ERROR":
        
        # If it is ERROR, increase the count by 1
        error_total += 1

# Print the final number of ERROR messages
print("Total ERROR messages found:", error_total)
