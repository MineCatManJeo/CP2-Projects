# Gabriel Crozier, Morse Code Translator

def abc_to_morse(abc, morse):
    print('\033cYou have chosen the alphabet to morse code translation. Input text to translate:')
    text_translate = list(input('  --->  ').lower())

    text_translated = ['  ']
    for i in range(len(text_translate)):
        if text_translate[i] in abc:
            text_translated.append(morse[abc.index(text_translate[i])])

        elif text_translate[i] == ' ':
            text_translated.append(' ')
    
        elif text_translate[i] == '.':
            text_translated.append('\n')

        else:
            text_translated.append('?')
        
    print('\033cYour text has been translated!\n(? has replaced any non translatable symbols)\n(A new line means a new sentence): ')
    print(' '.join(text_translated))

    input('\nHit enter if you are ready to move on ')
    print('\033c')



def morse_to_abc(abc, morse): # NOT DONE YET
    print('\033cYou have chosen the morse code to alphabet translation.')
    print('(Type in each morse code character with . and _)')
    print('Between each letter add a space and between words add a comma. Sentence')
    morse_translate = list(input('  --->  ').lower())

    morse_translated = ['  ']
    for i in range(len(morse_translate)):
        if morse_translate[i] in abc:
            morse_translated.append(morse[abc.index(morse_translate[i])])

        elif morse_translate[i] == ' ':
            morse_translated.append(' ')
    
        elif morse_translate[i] == '.':
            morse_translated.append('\n')

        else:
            morse_translated.append('?')
        
    print('\033cYour morse code has been translated!\n(? has replaced any non translatable symbols)\n(A new line means a new sentence): ')
    print(' '.join(morse_translated))

    input('\nHit enter if you are ready to move on ')
    print('\033c')


# List Setup and Main UI
def main():
    # This is the list setup
    abc = list('abcdefghijklmnopqrstuvwxyz1234567890')
    morse = '._ _... _._. _.. . .._. __. .... .. .___ _._ ._.. __ _. ___ .__. __._ ._. ... _ .._ ..._ .__ _.._ _.__ __.. .____ ..___ ...__ ...._ ..... _.... __... ___.. ____. _____'.split(' ')
    
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

            else: print(f'\033c|  {option}  | is not a valid number! Please try again!\n')

        else: print(f'\033c|  {option}  | is not a valid option! Please try again! (Options are the numbers 1, 2, 3)\n')
    print('\033cThank you for using this program!')
main()