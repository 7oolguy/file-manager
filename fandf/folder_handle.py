import os
import shutil

class Folder:
    def __init__(self, name, path, created, modified):
        self.name = name
        self.path = path
        self.created = created
        self.modified = modified
        self.contents = []  # Initialize this separately if needed
        self.item_type = "Folder"

    # Methods
    def rename(self, new_name):
        """
        Rename the folder.
        :param new_name: str
        """
        new_path = os.path.join(os.path.dirname(self.path), new_name)
        try:
            os.rename(self.path, new_path)
            self.name = new_name
            self.path = new_path
            print(f"Folder renamed to {new_name}")
        except FileNotFoundError:
            print(f"Error: The folder {self.path} does not exist.")
        except FileExistsError:
            print(f"Error: A folder with the name {new_name} already exists.")
        except PermissionError:
            print(f"Error: Permission denied to rename the folder.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to rename the folder

    def move(self, new_path):
        """
        Move the folder to a new location.
        :param new_path: str
        """
        try:
            # Ensure the new path is a directory
            if not os.path.isdir(new_path):
                raise NotADirectoryError(f"The path {new_path} is not a directory.")
            
            # Construct the new folder path
            new_folder_path = os.path.join(new_path, self.name)
            
            # Move the folder
            os.rename(self.path, new_folder_path)
            self.path = new_folder_path
            print(f"Folder moved to {new_folder_path}")
        except FileNotFoundError:
            print(f"Error: The folder {self.path} does not exist.")
        except NotADirectoryError as e:
            print(e)
        except PermissionError:
            print(f"Error: Permission denied to move the folder.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to move the folder

    def copy(self, destination_path):
        """
        Copy the folder to a new location.
        :param destination_path: str
        """
        try:
            # Ensure the destination path is a directory
            if not os.path.isdir(destination_path):
                raise NotADirectoryError(f"The path {destination_path} is not a directory.")
            
            # Construct the new folder path
            destination_folder_path = os.path.join(destination_path, self.name)
            
            # Copy the folder
            shutil.copytree(self.path, destination_folder_path)
            print(f"Folder copied to {destination_folder_path}")
        except FileNotFoundError:
            print(f"Error: The folder {self.path} does not exist.")
        except NotADirectoryError as e:
            print(e)
        except PermissionError:
            print(f"Error: Permission denied to copy the folder.")
        except shutil.Error as e:
            print(f"Error occurred while copying folder: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to copy the folder

    def delete(self):
        """
        Delete the folder.
        """
        try:
            if os.path.exists(self.path):
                shutil.rmtree(self.path)
                print(f"Folder {self.path} deleted.")
            else:
                print(f"Error: The folder {self.path} does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to delete the folder.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to delete the folder

    def add_item(self, item):
        """
        Add a file or subfolder to the folder.
        :param item: File or Folder
        """
        if item not in self.contents:
            self.contents.append(item)
        else:
            print(f"Item {item} is already in the folder.")

    def remove_item(self, item_name):
        """
        Remove a file or subfolder from the folder by name.
        :param item_name: str
        """
        if item_name in self.contents:
            self.contents.remove(item_name)
        else:
            print(f"Item {item_name} is not found in the folder.")
        # Logic to remove the item from the folder

    def list_contents(self):
        """
        List all contents of the folder.
        :return: list
        """
        try:
            self.contents = os.listdir(self.path)
            return self.contents
        except FileNotFoundError:
            print(f"Error: The folder {self.path} does not exist.")
            return []
        except PermissionError:
            print(f"Error: Permission denied to access the folder contents.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def get_info(self):
        """
        Get folder information.
        :return: dict
        """
        return {
            'name': self.name,
            'path': self.path,
            'created': self.created,
            'modified': self.modified,
            'contents': [item.get_info() for item in self.contents],  # Assumes contained items have a get_info method
            'item_type': self.item_type
        }

    def exists(self):
        """
        Check if the folder exists.
        :return: bool
        """
        return os.path.isdir(self.path)
        # Logic to check if the folder exists

    def search(self, keyword):
        """
        Search for files and subfolders within the folder that match the keyword.
        :param keyword: str
        :return: list
        """
        results = []
        for item in self.contents:
            if keyword.lower() in item.name.lower():
                results.append(item)
            if isinstance(item, Folder):
                results.extend(item.search(keyword))
        return results

    def sort_contents(self, by='name'):
        """
        Sort the folder's contents.
        :param by: str ('name', 'size', 'created', 'modified')
        """
        valid_criteria = ['name', 'size', 'created', 'modified']
        if by not in valid_criteria:
            raise ValueError(f"Invalid sorting criteria. Choose from {valid_criteria}.")

        if by == 'name':
            self.contents.sort(key=lambda item: item.name)
        elif by == 'size':
            self.contents.sort(key=lambda item: item.size)
        elif by == 'created':
            self.contents.sort(key=lambda item: item.created)
        elif by == 'modified':
            self.contents.sort(key=lambda item: item.modified)

        print(f"Contents sorted by {by}")
    
    def list_all_files(self):
        """
        List all files in the folder (recursively).
        :return: list - List of file paths
        """
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def list_all_folders(self):
        """
        List all subfolders in the folder (recursively).
        :return: list - List of folder paths
        """
        folder_list = []
        for root, dirs, files in os.walk(self.path):
            for directory in dirs:
                folder_list.append(os.path.join(root, directory))
        return folder_list