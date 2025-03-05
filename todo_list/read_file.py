# Reads files and returns each row as an item in a list
def read_file(location,location1):
    try:
        with open(location,newline='') as file:
            lines = file.readlines()
        with open(location1,newline='') as file:
            checks = file.readlines()
            chosen = [x[1] for x in checks if x.strip() != 'Your Check List:']
        return lines, checks, chosen
    except:
        raise FileNotFoundError("Error in reading file: File not found")