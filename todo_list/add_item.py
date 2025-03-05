# Adds an item to the list
def add_item(info,info1,item):
    if item:
        if isinstance(info,list):
            info.append(item)
        else:
            raise TypeError('Error: Not a list')
            
        if isinstance(info1,list):
            info1.append('[ ]. ')
        else:
            raise TypeError('Error: Not a list')
    return info,info1