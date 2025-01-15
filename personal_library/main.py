# Gabriel Crozier, Personal Library
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

def display():
    pass

def add_items():
    pass

def remove_items():
    pass

def search():
    pass

def main():
    welcome_text = '\033cWelcome to your personal library of information!\n\n'
    library = []
    while True:
        options = check_float(welcome_text + """What would you like to do?
1. Display Contents
2. Add Items
3. Remove Items
4. Search For Item
5. Exit The Program
   --->  """, 5)
        welcome_text = '\033c'
        if options == 1:
            display()
        elif options == 2:
            add_items()
        elif options == 3:
            remove_items()
        elif options == 4:
            search()
        elif options == 5:
            print('Thank you for using the library!')
            break
        else:
            print('That was not an option, please try again.')

main()