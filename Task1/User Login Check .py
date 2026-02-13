# User Login Check

# Correct login details stored in the system
correct_username = "admin"
correct_password = "1234"

# Details entered by the user (you can change these to test)
username = "admin"
password = "1234"

# Check if both username and password are correct
if username == correct_username and password == correct_password:
    # If both match, login is successful
    print("Login Successful")
else:
    # If any one is wrong, show invalid message
    print("Invalid Credentials")
