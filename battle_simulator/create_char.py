# User chooses name, then it runs skill_point to allow user to choose where to put points

from InquirerPy import inquirer

def create_char():
    character = {}
    name = inquirer.text(
        message="What would you like to name your new character?",
        validate=lambda result:all([x in ' -' or x.isalpha() for x in result]) and result != '',
        invalid_message="Name must be all letters!",
        filter=lambda result:result.title(),
        transformer=lambda result:result.title(),
    ).execute()
    character['name'] = name

    character['level'] = 0
    character['points'] = 7
    
    # skill point for more data

    character['health'] = None
    character['strength'] = None
    character['defence'] = None
    character['speed'] = None

    return character