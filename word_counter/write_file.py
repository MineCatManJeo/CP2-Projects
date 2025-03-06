# Rewrite to to file with the word count Added / Changed
def write_file(file_location,rows):
    with open(file_location,'w',newline='') as file:
        file.writelines(rows)