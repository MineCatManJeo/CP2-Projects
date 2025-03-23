# The menu for character selections, ui for selecting, create, or select, character

from InquirerPy import inquirer

from create_char import create_char as cc
from select_char import select_char as sc

def select_char_menu(rf,attrib):
    if len(rf) == 0:
        print('There are no characters made, you can make one now!')
        action = 'create'
    else:
        action = inquirer.select(
            message = "What would you like to do?",
            instruction="Press enter to select",
            choices=[
                "Create New Character",
                "Select Previously Made Character",
                "Exit The Program",
            ],
            filter=lambda x:x.split()[0].lower(),
        ).execute()
    if action == 'create':
        character = cc(attrib)
        rf.append(character)
        selected_character = character['name']
    elif action == 'select':
        selected_character = sc(rf)
    else:
        return "exit", "exit"
    return selected_character, rf