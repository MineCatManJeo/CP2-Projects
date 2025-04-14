# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer # InquirerPy library

from read_file import read_file as read
from write_file import write_file as write
from select_char_menu import select_char_menu as sel_menu
from skill_point import skills
from battle import battle_set_up as bst

def main():
    print('\033c')

    # Setup
    attributes = ['Health','Strength','Defence','Speed']
    rf = read('battle_simulator/storage_csvs/characters.csv')
    print(rf)
    input("guh")
    rf_enemy = read('battle_simulator/storage_csvs/enemies.csv')

    selected_character = False
    spend_points = "" # Create variable for if you need to spend poiunts or not, setup

    
    # Main Loop
    while True:

        # Checks if selected character is in play or not
        if not selected_character:
            print('\033c')
            selected_character, rf = sel_menu(rf,attributes)

        # USER DETAILS GIVEN AT TOP OF SCREEN
        if selected_character[0]['points'] > 0:
            spend_points = f"You Have [{selected_character[0]['points']}] Unspent Skill Point{'s' if selected_character[0]['points'] > 1 else ""}!\n"
            
        print(f"\033cSelected Character: {selected_character[0]['name']}, lvl [{selected_character[0]['level']}], xp: [{selected_character[0]['xp']}]\n\
{((selected_character[0]['level']+1)*50)-selected_character[0]['xp']} XP Needed to Level Up" + f"\n{spend_points}")
        spend_points = ""


        # User chooses what to do
        action = inquirer.select(
            message="What would you like to do?",
            choices=[
                "Select / Create a New Character",
                "Spend Skill Points",
                "Battle Enemies",
                "Exit the Program"
            ],
            filter=lambda result: result.split()[0].lower(),
            border=True,
            default="Battle Enemies"
        ).execute()
        

        # Options and what they do
        print('\033c')
        if action == 'select':
            selected_character, rf = sel_menu(rf,attributes) # Select / Create a new character

        elif action == 'spend':
            selected_character[0] = skills(selected_character[0],attributes) # sets character to new stats
            rf[selected_character[1]] = selected_character[0] # Lets file write to it later

        elif action == 'battle':
            selected_character[0] = bst(rf_enemy,selected_character[0]) # User interface for battle, also adds xp / levels to character
            rf[selected_character[1]] = selected_character[0]

        elif action == 'exit':
            break
            
        
        write('battle_simulator/storage_csvs/characters.csv',rf) # Writes the file after all options have been finished
    write('battle_simulator/storage_csvs/characters.csv',rf) # Writes again for end thing
    print('\033cThank you for using my program!')
main()