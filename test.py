import filef

if __name__ == '__main__':
    path = r"C:\Users\yan.silva\OneDrive - Adventistas\Documentos\Projectos\Organizer\dummy"
    
    items = filef.get_items_list(path)
    print(items)
    items = filef.get_file_by_type(path, file_type=['txt','md'])
    print(items)
    items = filef.find_file(path, "hello.txt")
    print(items)
    