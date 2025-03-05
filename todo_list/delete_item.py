# Deletes an item from the list
def delete_item(info,info1,item):
    if isinstance(info,list):
        info1.pop(info.index(item))
    else:
        print('Error: Not a list')

    if isinstance(info,list):
        info.remove(item)
    else:
        print('Error: Not a list')

    return info