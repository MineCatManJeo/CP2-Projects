# Writes to the file, required a list of all the lines

import csv
def write_file(file_loc,rf):
    with open(file_loc,'w',newline='') as file:
        print()
        fieldnames = list(rf[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames,restval=0,extrasaction='ignore',quoting=csv.QUOTE_NONNUMERIC)

        writer.writeheader()
        writer.writerows(rf)