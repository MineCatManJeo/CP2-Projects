# User system where they can add / subtract points to skills

from InquirerPy import inquirer
from InquirerPy.separator import Separator

def skills(character):
    # User skill tree UI
    print('\033c')
    skill_set = inquirer.checkbox(
        message='-- Skill Tree --',
        choices=[
            f'Health [{character['hea']}]',
            f'Strength [{character['str']}]',
            f'Defence [{character['def']}]',
            f'Speed [{character['spe']}]',
            Separator(line='-' * 25),
            'Reset Skill Tree',
            'Exit Skil Tree',
        ],
        instruction="Press [Space] to Select / Deselect Options",
        long_instruction="---------- EXTRA INSTRUCTION ----------\nSelecting the [Reset] Option Sets All Skills to 0, While Giving You Your Points Back,\nSelecting the [Exit] Option Exits Skill Selection",
        filter=lambda result: [res.split()[0].lower()[0:3] for res in result]
    ).execute()
    print(skill_set)


# Check list, user selects skills they want to add to, and when the press enter it adds 1 point to each skill selected (if possible), then it asks again so they can do it again. Once the are done they just have to select the exit skills button
# EXAMPLE:
# Add points to your skils!
#   Health   [2]
# > Strength [4] Current selection
#   Defence  [1]
# > Speed    [8] Current selection
#   Exit Skill Tree

#   Health   [2]
# > Strength [5] Will stay selected on next ask
#   Defence  [1]
# > Speed    [9] Will stay selected on next ask
#   Exit Skill Tree

#   Health   [2]
#   Strength [5]
# > Defence  [1] # Will not add point because exit is selected
#   Speed    [9]
# > Exit Skill Tree # Will exit skill tree

#   Health   [2]
#   Strength [5]
#   Defence  [1]
#   Speed    [9]
# > Reset Skill Points # Maybe this here?, or I could add as a precurser to this, maybe not though
#   Exit Skill Tree
skills({'name':'Billy','level':0,'points':7,'hea':0,'str':0,'def':0,'spe':0})