# Read the file and return it as a list with each new line being an item in a list
def read_file(file_location):
    try:
        with open(file_location,'r',newline='') as file:
            rows = file.readlines()
            return rows
    except:
        print('Error: File not found') # Reads the file and if it's not found return an error (Shouldn't actually happen)
        return False
