# Gabriel Crozier, To-Do list main file


# ------- IMPORTANT -------
#
#
# Make sure you have the InquirerPy module installed with pip3!!! If you cant figure it out for whatever reason then go to:
# -----------------------   https://inquirerpy.readthedocs.io/en/latest/index.html#install   ------------------------------
#
#
# ------- IMPORTANT -------

# Import all my functions!!!
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from create_list import create_list
from read_file import read_file
from check_to_bool import check_to_bool
from display_list import display
from write_file import write_file
from add_item import add_item
from delete_item import delete_item
from mark_item import mark_item

def main():
    # Defines the location of the lists
    list_loc = "todo_list/todo_list.txt" # Stores the name of your task
    list_loc1 = "todo_list/todo_checks.txt" # Stores the info that says your task is complete

    create_list(list_loc,list_loc1) # Creates list if no list is there

    while True:
        print('\033c') # Clears terminal at the beggining
        to_do_list, to_do_check, chosen = read_file(list_loc,list_loc1) # Reads the file and returns the list, checks, and if your task is complete "X" " "
        
        display(to_do_list,to_do_check) # Displays to-do list

        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                'Add an Item to Do',
                'Mark an Item as Complete',
                'Delete an Item',
                'Restart the List',
                'Exit Program',
                ],
            default='Exit Program',
            instruction='Select an option [Up/Down Arrow] + [Enter]',
            filter=lambda result:result.split()[0].lower() # Grabs the first word in the sentence for easy action ifs
        ).execute()

        if action == 'add':
            add_item(to_do_list, to_do_check,
                    inquirer.text(
                        message="What would you like to add to your to-do list?",
                        validate=lambda result:all(res.isalpha() or res.isspace() or res in "',()!?." for res in result) and result,
                        invalid_message="Invalid characters found in string",
                        filter=lambda result:result.title(),
                ).execute())
            
        elif action == 'mark':
            mark_item(to_do_list,to_do_check,
                inquirer.checkbox(
                    message="What would you like to mark off?",
                    # Gives you each of the tasks, then checks if task is checked and uses check_to_bool to do so, LIST COMPREHENSION IS COOL
                    choices=[Choice(x.strip(),enabled=check_to_bool(chosen[to_do_list.index(x)-1])) for x in to_do_list[1:]],
                    instruction="Press [Space] to select, and [Enter] to finalize selction",
                ).execute())
            
        elif action == 'delete':
            delete_item(to_do_list, to_do_check,
                        inquirer.fuzzy(
                            message="Choose an item to delete",
                            # Same thing as in mark, but it doesn't have a check box
                            choices=[Choice(value=x, name=x.strip()) for x in to_do_list[1:]],
                            validate=lambda result:result in to_do_list and result != "Your To-Do List:",
                        ).execute())
            
        elif action == 'restart': # Resets the list, deletes all items
            to_do_list = ["Your To-Do List:"]
            to_do_check = ["Your Check List:"]

        elif action == 'exit':
            break

        write_file(list_loc,to_do_list,list_loc1,to_do_check) # Writes the whole file again with the to_do variables

    print('\033cThank you for using my program!')



main()