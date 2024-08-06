import os
import datetime
from fandf.file_handle import File
from fandf.folder_handle import Folder

def get_file_attributes(file_path):
    """
    Get attributes of a file.
    :param file_path: str - Path to the file
    :return: dict - Dictionary containing file attributes
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)  # Correct way to get file size
    file_stat = os.stat(file_path)
    
    # Get creation and modification timestamps
    try:
        creation_time = datetime.datetime.fromtimestamp(file_stat.st_birthtime)
    except AttributeError:
        creation_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
    
    modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)
    
    # Get file type
    file_extension = os.path.splitext(file_path)[1][1:]  # Extract extension and remove leading dot
    
    return {
        'name': file_name,
        'path': file_path,
        'size': file_size,
        'created': creation_time,
        'modified': modified_time,
        'file_type': file_extension
    }

def get_folder_attributes(folder_path):
    """
    Get attributes of a folder.
    :param folder_path: str - Path to the folder
    :return: dict - Dictionary containing folder attributes and contents
    """
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"The folder {folder_path} does not exist.")
    
    folder_name = os.path.basename(folder_path)
    folder_stat = os.stat(folder_path)
    
    # Get creation and modification timestamps
    try:
        creation_time = datetime.datetime.fromtimestamp(folder_stat.st_birthtime)
    except AttributeError:
        creation_time = datetime.datetime.fromtimestamp(folder_stat.st_ctime)
    
    modified_time = datetime.datetime.fromtimestamp(folder_stat.st_mtime)
    
    # List contents (files and subfolders)
    contents = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            contents.append({'type': 'file', 'name': item, 'path': item_path})
        elif os.path.isdir(item_path):
            contents.append({'type': 'folder', 'name': item, 'path': item_path})
    
    return {
        'name': folder_name,
        'path': folder_path,
        'created': creation_time,
        'modified': modified_time,
    }, contents

def convert_items_to_class(items=[]):
    """
    Convert file and folder paths to their respective class instances.
    :param items: list - List of file and folder paths
    :return: list - List of File and Folder class instances
    """
    objects = []
    for item in items:
        if os.path.isfile(item):
            file_att = get_file_attributes(item)
            file = File(**file_att)
            objects.append(file)
        elif os.path.isdir(item):
            folder_att, contents = get_folder_attributes(item)
            folder = Folder(**folder_att)
            
            # Process contents to create File or Folder instances
            folder_contents = []
            for content in contents:
                if content['type'] == 'file':
                    file_att = get_file_attributes(content['path'])
                    folder_contents.append(File(**file_att))
                elif content['type'] == 'folder':
                    # Recursively process subfolders
                    subfolder_items = convert_items_to_class([content['path']])
                    folder_contents.append(subfolder_items[0])  # Assuming there's only one subfolder at this level
            
            # Assign contents to folder
            folder.contents = folder_contents
            objects.append(folder)
    
    return objects
