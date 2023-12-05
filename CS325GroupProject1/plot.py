# Authors: Jordan Brisley & Jayden Zebrowski
# Date: 12/4/2023
# CS325-02 Group Project Module 5
# Purpose: The purpose of this module is to read the CSV files and create a matplotlib bar graph to show the difference in sentiment values.

import pandas
import matplotlib.pyplot as plt
import matplotlib.colors as col
import os, re

counter = 0
files = os.scandir("../CS325GroupProject1/data/processed/csv/")

for file in files:
    fname = file.name
    counter = counter+1                                 #updating counter
    df = pandas.read_csv(file, sep=",", engine= "python",)
    itemsList = [re.sub(".[0-9]+", "", str(val).strip()) for val in df]
    uniqueItems = set(itemsList)
    sentiments = []
    values = []
    bar_labels = []
    for item in uniqueItems:
        sentiments.append(item.title())
        values.append(itemsList.count(item))
        bar_labels.append(item.title())
        
    # colors = ['blue', 'red', 'gray']
    labelfont = {'color':'black','size':15}

    plt.bar(sentiments, values, color = col.TABLEAU_COLORS, label=bar_labels)
    plt.xlabel("Sentiments", fontdict=labelfont)
    plt.ylabel("Count", fontdict=labelfont)
    plt.title(fname[:-4].replace("_", " ") +  " Sentiments")
    plt.legend()
    plt.savefig(fname = "../CS325GroupProject1/data/plots/" + fname[:-4] + ".png")
    plt.clf()

# with open('../CS325GroupProject1/data/processed/csv/' + file, 'r') as read:
#for dirName, subDirList, fileList in os.walk('../CS325GroupProject1/data/processed/csv/'):



