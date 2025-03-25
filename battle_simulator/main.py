# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer

from read_file import read_file as read
from write_file import write_file as write
from select_char_menu import select_char_menu as sel_menu
from skill_point import skills

def main():
    print('\033c')

    # Setup
    attributes = ['Health','Strength','Defence','Speed']
    rf = read('battle_simulator/storage_csvs/characters.csv')
    selected_character = False
    spend_points = ""


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
    print('\033cThank you for using my program!')



main()