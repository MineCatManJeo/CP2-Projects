# Deletes everything inside the list if user wants to do that
def delete_list(location):
    with open(location,'w',newline='') as file:
        file.write('')