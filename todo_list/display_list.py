# This displays the to do list for the user to see
def display(info):
    info = [x.strip() for x in info]
    if len(info) == 1:
        info.append('---Nothing in to-do list')
    print('\n'.join(info)+'\n')