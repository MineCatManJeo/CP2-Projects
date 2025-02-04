# Gabriel Crozier, Morse Code Translator


# translates alphabet to morse code
def abc_to_morse(abc, morse):
    # turns text into a list, finds the corresponding morse code counterpart, translates it, and adds seperators when needed.

    print('\033cYou have chosen the alphabet to morse code translation. Input text to translate:')
    text_translate = list(input('  --->  ').lower())

    text_translated = ['  ']
    for i in range(len(text_translate)):
        if text_translate[i] in abc:
            text_translated.append(morse[abc.index(text_translate[i])])

        elif text_translate[i] == ' ':
            text_translated.append('/')
    
        elif text_translate[i] == '.':
            text_translated.append(':')

        else:
            text_translated.append('?')
        
    print('\033cYour text has been translated!\n(? has replaced any non translatable symbols)\n(A new line means a new sentence): ')
    print(' '.join(text_translated))

    input('\nHit enter if you are ready to move on ')
    print('\033c')


# translates morese code to alphabet
def morse_to_abc(abc, morse):
    # splits into a list around the spaces, translates, adds in word / sentence seperators

    print('\033cYou have chosen the morse code to alphabet translation.')
    print('(Type in each morse code character with . and -)')
    print('Between each letter add a space and between words add a slash with spaces surrounding it ( / )')
    print('Between sentences add a colon with spaces surrounding it ( : )')
    morse_translate = input('  --->  ').split(' ')

    morse_translated = '  '
    for i in range(len(morse_translate)):
        if morse_translate[i] in morse:
            morse_translated += abc[morse.index(morse_translate[i])]
        elif morse_translate[i] == '/':
            morse_translated += ' '
        elif morse_translate[i] == ':':
            morse_translated += '.'
        else: morse_translated += '?'
        
    print('\033cYour morse code has been translated!\n(? has replaced any non translatable symbols)\n')
    print(morse_translated)

    input('\nHit enter if you are ready to move on ')
    print('\033c')


# List Setup and Main UI
def main():
    # This is the list setup
    abc = list('abcdefghijklmnopqrstuvwxyz1234567890')
    morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'.split(' ')
    
    # This is main UI
    print('\033cWelcome to my morse code translator!\n')

    while True:
        print('''What would you like to do?:
  1. Translate alphabet to morse code
  2. Translate morse code to alphabet
  3. Exit program''')
        option = input('--->  ')

        if option.isdigit():

            if option == '1':
                abc_to_morse(abc, morse)

            elif option == '2':
                morse_to_abc(abc, morse)
                
            elif option == '3':
                break
            # error handler for not correct number
            else: print(f'\033c|  {option}  | is not a valid number! Please try again!\n')
        # error handler for not number
        else: print(f'\033c|  {option}  | is not a valid option! Please try again! (Options are the numbers 1, 2, 3)\n')
    print('\033cThank you for using this program!')
main()