# Authors: Jordan Brisley & Jayden Zebrowski
# Date: 11/3/2023
# CS325-02 Group Project 1 Module 1
# Purpose: The purpose of this module is to take a text file full of old.reddit URLs given by the user and download the HTML of each website using a for loop. It then creates seperate text files for each URL in the list under the folder Data and subfolder raw.
# These files should be named html#.txt, EX: html1.txt html2.txt etc.

import sys
import urllib.request

file = sys.argv[1]                  #saving argument given by user

with open(file) as f:               #reading file and seperating each line(URL), saving them into all_links
    text = f.read()
    all_links = text.split('\n')

counter = 0                         #counter for how many URLs given in the list
for urls in all_links:              #for loop cycling through each link
    counter = counter+1                                                                                     #updating counter
    urllib.request.urlretrieve(urls, '../CS325GroupProject1/Data/raw/html/'+f'html{counter}.txt',)          #sending each links source code to data/raw/html and naming it html#.txt
