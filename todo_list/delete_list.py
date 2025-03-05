# Deletes everything inside the list if user wants to do that
def delete_list(location,location1):
    with open(location,'w',newline='') as file:
        file.write('')
    with open(location1,'w',newline='') as file:
        file.write('')