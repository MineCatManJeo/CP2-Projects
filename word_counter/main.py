# Gabriel Crozier, Word Counter for User Inputted File

# All Imported Files
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from read_file import read_file
from time_handling import add_time
from write_file import write_file


def main():
    print('\033cMAKE SURE TO READ THE INSTRUCTIONS\n')
    print("Also If you don't have a file to check the word count, you can make one in the Documents folder!")
    while True:

        file_location = inquirer.filepath( # Lets user choose filepath
            message="What file would you like to get the word count of?",
            default="word_counter\Documents\\",
            long_instruction="Press [Tab] to gain autofill options, Press [Enter] to finish selection",
            validate=PathValidator(is_file=True, message="Input is not a file"),
        ).execute()

        file_rows = read_file(file_location)

        if file_rows: # If the file was found or if the file has more than 0 rows of data
            file_rows = add_time(file_rows)
            write_file(file_location,file_rows) # Writes the file
            print(F'\033cFile Location: {file_location}, {file_rows[-1]}')
        
        leave = inquirer.confirm(
            message="Would you like to exit the program?",
            long_instruction="Press [y] to exit program, Press [x] or [Enter] to continue",
            default=False,
        ).execute()

        if leave: # If the user want to leave, let them exit
            break
    print('\033cThank you for using my program!')



main()