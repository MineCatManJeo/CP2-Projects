# Inquirerpy! Gives a list of every character to choose from

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

def select_char(rf):
    selected_character = inquirer.fuzzy(
        message="Who would you like to select?",
        choices=[
            Choice(name=f"{rf[x]['name']}, lvl: [{rf[x]['level']}]",value=[rf[x],x]) for x in range(len(rf))
        ],
        instruction="Type Name in for More Specific Results",
    ).execute()
    return selected_character