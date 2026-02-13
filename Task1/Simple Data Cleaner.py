# Simple Data Cleaner

# List of names with extra spaces and mixed letter cases
names = [" Alice ", "bob", " CHARLIE "]

# Empty list to store cleaned names
cleaned_names = []

# Go through each name in the list
for name in names:
    
    # Remove spaces from beginning and end
    name_without_spaces = name.strip()
    
    # Convert the name to lowercase
    name_lowercase = name_without_spaces.lower()
    
    # Add the cleaned name to the new list
    cleaned_names.append(name_lowercase)

# Print the final cleaned list
print("Cleaned Names:", cleaned_names)
