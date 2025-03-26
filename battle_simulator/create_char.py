# User chooses name, then it runs skill_point to allow user to choose where to put points

from InquirerPy import inquirer
from skill_point import skills

def create_char(attrib):
    character = {'name':None,'level':0,'points':7,'xp':0,'hea':0,'str':0,'def':0,'spe':0} # Base character for easy modification
    name = inquirer.text(
        message="What would you like to name your new character?",
        validate=lambda result:all([x in ' -' or x.isalpha() for x in result]) and result != '', # Ensures character isn't empty, or contains non letters
        invalid_message="Name must be all letters!",
        filter=lambda result:result.title(),
        transformer=lambda result:result.title(),
    ).execute()
    character['name'] = name
    
    print('\033c')
    character = skills(character,attrib) # Sets up skills for that character
    return [character]