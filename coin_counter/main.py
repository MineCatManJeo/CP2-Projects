# Coin deliminator

from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator
from read_file import read_file as read
from coin_change import coin_change as cc
from print_answer import print_answer as pa


def main():
    print('\033c')
    # Reads the file as a list of dictionaries
    rf = read("coin_counter/coins.csv")
    countries = [cur['country'] for cur in rf] # Only reads the first column

    def Cindex(currency): # Returns the second column of all of them
        return rf[countries.index(currency)]['currency']
    
    def numTransfer(num): # Turns items into floats
        try: num = float(num)
        except: num = 0
        return num
    
    def split_currency(country,place,convert=True): # Splits Penny-0.01 into Penny or 0.01 depending on place value
        if convert:
            return [numTransfer(x.split("-")[place]) for x in Cindex(country)]
        else:
            return [x.split("-")[place] for x in Cindex(country)]

    print("Welcome to my Coin Change Probloem Calculator!")

    while True:
        # Gives user a list of options (6 options, top result for common money)
        country = inquirer.fuzzy(
            message="What Currency Would You Like to Use?",
            choices=countries,
            validate=lambda result: result in countries,
            invalid_message="Not a valid option",
        ).execute()

        # User can select the amount of money they desire
        amount = float(inquirer.number(
            message="Enter the Amount of Money You Want to Use for the problem",
            min_allowed=0,
            max_allowed=250*float(Cindex(country)[-1].split('-')[1]), # Cant excede 250x the highest currency value of that currency
            float_allowed=True,
            replace_mode=True,
            validate=NumberValidator("Input should be a number",float_allowed=True),
            instruction="(Left / Right Arrows to move cursor past [.])",
            keybindings={"negative_toggle": []},
        ).execute())
        amount = round(amount,2) # Rounds it, lazy, but functional

        coin_solved = cc(amount,split_currency(country,1)) # Gives the solution to the coin change problem
        pa(coin_solved,split_currency(country,0,False),split_currency(country,1)) # Prints the solution relatively decently

        if not inquirer.confirm(message="Would you like to do it again?",instruction="(Type [y] to Continue and [n] to Exit)").execute(): # Asks if you would like to go again
            break
        print('\033c')
    print("\033cThank you for using my program!")

main()