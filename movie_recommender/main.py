# Gabriel Crozier, Movie Recommender

from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

name = inquirer.text(message="Name:").execute()
name = inquirer.text(message="Confirm Name:", default=lambda _:name).execute()
age = inquirer.text(
    message=lambda _: f"Hi {name}, enter your age:", validate=NumberValidator()
).execute()