# Rewrites list to file (with modifications)
def write_file(location,info):
    with open(location,'w',newline='') as file:
        file.writelines([x.strip() + '\n' for x in info if x != '\n'])