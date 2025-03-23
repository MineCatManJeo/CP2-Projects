# Reads the character file, returns all of it as a list, selections for specifics
# Just return the whole file, specifics will be gathered later

import csv

def read_file(file_loc):
    with open(file_loc,'r',newline='') as file:
        reader = csv.DictReader(file, restval=0, quoting=csv.QUOTE_NONNUMERIC)
        file_read = [row for row in reader]
    return file_read