# Mark an item on the list as complete / uncomplete
def mark_item(info,info1,items):
    # Grabs the correct indexes for items in to-do list that match the items selected
    indexes = [info.index(x)-1 for x in info if x.strip() in items]
    
    for i in range(len(info1[1:])):
        info_list_string = list(info1[i+1]) # Turns the string into a list for better manipulation

        if i in indexes: # If the current value of i is in the indexes, the user has selected that item so it needs to be "X"
            info_list_string[1] = "X"
        else:
            info_list_string[1] = " "
        info1[i+1] = ''.join(info_list_string) # Restringifies the list with possible modifications
    return info1