import os
from fandf import items

def find_items(root_dir, target_substring):
    """
    Find all files and folders within root_dir and its subdirectories that contain target_substring in their names.
    :param root_dir: str - The root directory to start the search
    :param target_substring: str - The substring to search for in filenames and folder names
    :return: list - A list of objects (File or Folder instances) containing the target substring
    """
    def recursive_search(current_path):
        results = []
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            # Check if the target substring is in the item name
            if target_substring.lower() in item.lower():
                # Convert item path to its corresponding File or Folder class instance
                items_list = items.convert_items_to_class([item_path])
                results.extend(items_list)  # Extend results with the converted items
            # If it's a directory, recursively search inside it
            elif os.path.isdir(item_path):
                results.extend(recursive_search(item_path))
        return results

    return recursive_search(root_dir)

def convert_to_dict(item_list):
    """
    Convert a list of objects to a list of dictionaries.
    :param item_list: list - List of File or Folder instances
    :return: list - List of dictionaries representing the items
    """
    return [obj.get_info() for obj in item_list]
    
if __name__ == "__main__":
    search_results = find_items(r"C:\Users\yan.silva\OneDrive - Adventistas", "dum")
    dict_list = convert_to_dict(search_results)
    
    for item in dict_list:
        print(f"{item['item_type']} -> {item['name']}")
        
                            