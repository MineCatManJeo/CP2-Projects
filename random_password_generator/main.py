# Gabriel Crozier, Password generator
import random
import string

# Checks input for number or bool, error handler and default settings
def check_dataType(input_text, dataType, default = 0):
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
    if dataType == 'bool':
        user_data = input(input_text).lower()
        if user_data == 'n':
            user_data = False
        else:
            user_data = True
    return user_data

def randomNumGenerator(length, num, sym, upper, lower):
    password = ''
    for character in range(length):
        possibleCharacters = ''
        if num: possibleCharacters += string.digits
        if sym: possibleCharacters += string.punctuation
        if upper: possibleCharacters += string.ascii_uppercase
        if lower: possibleCharacters += string.ascii_lowercase
        password += random.choice(possibleCharacters)
    return password


def main():
    print('\033cWelcome to the random password generator.')
    print('This generator will ask you a few questions then it will generate you 4 paswords for you to chose from.')
    while True:
        length = int(check_dataType('How long would you like your password to be? --->  ', 'float', 10))
        numbers = check_dataType('Do you wish to include numbers? (y/n) --->  ', 'bool')
        symbols = check_dataType('Do you wish to include symbols? (y/n) --->  ', 'bool')
        upper = check_dataType('Do you wish to include uppercase letters? (y/n) --->  ', 'bool')
        lower = check_dataType('Do you wish to include lowercase letters? (y/n) --->  ', 'bool')
        passwords = []
        print('\033cHere are 4 randomly generated passwords: ')
        for i in range(4):
            passwords.append(randomNumGenerator(length,numbers,symbols,upper,lower))
            print(f'{i+1}. {passwords[-1]}')
        if input('Would you like to generate new passwords? (y/n) --->  ').lower() == 'n':
            break
    
main()