# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer

from read_file import read_file as read
from write_file import write_file as write
from select_char_menu import select_char_menu as sel_menu
from display_char import display_char as dc

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
            if rf == 'exit':
                break
        
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "select",
                "create",
                "skill",
                "battle",
                "display",
                "exit"
            ]
        ).execute()
        if action == 'display':
            dc(rf,selected_character)
            begin_message = 'Guh'
        elif action == 'exit':
            break
            
        write('battle_simulator/storage_csvs/characters.csv',rf)
    print('\033cThank you for using my program!')



main()