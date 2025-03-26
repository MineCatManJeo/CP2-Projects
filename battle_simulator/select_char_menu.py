# The menu for character selections, ui for selecting, create, or select, character

from InquirerPy import inquirer

from create_char import create_char as cc
from select_char import select_char as sc

def select_char_menu(rf,attrib):
    begin_message = ''
    if len(rf) == 0: # If the amount of characters is 0 make a new character
        begin_message = 'There are no characters made, you can make one now!'
        action = 'create'

    else:
        action = inquirer.select(
            message = "What would you like to do?",
            instruction="Press enter to select",
            choices=[
                "Create New Character",
                "Select Previously Made Character",
            ],
            filter=lambda x:x.split()[0].lower(),
        ).execute()

    if action == 'create':
        print(f'\033c{begin_message}') # Begin message only includes the "There are no characters made, you can make one now"
        selected_character = cc(attrib) # Create character

        rf.append(selected_character[0]) # append rf for write later
        selected_character.append(len(rf)-1) # Appends the index of selected character for easy use later

    elif action == 'select':
        selected_character = sc(rf) # Select previously made character
    return selected_character, rf