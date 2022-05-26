import csv

with open('Raw_Skills_Dataset.csv', 'r') as list_1, open('Example_Technical_Skills.csv', 'r') as list_2, open('Example_Soft_Skills.csv', 'r') as list_3:
    fileone = list_1.readlines()
    filetwo = list_2.readlines()
    filethree = list_3.readlines()

with open('tech_list.csv', 'w') as techFile, open('soft_list.csv', 'w') as softFile:
    for line in filetwo:
        if line in fileone:
            techFile.write(line)
    for line in filethree:
        if line in fileone:
            softFile.write(line)
