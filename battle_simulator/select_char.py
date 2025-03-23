# Inquirerpy! Gives a list of every character to choose from

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

def select_char(rf):
    selected_character = inquirer.fuzzy(
        message="Who would you like to select?",
        choices=[
            f"{rf[x]['name']}, lvl: [{rf[x]['level']}]" for x in range(len(rf))
        ],
        filter=lambda result: result.split()[0],
        instruction="Type Name in for More Specific Results",
    ).execute()
    return selected_character