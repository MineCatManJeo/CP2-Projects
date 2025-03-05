# This displays the to do list for the user to see
def display(info, info1):
    lines = [x.strip() for x in info]
    if len(lines) == 1:
        lines.append('---Nothing in to-do list')
        print('\n'.join(lines)+'\n')
        return
    check = [x.strip() for x in info1]
    lines = [f"{check[lines.index(x)]} {x}" for x in lines if x.strip() != "Your To-Do List:"]
    lines.insert(0,"Your To-Do List:")
    print('\n'.join(lines)+'\n')