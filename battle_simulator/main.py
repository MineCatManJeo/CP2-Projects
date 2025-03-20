# Gabriel Crozier, Battle Simulator
from InquirerPy import inquirer

from read_file import read_file as read
from select_char_menu import select_char_menu as sel_menu

def main():
    print('\033c')
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
    
    rf = read('battle_simulator/storage_csvs/characters.csv')
    sel_menu(rf)
    #main()



main()