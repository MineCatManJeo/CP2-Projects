# Reads the character file, returns all of it as a list, selections for specifics
# Just return the whole file, specifics will be gathered later

import csv

def read_file(file_loc):
    with open(file_loc,'r') as file:
        reader = csv.DictReader(file)
        file_read = [row for row in reader]
    return file_read
