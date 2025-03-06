# Add the correct time and word count to the end of the variable that holds the read file
import datetime

def add_time(rows):

    current_time = datetime.datetime.now()
    formatted_date = current_time.strftime("Time: %m-%d-%Y, %H:%M:%S") # Grabs the currect date and stuffs it into a readable format
    word_count = 0
    
    for row in rows: # Also grabs word count to add to end of file
        word_count += len(row.split())

    if rows[-1][0:11] == "Word Count:": # Prints if there is already a word count at the end of the file
        rows[-1] = f'Word Count: {word_count-6}, {formatted_date}'
    else:
        rows.append('\n')
        rows.append(f'Word Count: {word_count}, {formatted_date}')
    return rows