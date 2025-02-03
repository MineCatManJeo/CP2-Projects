# Gabriel Crozier, Password generator
import random
import string

# Checks input for number or bool, error handler and default settings
def check_dataType(input_text, dataType, default = 0):
    # This checks for number values
    if dataType == 'float':
        for i in range(10):
            try:
                user_data = float(input(input_text))
                break
            except:
                print('That was not a number, please try again.\n')
        else:
            print(f'To many attempts, defaulted to {default}.')
            user_data = default
            # This is for boolean values
    if dataType == 'bool':
        user_data = input(input_text).lower()
        if user_data == 'n':
            user_data = False
        else:
            user_data = True
    return user_data

# randomly generates each character in your password based off off the values you allowed
def randomNumGenerator(length, num, sym, upper, lower):
    password = ''
    for character in range(length):
        # Adds each character to this string
        possibleCharacters = ''
        if num: possibleCharacters += string.digits
        if sym: possibleCharacters += string.punctuation
        if upper: possibleCharacters += string.ascii_uppercase
        if lower: possibleCharacters += string.ascii_lowercase
        password += random.choice(possibleCharacters)
    return password

# Main UI, allows for multiple generations of passwords
def main():
    print('\033cWelcome to the random password generator.')
    print('This generator will ask you a few questions then it will generate you 4 paswords for you to chose from.')
    while True:
        length = int(check_dataType('How long would you like your password to be? --->  ', 'float', 10))
        numbers = check_dataType('Do you wish to include numbers? (y/n) --->  ', 'bool')
        symbols = check_dataType('Do you wish to include symbols? (y/n) --->  ', 'bool')
        upper = check_dataType('Do you wish to include uppercase letters? (y/n) --->  ', 'bool')
        lower = check_dataType('Do you wish to include lowercase letters? (y/n) --->  ', 'bool')
        if not numbers and not symbols and not upper and not lower:
            lower = True
        print('\033cHere are 4 randomly generated passwords: ')
        for i in range(4):
            # Generated password
            password = randomNumGenerator(length,numbers,symbols,upper,lower)
            # Prints 4 generated passwords
            print(f'{i+1}. {password}')
        # Allows for user to leave program
        if input('Would you like to generate new passwords? (y/n) --->  ').lower() == 'n':
            break
    
main()