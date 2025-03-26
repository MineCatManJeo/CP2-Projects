# Reads the character file, returns all of it as a list, selections for specifics
# Just return the whole file, specifics will be gathered later

import csv

def convert_float(dicti): # Converts the floats that the QUOTE_NUMERIC gives me into ints for easy use
    for key in dicti.keys():
        try:
            dicti[key] = int(dicti[key]) # Sets he num to its int
        except:
            pass
    return dicti

def read_file(file_loc):
    with open(file_loc,'r',newline='') as file:
        reader = csv.DictReader(file, restval=0, quoting=csv.QUOTE_NONNUMERIC)
        file_read = [convert_float(row) for row in reader] # Goes through each line (Not the field stuff) and adds it to a list (as a dicitonary)
    return file_read