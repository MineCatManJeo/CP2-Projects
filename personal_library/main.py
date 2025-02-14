# Gabriel Crozier, Personal Library

def sort_key(book):
    return(book['book'])



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



# loops through each item in a list and displays it with a number
def display(library):
    # Sorts the library based alphebetically on the book title
    library.sort(key=sort_key)


    if len(library) == 0:
        print('There is nothing to display!')
        return

    # Lets user choose between a simple display or a more complicated display
    while True:
        option = input('Would you like to have minimum display or maximum display? (min, max) --->  ').lower()
        if option in ['min','max']:
            break
        print(f'\033c| {option} | is not a valid option! Please try again: ')

    count = 0
    print('These are the books in your library: \n')
    
    # Loops through the library and displays it correlating with a number.
    for item in library:
        count += 1
        if option == 'min':
            print(f"{count}. {item['book']} by {item['author']}")
        if option == 'max':
            print(f"{count}. {item['book']} by {item['author']}, {item['pages']} pages, Made in {item['year']}")



# Combines author and book name in one string to help with sets
def add_items(library):
    book = input('What is the name of the book would you like to add? --->  ')
    author = input(f'Who is the author of {book}? --->  ')
    pages = input(f'How many pages are in {book}? --->  ')
    year = input(f'When was {book} made? --->  ')

    library.append({'book':book.title(), 'author':author.title(), 'pages':pages, 'year':year})
    print(f'\033cYou just added {book.title()} by {author.title()}!')



# Removes a book
def remove_items(library):
    book = search(library)
    if book == False:
        return
    else:
        library.remove(book)
        print(f"\033c{book['book']} by {book['author']} has been removed.")

    

def search(library,select_book=True): # searches for an item and returns a list of valid items or just one item
    itemSearch = input('What book would you like to look for? (Name or Author) ---> ')
    foundItems = []
    count = 0
    # Checks if your input is inside of a book in the library
    for item in library:
        if itemSearch.lower() in ''.join(list(item.values())).lower():
            count += 1
            foundItems.append(item)

    if count == 0: # Displays if nothing was found in library
        print('Couldn\'t find anything...')
        return False

    elif count == 1: # Displays the item
        print(f"The book {foundItems[0]['book']} by {foundItems[0]['author']} has been found in your library.")
        return foundItems[0]

    else: # Displays the itemS
        print('Here\'s a list of what we found in your library.')
        for i in range(1,count+1):
            print(f"{i}. {foundItems[i-1]['book']} by {foundItems[i-1]['author']}")
        if select_book:
            while True:
                select = int(check_float('Which book would you like to select? (Number) --->  '))
                if select > len(foundItems):
                    print('That was too large of a number, please try again.')
                    continue
                break
            return foundItems[select-1]


def change(library):
    book = search(library)
    if book == False:
        return
    else:
        while True:
            book_change_type = input('What would you like to change? (book, author, pages, year) --->  ').lower()
            if book_change_type in ['book','author','pages','year']:
                break
            else:
                print(f'\033c| {book_change_type} | is not a valid option.')
        
        book_change = input(f'What would you like to change the {book_change_type} to? (Origionally: {book[book_change_type]}) --->  ')
        library.remove(book)
        book[book_change_type] = book_change
        library.append(book)

                

# Contains my UI and options menu
def main():
    welcome_text = '\033cWelcome to your personal library of books!\n\n'
    # All items are added to this set which can be converted later to help with search function
    library = []
    while True:
        options = check_float(welcome_text + """What would you like to do?
1. Display Contents
2. Add a Book
3. Remove a Book
4. Search For a Book
5. Change Book Information
6. Exit The Program
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
            search(library,False)
        elif options == 5:
            change(library)
        elif options == 6:
            print('Thank you for using the library!')
            break
        else:
            print('That was not an option, please try again.')
        # This gives the user a chance to read what happened before starting another task
        input('Done Reading? ')
main()