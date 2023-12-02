# Authors: Jordan Brisley & Jayden Zebrowski
# Date: 12/5/2023
# CS325-02 Group Project Module 5
# Purpose: The purpose of this module is to read the CSV files and create a matplotlib bar graph to show the difference in sentiment values.

import pandas
import matplotlib.pyplot as plt
import os

counter = 0
files = os.scandir("../CS325GroupProject1/data/processed/csv/")

for file in files:
    counter = counter+1                                 #updating counter
    df = pandas.read_csv(file, sep=", ", engine= "python",)
    positive = df.filter(regex='positive')
    positivecount = (len(positive.columns))

    negative = df.filter(regex='negative')
    negativecount = (len(negative.columns))

    neutral = df.filter(regex='neutral')
    neutralcount = (len(negative.columns))

    sentiments = ["Positive", "Negative", "Neutral"]
    values = [positivecount, negativecount, neutralcount]
    colors = ['blue', 'red', 'gray']
    labelfont = {'color':'black','size':15}
    bar_labels = ["Positive", "Negative", "Neutral"]

    plt.bar(sentiments, values, color = colors, label=bar_labels)
    plt.xlabel("Sentiments", fontdict=labelfont)
    plt.ylabel("Count", fontdict=labelfont)
    plt.title("URL" + str(counter) +  " Sentiments")
    plt.legend()
    plt.savefig(fname = "../CS325GroupProject1/data/plots/figure" + str(counter) + ".png")
    plt.clf()

# with open('../CS325GroupProject1/data/processed/csv/' + file, 'r') as read:
#for dirName, subDirList, fileList in os.walk('../CS325GroupProject1/data/processed/csv/'):



