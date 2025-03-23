# User system where they can add / subtract points to skills

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

def skills(character,attributes):
    # User skill tree UI
    attribute_abr = [x[0:3].lower() for x in attributes]

    for abr in attribute_abr: # Adds the attributes to the character
        if character.get(abr) == None:
            character[abr] = 0

    start_message = ""

    skill_set = inquirer.select(
        message=f'- [{character['points']}] - Skill Tree - [{character['points']}] -',
        choices=[
            Choice(name=f"{x} [{character[x[0:3].lower()]}]",value=x[0:3].lower()) for x in attributes
        ] + [
            Separator(line='-' * 25),
            'Reset Skill Tree',
            'Exit Skill Tree',
        ],
        instruction="Press [Space] to Select / Deselect Options",
        long_instruction="---------- EXTRA INSTRUCTION ----------\nSelecting the [Reset] Option Sets All Skills to 0, While Giving You Your Points Back,\nSelecting the [Exit] Option Exits and Saves Skill Selection\nWARNING: You May Have to Scroll to See More Options",
        filter=lambda result: [res.split()[0].lower()[0:3] for res in result],
        transformer=lambda _:"",
        multiselect=True,
        border=True,
        height=3+len(attributes),
    ).execute()

    if "exi" in skill_set:
        return character
    elif "res" in skill_set:
        for attribute in attribute_abr:
            character['points'] += character[attribute]
            character[attribute] = 0
    else:
        for attribute in skill_set:
            if character['points'] >= 1:
                character[attribute] += 1
                character['points'] -= 1
            else:
                start_message = "You don't have enough skill points!"
    
    print('\033c'+start_message)
    skills(character,attributes)
    return character