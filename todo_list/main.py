# Gabriel Crozier, To-Do list main file
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from create_list import create_list
from read_file import read_file
from delete_list import delete_list
from display_list import display
from write_file import write_file
from add_item import add_item
from delete_item import delete_item

def main():
    list_loc = "todo_list/todo_list.txt"
    list_loc1 = "todo_list/todo_checks.txt"
    create_list(list_loc,list_loc1) # Creates list if no list is there
    while True:
        #print('\033c')
        to_do, to_do_dict = read_file(list_loc,list_loc1) # to_do dict extrmely unstalbe attmepeted to finish marks in like 15 minutes, bad idea (I should kill mysefl)
        display(to_do)
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
            filter=lambda result:result.split()[0].lower()
        ).execute()

        if action == 'add':
            add_item(to_do,
                    inquirer.text(
                        message="What would you like to add to your to-do list?",
                        validate=lambda result:all(res.isalpha() or res.isspace() or res in "',()" for res in result),
                        invalid_message="Invalid characters found in string",
                        filter=lambda result:result.title(),
                ).execute(), to_do_dict)
            
        elif action == 'mark':
            inquirer.checkbox(
                message="What would you like to mark off?",
                choices=[Choice(value=x,name=x.strip()) for x in to_do[1:]],
            ).execute()
        elif action == 'delete':
            delete_item(to_do,
                        inquirer.fuzzy(
                            message="Choose an item to delete",
                            choices=[Choice(value=x,name=x.strip()) for x in to_do[1:]],
                        ).execute(), to_do_dict)
            
        elif action == 'restart':
            delete_list(list_loc)
            to_do = ["Your To-Do List:"]

        elif action == 'exit':
            break
        write_file(list_loc,to_do)
    print('\033cThank you for using my program!')



main()