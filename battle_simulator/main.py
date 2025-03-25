# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer

from read_file import read_file as read
from write_file import write_file as write
from select_char_menu import select_char_menu as sel_menu
from select_char import select_char as sc
from create_char import create_char as cc
from skill_point import skills

def main():
    print('\033c')

    # Setup
    attributes = ['Health','Strength','Defence','Speed']
    rf = read('battle_simulator/storage_csvs/characters.csv')
    selected_character = False
    spend_points = ""

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
        if not selected_character:
            print('\033c')
            selected_character, rf = sel_menu(rf,attributes)

        if selected_character[0]['points'] > 0:
            spend_points = f"You Have [{selected_character[0]['points']}] Unspent Skill Point{'s' if selected_character[0]['points'] > 1 else ""}!\n"
            
        print(f"\033cSelected Character: {selected_character[0]['name']}, lvl [{selected_character[0]['level']}]" + f"\n{spend_points}")
        spend_points = ""

        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "Select / Create a New Character",
                "Spend Skill Points",
                "Battle Enemies",
                "Exit the Program"
            ],
            filter=lambda result: result.split()[0].lower(),
            border=True
        ).execute()

        print('\033c')
        if action == 'select':
            selected_character, rf = sel_menu(rf,attributes)
        elif action == 'spend':
            selected_character[0] = skills(selected_character[0],attributes)
            rf[selected_character[1]] = selected_character[0]
        elif action == 'exit':
            break
            
        write('battle_simulator/storage_csvs/characters.csv',rf)
        #inquirer.text(message="Press [Enter] to Continue").execute()
    print('\033cThank you for using my program!')



main()