# This file reads the movie CSV file
import csv
print('\033c')
def open_csv():
    with open("movie_recommender/Movies list.csv",'r',newline='') as movies:
        
        csvreader = csv.DictReader(movies, fieldnames=['Title','Director','Genre','Rating','Length (min)','Notable Actors'])
        for row in csvreader:
            print(row['Genre'])

open_csv()