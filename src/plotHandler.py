import matplotlib.pyplot as plt
import numpy as np

from src.readingsHandler import generateReadingsChange, readings_change_dictionary

LabelList = ["1.8.0", "1.8.1", "1.8.2", "2.8.0", "2.8.1", "2.8.2"]

def generatePlot(startIndex, endIndex, boolList):

    adate = []
    registers_data = [[],[],[],[],[],[]]

    generateReadingsChange()


    for i in range(startIndex,endIndex + 1):
        row = readings_change_dictionary[i]
        adate.append(row['date'])
        registers_data[0].append(row['1.8.0'])
        registers_data[1].append(row['1.8.1'])
        registers_data[2].append(row['1.8.2'])
        registers_data[3].append(row['2.8.0'])
        registers_data[4].append(row['2.8.1'])
        registers_data[5].append(row['2.8.2'])

    for registerD in registers_data:
        np.asarray(registerD)

    fig, ax = plt.subplots(figsize=(18,9))

    x = range(endIndex - startIndex + 1)
    plt.xlabel("Month of Usage")
    plt.ylabel("Difference between months")
    plt.xticks(x, adate)

    for i in range(6):
        if boolList[i]:
            plt.plot(x, registers_data[i], label=LabelList[i])
            for index in range(len(x)):
                ax.text(x[index], registers_data[i][index], registers_data[i][index], size=12)

    plt.legend(loc="upper left")

    plt.show()
