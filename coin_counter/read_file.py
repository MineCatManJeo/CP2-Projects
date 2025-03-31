# Reads the coin file
import csv

def read_file(location):
    with open(location,newline='') as file:
        reader = csv.DictReader(file,restkey="currency")
        return [row for row in reader] # Returns a list of dictionaries