# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer

from read_file import read_file as read
from write_file import write_file as write
from select_char_menu import select_char_menu as sel_menu
from display_char import display_char as dc
from select_char import select_char as sc
from create_char import create_char as cc
from skill_point import skills

def main():
    print('\033c')

    # Setup
    attributes = ['Health','Strength','Defence','Speed']
    rf = read('battle_simulator/storage_csvs/characters.csv')
    selected_character = False
    begin_message = ""

    # User character selection
    ## User creates character
    ### Name, blah blah, uses skill point function
    ## User selects previosly made character
    ## Variable used that is just the created / selected character

    # menu for options to do with character
    ## Select New Character
    ## Delete Character
    ## Add Skill points
    ## Battle NPC / Possible other character (optional)
    ## Check level, attributes, ect
    ## Exit Program

    # Variables:
    # The whole list
    # Names of each character in list maybe not, because we have everycharacter already
    #### Once char is selected, specificly the character is a var

    while True:
        print('\033c'+begin_message)

        if not selected_character:
            selected_character, rf = sel_menu(rf,attributes)
        
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "selcre",
                "skill",
                "battle",
                "display",
                "exit"
            ]
        ).execute()
        print('\033c')
        if action == 'selcre':
            selected_character, rf = sel_menu(rf,attributes)
        elif action == 'skill':
            selected_character[0] = skills(selected_character[0],attributes)
            rf[selected_character[1]] = selected_character[0]
        elif action == 'display':
            dc(rf,selected_character[0])
        elif action == 'exit':
            break
            
        write('battle_simulator/storage_csvs/characters.csv',rf)
        inquirer.text(message="Press [Enter] to Continue").execute()
    print('\033cThank you for using my program!')



main()