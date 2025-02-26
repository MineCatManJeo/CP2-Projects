from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator
from read_file import open_csv_all as open_all, open_csv_column as open_column, open_csv_column_sep as open_column_sep
from search_file import search

def main():
    print('\033cWelcome to my movie recommender program!')
    # Ask user for if print out full or serach DONE
    # Full just sends to seperate file for grabbing everythin
    # Search asks user for search options in main
    #   then after asks it also goes to seperate file for searching mechanic
    # Print in user freindly
    # Run again
    while True:

        # The beggining action
        action = inquirer.select(
            message="What would you like to do?",
            instruction="Press [Enter] to select:",
            long_instruction="Press [up/down] arrows to select new options",
            choices=[
                Choice(value="all",name="Print All Movies"),
                Choice(value="select",name="Search For Movies"),
                Choice(value=None,name="Exit Program"),
            ],
            default=None,
        ).execute()
        print('\033c')

        # If the action is all it prints all movies
        if action == 'all':
            moviesAll = open_all()
            for movie in moviesAll:
                # TITLE, by DIRECTOR is GENRE, LENGTH minutes long, rated RATING, and stars ACTORS!GENRE
                print(f'{movie[0]:>40},  by {movie[1]:>45}  is  {movie[2]:>20} ,  {movie[4]:>3}  minutes long, rated  {movie[3]:>9} , and stars  {movie[5]}!')
            print('\n')

        # If the action is select, it gives the user a ton of options to choose from
        elif action == 'select':
            searches = []

            # The user choice between categories such as Genre and Director
            prefrences = inquirer.select(
                message="What would you like to search for?",
                instruction="Press [Space] to toggle a selection (Multiselect):",
                long_instruction="Once you've selected your prefrences, you can press [Enter] to end selection",
                choices=[
                    "Director",
                    "Genre",
                    "Rating",
                    Choice(value="Length (min)", name="Length"),
                    "Notable Actors",
                ],
                multiselect=True,
                validate=lambda result: len(result) >= 1,
                invalid_message="should be at least 1 selection",
                transformer=lambda result: ", ".join(result[0:-1]) + ", and " + result[-1]
            ).execute()

            # for each of the categories it allows the user to actually search for something
            for frence in prefrences:

                if frence == 'Rating': # Rating choices
                    choices = list(set(open_column(frence)))
                elif frence == 'Genre': # Genre choices
                    choices = list(set(open_column_sep(frence,"/")))
                elif frence in ['Director','Notable Actors']: # Director / Actors choices (Sadly you only get to choose one during selection)
                    choices = list(set(open_column_sep(frence,", ")))
                else: # Length category, needs it's own unique code unlike the others
                    length = []
                    length.append(inquirer.number(
                        message="What minimum length would you prefer?",
                        instruction="Input min minute count",
                        long_instruction="There will be a maximum length question after this",
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

                # This is the UI for everything exept the length category
                choices.sort()
                searches.append(inquirer.fuzzy(
                    message=f"What {frence} would you like to search for?",
                    instruction="Typing shows you more options:",
                    long_instruction="You can't search for more than one item, so press [Enter] when ready",
                    choices=choices,
                    validate=lambda result: result in choices,
                    invalid_message="choose one of the availiable options"
                ).execute()) # Need to go through each search option and allow for choices
            print('\033c')

            all_movies_search = open_all()
            relevence1_s, relevence2_s = search(all_movies_search,searches)

            if len(relevence1_s) + len(relevence2_s) == 0:
                print('No movie was found!')
            else:
                print('All movies that were directly searched: ') # All movies directly found by you
                for found in relevence1_s:
                    print(f'{found[0]:>40},  by {found[1]:>45}  is  {found[2]:>20} ,  {found[4]:>3}  minutes long, rated  {found[3]:>9} , and stars  {found[5]}!')

                if len(searches) >= 3:
                    print('\nYou might also like these movies: (These movies are one off of your search results)') # All movies that were 1 off your search criteria
                    for found in relevence2_s:
                        print(f'{found[0]:>40},  by {found[1]:>45}  is  {found[2]:>20} ,  {found[4]:>3}  minutes long, rated  {found[3]:>9} , and stars  {found[5]}!')


        elif not action: # if the user chose Exit it leaves the program
            print('Thank you for using my program!')
            break

if __name__ == "__main__": # Please tell me if im using this wrong, I know you can sometimes use it for other files, but is that only if they have a main functions, also is this only for the main.py?
    main()