import os
import shutil

class File:
    def __init__(self, name, path, size, created, modified, file_type):
        # Attributes
        self.name = name            # Name of the file
        self.path = path            # Path to the file
        self.size = size            # Size of the file in bytes
        self.created = created      # Creation timestamp
        self.modified = modified    # Last modified timestamp
        self.file_type = file_type  # Type of the file (e.g., 'txt', 'jpg')
        self.item_type = "File"
    
    # Methods
    def rename(self, new_name):
        """
        Rename the file.
        :param new_name: str
        """
        new_path = os.path.join(os.path.dirname(self.path), new_name)
        try:
            os.rename(self.path, new_path)
            self.name = new_name
            self.path = new_path
            print(f"File renamed to {new_name}")
        except FileNotFoundError:
            print(f"Error: the files {self.path} does not exists.")
        except FileExistsError:
            print(f"Error: A file with the name {new_name} already exists.")
        except PermissionError:
            print(f"Error: Permission denied to rename the file.")
        except Exception as e:
            print(f"An unexpected error ocurred: {e}")
        # Logic to rename the file

    def move(self, new_path):
        """
        Move the file to a new location.
        :param new_path: str
        """
        new_file_path = os.path.join(new_path, self.name)
        try:
            if not os.path.isdir(new_path):
                raise NotADirectoryError(f"The path {new_path} is not a directory.")
            os.rename(self.path, new_file_path)
            self.path = new_file_path
            print(f"File moved to {new_file_path}")
        except FileNotFoundError:
            print(f"Error: the file {self.path} does not exists.")
        except NotADirectoryError as e:
            print(e)
        except PermissionError:
            print(f"Error: Permission denied to move the file.")
        except Exception as e:
            print(f"An unexpected error ocurred: {e}")
        # Logic to move the file

    def copy(self, destination_path):
        """
        Copy the file to a new location.
        :param destination_path: str
        """
        destination_file_path = os.path.join(destination_path, self.name)
        try:
            if not os.path.isdir(destination_path):
                raise NotADirectoryError(f"The path {destination_path} is not a directory.")
            
            shutil.copy2(self.path, destination_file_path)  # copy2 preserves metadata
            print(f"File copied to {destination_file_path}")
        except FileNotFoundError:
            print(f"Error: The file {self.path} does not exist.")
        except NotADirectoryError as e:
            print(e)
        except PermissionError:
            print(f"Error: Permission denied to copy the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to copy the file

    def delete(self):
        """
        Delete the file.
        """
        try:
            os.remove(self.path)
            print(f"File {self.path} deleted.")
        except FileNotFoundError:
            print(f"Error: The file {self.path} does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to delete the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to delete the file

    def read(self):
        """
        Read the file's contents.
        :return: str
        """
        try:
            with open(self.path, 'r') as file:
                contents = file.read()
            return contents
        except FileNotFoundError:
            print(f"Error: The file {self.path} does not exist.")
            return None
        except PermissionError:
            print(f"Error: Permission denied to read the file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        # Logic to read the file

    def write(self, content):
        """
        Write content to the file.
        :param content: str
        """
        try:
            with open(self.path, 'w') as file:
                file.write(content)
            print(f"Content written to {self.path}")
        except PermissionError:
            print(f"Error: Permission denied to write to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # Logic to write content to the file

    def get_info(self):
        """
        Get file information.
        :return: dict
        """
        return {
            'name': self.name,
            'path': self.path,
            'size': self.size,
            'created': self.created,
            'modified': self.modified,
            'file_type': self.file_type,
            'item_type': self.item_type
        }

    def exists(self):
        """
        Check if the file exists.
        :return: bool
        """
        return os.path.exists(self.path)
        # Logic to check if the file exists
        