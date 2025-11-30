import os

# Get the directory where this file (FileService.py) is located
current_folder = os.path.dirname(file)

# The data folder is inside the current folder
data_folder = os.path.join(current_folder, "data")

def save_data(filename, data_list):
    # Create the full path to the file
    file_path = os.path.join(data_folder, filename)
    
    try:
        # Open the file in 'write' mode
        file = open(file_path, "w")
        
        # Write each item in the list to the file
        for line in data_list:
            file.write(line + "\n")
            
        # Close the file to save changes
        file.close()
        
    except Exception as error:
        print("Error saving file: " + str(error))

def load_data(filename):
    # Create the full path to the file
    file_path = os.path.join(data_folder, filename)
    
    # Check if the file exists before trying to open it
    if not os.path.exists(file_path):
        return []

    try:
        # Open the file in 'read' mode
        file = open(file_path, "r")
        
        # Read all lines from the file
        all_lines = file.readlines()
        
        # Close the file
        file.close()
        
        # Create a new list to hold the clean lines (without newlines)
        clean_lines = []
        for line in all_lines:
            # strip() removes the newline character at the end
            clean_lines.append(line.strip())
            
        return clean_lines
        
    except Exception as error:
        print("Error reading file: " + str(error))
        return []