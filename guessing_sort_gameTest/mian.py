import math
def sort_key(item):
    score = 0
    for letter in list(item):
        order = ord(letter.lower())-96
        if order > 13 and order <= 26:
            score += math.sqrt(order)
        if order <= 13 and order >= 1:
            score -= math.cbrt(order)
    score / len(item)
    return(item)

def user_word():
    sentence = []
    info = int(input('How many words would you like to write? --->  '))
    for i in range(info):
        word = input("Write a word that could help you figure out my sorting algorithm. --->  ")
        sentence.append(word)
    return sentence

def main():
    print('Welcome to my sorting guessing game! You just need to guess how I sorted your words!')
    words = user_word()
    words.sort(key=sort_key)
    print(words)
main()
