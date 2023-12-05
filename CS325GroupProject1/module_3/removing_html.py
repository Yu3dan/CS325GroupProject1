# Authors: Jordan Brisley & Jayden Zebrowski
# Date: 11/3/2023
# CS325-02 Group Project Module 3
# Purpose: The purpose of this last module is to take the unfiltered comment text files created by module 2 and make them readable by removing all html tags. Once finished, it sents it to folders data/processed/unfilteredcomments and creates a new text file
# named filteredcomments#.txt where each comment is now as it appears on the reddit website.

from bs4 import BeautifulSoup
import os

def remove_tags(html):                                          #cutting the HTML and CSS styling from the filtered text
    bs = BeautifulSoup(html, 'html.parser')
    for data in bs(['style', 'script']):
        data.decompose()
    return ' '.join(bs.stripped_strings)

counter = 0                                                     #initializing counter for files in data/raw/unfilteredcomments

for dirName, subDirList, fileList in os.walk('../CS325GroupProject1/data/raw/unfilteredcomments'):
        for file in fileList:
            counter = counter+1                                 #updating counter
            with open('../CS325GroupProject1/data/raw/unfilteredcomments/' + file, 'rb') as bs:
                soup = BeautifulSoup(bs, 'html5lib')    
            comments = soup.find_all('p')                                                                                                       #parsing to find comments 
            with open('../CS325GroupProject1/data/processed/comments/' + f'{file[:-4]}.txt', 'w', encoding="utf-8") as output:             #creating the final text file with each comment seperated and neatly placed without html.                       
                for comment in comments:       
                    output.write(remove_tags(comment.prettify()))
                    output.write("\n")

        
