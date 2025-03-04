# Reads files and returns each row as an item in a list
def read_file(location,location1):
    try:
        with open(location,newline='') as file:
            lines = file.readlines()
            return lines, {}
        with open(location1,newline='') as file:
            checks = file.readlines()
        return lines, checks
    except:
        raise FileNotFoundError("Error in reading file: File not found")