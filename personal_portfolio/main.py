# Gabriel Crozier, Portfolio assignment
from InquirerPy import inquirer
from InquirerPy.separator import Separator

from movie_recommender import main as movie_recommender # USE AI TO FIGURE OUT PROBLEM
from todo_list import main as todo_list # IF NO WORK THEN USE SAMUAL METHOD (JUST COPY AND PAST IN THE FILES TO YOUR CODE)
from morse_code_translator import main as morse_code_translator
from random_password_generator import main as random_password_generator
from word_counter import main as word_counter
from coin_counter import main as coin_counter

def try_func(func):
    try: func()
    except: print("There was an error in your fuction...")

def main():
    print('\033cWelcome to my personal portfolio!')
    while True:
        game = inquirer.select(
            message="What poroject would you like to select?",
            choices=[
                "Movie Recommender",
                "To-do List",
                "Morse Code Translator",
                "Random Password Generator",
                "Word Counter",
                "Coin Counter",
                Separator(),
                "Exit"
            ],
            filter=lambda result:result.split()[0]
        ).execute()

        if game == "Exit": # NEED TO ADD DESCRIPTION
            break # Exits program
        elif game == "Movie":
            try_func(movie_recommender)
        elif game == "To-do":
            try_func(todo_list)
        elif game == "Morse":
            try_func(morse_code_translator)
        elif game == "Random":
            try_func(random_password_generator)
        elif game == "Word":
            try_func(word_counter)
        elif game == "Coin":
            try_func(coin_counter)
        else:
            print("There was an error in the action section")

    print("Thank you for seeing my portfolio!")
