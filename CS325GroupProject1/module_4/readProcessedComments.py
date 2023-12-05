import os
import regex, re
# from module_4 import sentiment_analysis
BATCH_SIZE = 2300
SLEEP_TIME = 15

#Changing the value of either of these if statement changes the length of the batch. If you get fails adjust this
#Bigger values for BATCH_SIZE mean the program runs faster but is more prone to errors coming from google API
#Lower values also tend to have issues from Google API because you send too many API requests too quicly
#Longer SLEEP_TIME means the program will take longer to run but will be more consistent

files = os.scandir("../CS325GroupProject1/data/processed/comments/")
fileDataRaw = []
fileNames = []
for filePath in files:
    # print(filePath)
    fa = open(filePath, "r", encoding="utf8")
    # for line in fa:
    #     print(line)
    fileNames.append(filePath.name)
    fileDataRaw.append(fa.readlines())
# We now have all the files read
fileData = []
i = 0
for pageData in fileDataRaw:
    
    fileData.append([])
    lineCount = -1 #Starting at -1 to add 1 and get to 0
    for line in pageData:
        if "[â€“]" in line:
            # Consider this a title line
            reg = r".*?points.*?([0-9]+) points"
            score = regex.match(reg, line)
            fileData[i].append(["", score])
            lineCount += 1
        elif line.strip() == "":
            continue #Skip empty lines
        else:
            clean_line = re.sub(r'[^a-zA-Z0-9\.\-\_\,\(\)\"\' ]', '', line.strip())
            fileData[i][lineCount][0] += clean_line
        
    
    i += 1
    # i += 1
# print(fileData[0])
# for comment, score in fileData:
#     print("Comment: ", comment.strip())
#     print("Score: ", score)
#     # Have the file info out

# Testing function


commentVals = []
commentVals.append("")
j = 0
for file in fileData:
    for i in range(50):
        if len(file) > i:
            commentVals[j] += file[i][0] + "\n"
    j += 1
    commentVals.append("")
commentVals.pop(len(commentVals) - 1)

from bardapi import Bard
import requests

PSID = open("./module_4/PSID", "r").readline()
PSIDCC = open("./module_4/PSIDCC", "r").readline()
PSIDTS = open("./module_4/PSIDTS", "r").readline()

session = requests.Session()
# This is a whole pain but it does actually work unlike chatgpt
session.cookies.set("__Secure-1PSID", PSID)
session.cookies.set( "__Secure-1PSIDCC", PSIDCC)
session.cookies.set("__Secure-1PSIDTS", PSIDTS)
session.headers = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
 }

global client
client = Bard(token=PSID, session=session)
# The starting prompt in order to get information properly


def getSentiment(val : str) -> str:
    prompt = "I am going to send you a series of comments, only give me the sentiment analysis for each of the following comments in order. Do not explain the sentiment, do not add any extra information. Only separate the sentiments by a comma. Do not say which comment the sentiment belongs to.\n"
    global client
    response = client.get_answer(prompt + val)
    # print(prompt + val)
    return response["content"]

i = 0
from time import sleep
for val in commentVals:
    # print("Getting sentiments for: ", val[:500])
    # If we allow too many sentiments through the ai gets confused and does not answer properly
    splitVals = val.split("\n")
    currentVals = ""
    responses = ""
    fa = open(f"./data/processed/csv/{fileNames[i][:-4]}.csv", "w")

    i += 1
    
    itemsPerBatch = 7
    for j in range(len(splitVals)):
        # print(len(currentVals))
        if len(currentVals) > BATCH_SIZE: 
            # On every fifth value send it to the ai
            print("Getting sentiment batch")
            batch = getSentiment(currentVals)
            print(batch)
            if "language model" in batch:

                
                print("Batch failed, too long")
                responses += "FAIL, " * itemsPerBatch
                continue
            elif "cookie values" in batch:
                print("batch failed, cookie error")
                # j -= 1
                continue
            responses += batch + ", "
            print("Sentiment batch received")
            if (j > 100):
                break #Just to make sure this doesn't continue through all comments
            currentVals = ""
            # Needed to slow down the receiving otherwise google would get mad for sending too many
            sleep(SLEEP_TIME)
        # Sleep between files to give extra safety
        currentVals += splitVals[j].strip()
    responses += getSentiment(currentVals)
    # Add the rest of the values to the sentiment
    # print(sentiments)
    cleanedResponsesStep1 = responses.replace(".", "").replace("\n", "").replace(",,", ",").lower() #So many things that can go wrong with the data it outputs
    cleanedResponsesStep2 = re.sub("\[.*?\]", "", cleanedResponsesStep1) #Google bard added image outputs, this removes the information from those.
    fa.writelines(cleanedResponsesStep2) #Make sure there are no formatting issues. AI isn't very consistent with this stuff
    sleep(SLEEP_TIME * 2) #Extra slowdown to be more sure we wont have any issues between files
