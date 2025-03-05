# Mark an item on the list as complete / uncomplete
def mark_item(info,info1,items):
    print(info)
    print(info1)
    print(items)
    indexes = [info.index(x)-1 for x in info if x.strip() in items]
    for i in range(len(info1[1:])):
        info_list_string = list(info1[i+1])
        if i in indexes:
            info_list_string[1] = "X"
        else:
            info_list_string[1] = " "
        info1[i+1] = ''.join(info_list_string)
    return info1