# Coin deliminator

from InquirerPy import inquirer
from read_file import read_file as read
from coin_change import coin_change as cc


def main():
    print('\033c')
    rf = read("coin_counter/coins.csv")
    countries = [cur['country'] for cur in rf]

    def Cindex(currency):
        return rf[countries.index(currency)]['currency']

    print(Cindex("EUR"))

main()