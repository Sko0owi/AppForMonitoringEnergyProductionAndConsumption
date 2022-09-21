import csv


import src.readingsHandler as readingHandler
#from src.readingsHandler import dateChange, generateReadingsChange, readings_dictionary, readings_header, readings_change_dictionary, showData

def saveChangesToCSVFiles():

    with open('csvFiles/readingsFromRegister.csv', 'w', encoding='UTF8', newline='') as readings:
            writer = csv.DictWriter(readings, fieldnames=readingHandler.readings_header)
            writer.writeheader()
            writer.writerows(readingHandler.readings_dictionary)

    readingHandler.generateReadingsChange()

    with open('csvFiles/changeInReadingsFromRegister.csv', 'w', encoding='UTF8', newline='') as readings:
            writer = csv.DictWriter(readings, fieldnames=readingHandler.readings_header)
            writer.writeheader()
            writer.writerows(readingHandler.readings_change_dictionary)

def csvInit(fileExist):

    if fileExist:
        with open('csvFiles/readingsFromRegister.csv', 'r') as readings:
            dt = csv.DictReader(readings)
            for r in dt:
                row = {'date': r['date'],
                    '1.8.0': r['1.8.0'],
                    '1.8.1': r['1.8.1'],
                    '1.8.2': r['1.8.2'],
                    '2.8.0': r['2.8.0'],
                    '2.8.1': r['2.8.1'],
                    '2.8.2': r['2.8.2']}
                readingHandler.readings_dictionary.append(row)
            readingHandler.showData()

        if len(readingHandler.readings_dictionary) > 0:

            last_date = readingHandler.readings_dictionary[len(readingHandler.readings_dictionary) - 1]['date'].split("/")
            readingHandler.date_month = int(last_date[0])
            readingHandler.date_year = int(last_date[1])
            readingHandler.dateChange('next')

        saveChangesToCSVFiles()
    else:
        saveChangesToCSVFiles()
