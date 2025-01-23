# Gabriel Crozier, Personal Library

# This is useful when checking for a user input that is a number, just replace input with check_float and it will have error checking for numbers
def check_float(input_text, default = 0):
    for i in range(10):
        try:
            user_data = float(input(input_text))
            break
        except:
            print('That was not a number, please try again.\n')
    else:
        print(f'To many attempts, defaulted to {default}.')
        user_data = default
    return user_data

# loops through each item in a set and displays it with a number
def display(library):
    count = 0
    if len(library) == 0:
        print('There is nothing to display!')
    else:
        print('These are the books in your library: \n')
    for item in library:
        count += 1
        print(f'{count}. {item}')

# Combines author and book name in one string to help with sets
def add_items(library):
    book = input('What is the name of the book would you like to add? --->  ')
    author = input(f'Who is the author of {book}? --->  ')
    library.add(f'{book.title()} by {author.title()}')
    print(f'\033cYou just added {book.title()} by {author.title()}!')

# REally similar to search function
def remove_items(library):
    itemRemove = input('What book would you like to remove? (Name or author) ---> ')
    foundItems = []
    count = 0
    # Checks if your input is inside of a book in the library
    for item in library:
        if itemRemove.lower() in item.lower():
            count += 1
            foundItems.append(item)
    if count == 0: # Nothing found
        print('Couldn\'t find anything...')
    elif count == 1: # 1 thing found, seperate text to account for singularity
        print(f'The book {foundItems[0]} has been removed.')
        library.discard(foundItems[0])
    else: # prints the list, then asks user which of the located results to remove
        print('Here\'s a list of what we found.')
        for i in range(1,count+1):
            print(f'{i}. {foundItems[i-1]}')
        delete = int(check_float('Which book would you like to remove? (Number) --->  '))
        library.discard(foundItems[delete-1])
        print(f'{foundItems[delete-1]} has been removed.')

def search(library): # same as the remove function, but it doesnt remove things 0:
    itemSearch = input('What book(s) would you like to look for? (Name or author) ---> ')
    if itemSearch.strip() == 'by':
        display(library)
        return
    foundItems = []
    count = 0
    for item in library:
        if itemSearch.lower() in item.lower():
            count += 1
            foundItems.append(item)
    if count == 0:
        print('Couldn\'t find anything...')
    elif count == 1:
        print(f'The book {foundItems[0]} has been found in your library.')
    else:
        print('Here\'s a list of what we found in your library.')
        for i in range(1,count+1):
            print(f'{i}. {foundItems[i-1]}')
# Contains my UI and options menu
def main():
    welcome_text = '\033cWelcome to your personal library of books!\n\n'
    # All items are added to this set which can be converted later to help with search function
    library = set()
    while True:
        options = check_float(welcome_text + """What would you like to do?
1. Display Contents
2. Add Items
3. Remove Items
4. Search For Item
5. Exit The Program
   --->  """, 5)
        welcome_text = '\033c'
        print('\033c')
        if options == 1:
            display(library)
        elif options == 2:
            add_items(library)
        elif options == 3:
            remove_items(library)
        elif options == 4:
            search(library)
        elif options == 5:
            print('Thank you for using the library!')
            break
        else:
            print('That was not an option, please try again.')
        # This gives the user a chance to read what happened before starting another task
        input('Done Reading? ')
main()