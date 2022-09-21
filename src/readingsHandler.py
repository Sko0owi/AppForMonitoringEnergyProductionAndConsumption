
import os

import src.csvFilesHandler as FileHandler



date_month = 3
date_year = 2021

readings_header = ['date', '1.8.0', '1.8.1', "1.8.2", "2.8.0", "2.8.1", "2.8.2"]

readings_dictionary = []

readings_change_dictionary = []


def generateReadingsChange():
    readings_change_dictionary.clear()
    if len(readings_dictionary) != 0:
        previous = {'date': readings_dictionary[0]['date'],
                    '1.8.0': readings_dictionary[0]['1.8.0'],
                    '1.8.1': readings_dictionary[0]['1.8.1'],
                    '1.8.2': readings_dictionary[0]['1.8.2'],
                    '2.8.0': readings_dictionary[0]['2.8.0'],
                    '2.8.1': readings_dictionary[0]['2.8.1'],
                    '2.8.2': readings_dictionary[0]['2.8.2']}
        for row in readings_dictionary:
            newRow = {'date': row['date'],
                    '1.8.0': int(row['1.8.0']) - int(previous['1.8.0']),
                    '1.8.1': int(row['1.8.1']) - int(previous['1.8.1']),
                    '1.8.2': int(row['1.8.2']) - int(previous['1.8.2']),
                    '2.8.0': int(row['2.8.0']) - int(previous['2.8.0']),
                    '2.8.1': int(row['2.8.1']) - int(previous['2.8.1']),
                    '2.8.2': int(row['2.8.2']) - int(previous['2.8.2'])}
            previous = row
            readings_change_dictionary.append(newRow)


def dateChange(next_date):
    global date_month, date_year
    if next_date == "next":
        date_month += 1
        if date_month == 13:
            date_month = 1
            date_year += 1
    elif next_date == "previous":
        date_month -= 1
        if date_month == 0:
            date_month = 12
            date_year -= 1
    else:
        print("wrong command")

def checkLastRowDate():
    if len(readings_dictionary) == 0:
        return "error"
    return readings_dictionary[len(readings_dictionary) - 1]['date']

def deleteLastRow():
    dateChange("previous")

    readings_dictionary.pop(len(readings_dictionary) - 1)

    FileHandler.saveChangesToCSVFiles()
    showData()
    

def addNewRow(f180,f181,f182,f280,f281,f282):
    row = {'date': str(date_month) + "/" + str(date_year),
        '1.8.0': f180,
        '1.8.1': f181,
        '1.8.2': f182,
        '2.8.0': f280,
        '2.8.1': f281,
        '2.8.2': f282}
    readings_dictionary.append(row)

    dateChange("next")

    FileHandler.saveChangesToCSVFiles()
    showData()

def editExistingRow(index,f180,f181,f182,f280,f281,f282):
    readings_dictionary[index]['1.8.0'] = f180
    readings_dictionary[index]['1.8.1'] = f181
    readings_dictionary[index]['1.8.2'] = f182
    readings_dictionary[index]['2.8.0'] = f280
    readings_dictionary[index]['2.8.1'] = f281
    readings_dictionary[index]['2.8.2'] = f282

    FileHandler.saveChangesToCSVFiles()
    showData()

def findRowIndexByDate(date):
    for i in range(len(readings_dictionary)):
        if readings_dictionary[i]['date'] == date:
            return i
    return -1


def showData():
    cls = lambda: os.system('cls')
    cls()

    for r in readings_dictionary:
        print(r)
    print("\n")
