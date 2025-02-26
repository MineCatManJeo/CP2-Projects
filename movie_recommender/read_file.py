# This file reads the movie CSV file
import csv
def open_csv_column(column_name):
    with open("movie_recommender/Movies list.csv",'r',newline='') as movies:
        csvreader = csv.DictReader(movies, fieldnames=['Title','Director','Genre','Rating','Length (min)','Notable Actors'])
        next(csvreader)
        column_info = []
        for row in csvreader:
            column_info.append(row[column_name])
    return column_info
def open_csv_column_sep(column_name,separator):
    with open("movie_recommender/Movies list.csv",'r',newline='') as movies:
        csvreader = csv.DictReader(movies, fieldnames=['Title','Director','Genre','Rating','Length (min)','Notable Actors'])
        next(csvreader)
        column_info = []
        for row in csvreader:
            column_info.append(row[column_name])
    column_info = [item for items in column_info for item in items.split(separator)]
    return column_info
def open_csv_all():
    with open("movie_recommender/Movies list.csv",'r',newline='') as movies:
        csvreader = csv.reader(movies)
        next(csvreader)
        row_info = []
        for row in csvreader:
            row_info.append(list(row))
    return row_info