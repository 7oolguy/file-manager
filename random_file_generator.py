import os
import random
import string

def generate_random_name(length=8):
    """
    Generate a random string of fixed length consisting of letters and digits.
    
    Args:
        length (int): The length of the random string. Default is 8.
        
    Returns:
        str: A random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_files_and_folders(base_path, depth=1, max_depth=4):
    """
    Recursively create files and folders within a specified directory.
    
    Args:
        base_path (str): The path to the directory where files and folders will be created.
        depth (int): The current depth of recursion. Default is 1 (top level).
        max_depth (int): The maximum depth of recursion. Default is 4.
    """
    # If the current depth exceeds the maximum depth, stop recursion
    if depth > max_depth:
        return
    
    # Generate a random number of files and folders to create
    num_files = random.randint(2, 5)
    num_folders = random.randint(2, 5)
    
    # Create random files in the current directory
    for _ in range(num_files):
        # Generate a random file name with a random extension
        file_name = f"{generate_random_name()}.{random.choice(['txt', 'csv', 'json', 'xml', 'md'])}"
        file_path = os.path.join(base_path, file_name)
        
        # Create the file and write a sample content to it
        with open(file_path, 'w') as file:
            file.write("This is a sample file.")
    
    # Create random subfolders and populate them recursively
    for _ in range(num_folders):
        # Generate a random folder name
        folder_name = generate_random_name()
        folder_path = os.path.join(base_path, folder_name)
        
        # Create the folder if it doesn't already exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Recursively create files and folders in the newly created subfolder
        create_files_and_folders(folder_path, depth + 1, max_depth)

def create_directory_in_script_directory(new_dir_name):
    """
    Create a new directory inside the directory where the script is located
    and return the path of the newly created directory.
    
    Args:
        new_dir_name (str): The name of the new directory to create.
        
    Returns:
        str: The path of the newly created directory.
    """
    # Get the directory where the current script is located
    base_directory = os.path.dirname(__file__)
    
    # Define the path for the new directory
    new_dir_path = os.path.join(base_directory, new_dir_name)
    
    # Create the new directory if it doesn't exist
    os.makedirs(new_dir_path, exist_ok=True)
    
    # Return the path of the newly created directory
    return new_dir_path

def main(base_directory):
    """
    Create a directory structure with files and subfolders starting from the base directory.
    
    Args:
        base_directory (str): The base directory where the folder structure will be created.
    """
    # Ensure the base directory exists
    os.makedirs(base_directory, exist_ok=True)
    
    # Start the recursive creation of files and folders
    create_files_and_folders(base_directory)

# Example usage
if __name__ == "__main__":  
    # Execute the main function to create the directory structure
    main(create_directory_in_script_directory('dummy'))
