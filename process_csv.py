import csv
import chord_backend as chord

# Processes csv file into chord object
def process_csv(file_name):
    chords = {}

    with open (file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                chords.update({row[0]: chord.Chord(row[0], row[1], row[2], row[3], row[4], row[5], row[6])})             
            line_count += 1
    
    return chords
