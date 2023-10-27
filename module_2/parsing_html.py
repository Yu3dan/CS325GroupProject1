# Authors: Jordan Brisley & Jayden Zebrowski
# Date: 11/3/2023
# CS325-02 Group Project Module 2
# Purpose: The purpose of this module is to look through the html text files created by module 1 and filter out all of the unnecessary html portion as we only want the section that contains the comments. Once it does this, it saves that section into "commentree",
# and goes through the comments, saving it into "comments" as each reddit comment starts with the html tag <p>. It then creates a new text file named unfilteredcomomments#.txt with all the comments of the post with the html tags still attached under the 
# folders data/raw/unfilteredcomments/. 

from bs4 import BeautifulSoup
import os

counter = 0                 #counter for how many files are in the html folder in order to match them to the unfilteredcomments#.txt

for dirName, subDirList, fileList in os.walk('../CS325GroupProject1/Data/raw/html'):                #walking down the files in the directory ../CS325GroupProject1/Data/raw/html
        for file in fileList:
            counter = counter+1                                                                     #updating counter
            with open('../CS325GroupProject1/Data/raw/html/' + file, 'rb') as bs:                   #parsing through the html files given by module 1
                soup = BeautifulSoup(bs, 'html5lib')
                commentree = soup.find("div", attrs={'class':'sitetable nestedlisting'})            #finding the html section that contains all comments in post
                comments = commentree.find_all('p')                                                 #saving the list of comments 
            with open('../CS325GroupProject1/Data/raw/unfilteredcomments/' + f'unfilteredcomments{counter}.txt', 'w', encoding="utf-8") as output:                         #creating the new text files unfilteredcomments#.txt   
                for comment in comments:                                                                                                                                   #using a for loop to rewrite each comment with the html still attached
                    output.write((comment.prettify()))                                                                                                                     #creating an empty line between each comment
                    output.write("\n")                                                                                                                              
                           


     
