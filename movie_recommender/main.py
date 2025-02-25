from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from read_file import open_csv

def main():
    print('\033cWelcome to my movie recommender program!')
    # Ask user for if print out full or serach DONE
    # Full just sends to seperate file for grabbing everythin
    # Search asks user for search options in main
    #   then after asks it also goes to seperate file for searching mechanic
    # Print in user freindly
    # Run again
    while True:
        action = inquirer.select(
            message="What would you like to do?",
            instruction="Press [Enter] to select:",
            choices=[
                Choice(value="all",name="Print All Movies"),
                Choice(value="select",name="Search For Movies"),
                Choice(value=None,name="Exit Program"),
            ],
            default=None,
        ).execute()
        if action == 'all':
            pass
        elif action == 'select':
            searches = []
            prefrences = inquirer.select(
                message="What would you like to search for?",
                instruction="Press [Space] to toggle a selection (Multiselect):",
                choices=[
                    "Director",
                    "Genre",
                    "Rating",
                    Choice(value="Length (min)", name="Length"),
                    "Notable Actors",
                ],
                multiselect=True,
            ).execute()
            for frence in prefrences:
                searches.append(inquirer.fuzzy(
                    message=f"What {frence} would you like to search for?",
                    choices=list(set(open_csv(frence))),
                ).execute()) # Need to go through each search option and allow for choices
        elif not action:
            print('Thank you for using my program!')
            break

if __name__ == "__main__":
    main()