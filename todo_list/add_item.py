# Adds an item to the list
def add_item(info,item,info1):
    if isinstance(info,list):
        info.append(item)
    else:
        print('Error: Not a list')
        
    if isinstance(info1,list):
        info1.append('[✘]. ')
    else:
        print('Error: Not a list')
    return info,info1