# Reads the character file, returns all of it as a list, selections for specifics
# Just return the whole file, specifics will be gathered later

import csv

def convert_float(dicti):
    for key in dicti.keys():
        try:
            dicti[key] = int(dicti[key])
        except:
            pass
    return dicti

def read_file(file_loc):
    with open(file_loc,'r',newline='') as file:
        reader = csv.DictReader(file, restval=0, quoting=csv.QUOTE_NONNUMERIC)
        file_read = [convert_float(row) for row in reader]
    return file_read