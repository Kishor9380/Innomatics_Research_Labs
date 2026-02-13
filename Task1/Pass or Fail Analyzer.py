# Pass / Fail Analyzer

# List of student marks
marks = [45, 78, 90, 33, 60]

# Variables to store pass and fail counts
pass_count = 0
fail_count = 0

# Check each student's marks
for score in marks:
    
    # If marks are 50 or more, student passes
    if score >= 50:
        pass_count += 1
    else:
        # If marks are less than 50, student fails
        fail_count += 1

# Print the final result clearly
print("Total Students Passed:", pass_count)
print("Total Students Failed:", fail_count)
