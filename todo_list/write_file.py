# Rewrites list to file (with modifications)
def write_file(location,info,location1,info1):
    with open(location,'w',newline='') as file:
        file.writelines([x.strip() + '\n' for x in info if x != '\n'])
    with open(location1,'w',newline='') as file:
        file.writelines([x.strip() + '\n' for x in info1 if x != '\n'])