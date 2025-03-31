# Prints out the answer in a readable format
def print_answer(solved,names,values):
    print('\033c')
    print(f"Starting Amount: {sum(solved)}")

    # Creates a dictionary that has the key as each unique value in the solution, and the value as the amount of them
    counts = {x:solved.count(x) for x in list(dict.fromkeys(solved))}

    for key in counts:
        print(f"You need {counts[key]}, {names[values.index(key)]},") # Prints them, names aren't very cool, but i found it hard to find the names and dont want to change everything
