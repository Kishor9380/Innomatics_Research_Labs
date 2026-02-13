# Message Length Analyzer

# List of messages to check
messages = ["Hi", "Welcome to the platform", "OK"]

# Go through each message in the list
for text in messages:
    
    # Find the number of characters in the message
    length = len(text)
    
    # Print the message and its length
    print("Message:", text)
    print("Length:", length)
    
    # Check if the message is longer than 10 characters
    if length > 10:
        print("This message is longer than 10 characters.")
    
    # Print a blank line for better readability
    print()
  
