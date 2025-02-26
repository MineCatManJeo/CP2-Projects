from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator
from read_file import open_csv_all as open_all, open_csv_column as open_column, open_csv_column_sep as open_column_sep

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
        print('\033c')

        if action == 'all':
            moviesAll = open_all()
            for movie in moviesAll:
                # TITLE, by DIRECTOR is GENRE, LENGTH minutes long, rated RATING, and stars ACTORS!GENRE
                print(f'{movie[0]:>40},  by {movie[1]:>45}  is  {movie[2]:>20} ,  {movie[4]:>3}  minutes long, rated  {movie[3]:>9} , and stars  {movie[5]}!')
            print('\n')

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
                validate=lambda result: len(result) >= 2,
                invalid_message="should be at least 2 selections",
                transformer=lambda result: ", ".join(result[0:-1]) + ", and " + result[-1]
            ).execute()

            for frence in prefrences:
                if frence == 'Rating':
                    choices = list(set(open_column(frence)))
                elif frence == 'Genre':
                    choices = list(set(open_column_sep(frence,"/")))
                elif frence in ['Director','Notable Actors']:
                    choices = list(set(open_column_sep(frence,", ")))
                else: # Length
                    length = []
                    length.append(inquirer.number(
                        message="What minimum length would you prefer?",
                        instruction="Input min minute count",
                        validate=EmptyInputValidator('input should not be empty'),
                        filter=lambda result: int(result),
                        transformer=lambda result: f"{result} minutes",
                    ).execute())

                    length.append(inquirer.number(
                        message="What maximum length would you prefer?",
                        instruction="Input max minute count",
                        validate=lambda result: int(result) >= length[0],
                        invalid_message="input has to be larger than previous minute count",
                        filter=lambda result: int(result),
                        transformer=lambda result: f"{length[0]}-{result} minutes",
                    ).execute())

                    searches.append(length)
                    continue
                choices.sort()
                searches.append(inquirer.fuzzy(
                    message=f"What {frence} would you like to search for?",
                    choices=choices,
                    validate=lambda result: result in choices,
                    invalid_message="choose one of the availiable options"
                ).execute()) # Need to go through each search option and allow for choices
            print('\033c')
            print(searches)

        elif not action:
            print('Thank you for using my program!')
            break

if __name__ == "__main__":
    main()