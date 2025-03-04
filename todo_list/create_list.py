# If the list isn't there, create a list
def create_list(location,location1):
    try:
        with open(location,'r',newline='') as file:
            read_line = file.readline().strip()
        if read_line != "Your To-Do List:":
            with open(location,'w',newline='') as file:
                file.write("Your To-Do List:")
    except:
        with open(location,'x',newline='') as file:
            file.write("Your To-Do List:")
    try:
        with open(location1,'r',newline='') as file:
            read_line = file.readline().strip()
        if read_line != "Your Check List:":
            with open(location1,'w',newline='') as file:
                file.write("Your Check List:")
    except:
        with open(location1,'x',newline='') as file:
            file.write("Your Check List:")