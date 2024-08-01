import os

def get_items_list(path, return_type='all'):
    files = []
    folders = []
    
    #List all items in directory    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        if os.path.isfile(full_path):
            files.append(item)
        elif os.path.isdir(full_path):
            folders.append(item)
    
    if return_type == 'files':
        return files
    elif return_type == 'folders':
        return folders
    elif return_type == 'all':
        return files, folders
    else:
        raise ValueError("Váriavel return_type inválida. Escolha entre 'all', 'files', ou 'folders'")

def get_file_type(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension[1:] if file_extension else ''

def get_file_by_type(path, file_type=['csv', 'xml']):
    
    files = get_items_list(path, return_type='files')
    files_filtered = []
    for item in files:
        ext = get_file_type(item)
        if ext in file_type:
            files_filtered.append(item)
    return files_filtered

def find_items(root_dir, target_substring):
    def recursive_search(current_path):
        results = []
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            # Check if the target substring is in the item name
            if target_substring in item:
                results.append(item_path)
            # If it's a directory, recursively search inside it
            elif os.path.isdir(item_path):
                results.extend(recursive_search(item_path))
        return results

    return recursive_search(root_dir)