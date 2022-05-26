import csv

with open('Raw_Skills_Dataset.csv', 'r') as list_1, open('Example_Technical_Skills.csv', 'r') as list_2:
    fileone = list_1.readlines()
    filetwo = list_2.readlines()

with open('my_list.csv', 'w') as outFile:
    for line in filetwo:
        if line in fileone:
            outFile.write(line)
