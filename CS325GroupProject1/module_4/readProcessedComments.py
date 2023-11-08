import os
import regex, re
# from module_4 import sentiment_analysis
files = os.scandir("./data/processed/")
fileDataRaw = []
for filePath in files:
    # print(filePath)
    fa = open(filePath, "r", encoding="utf8")
    # for line in fa:
    #     print(line)
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
    prompt = "I am going to send you a series of comments, only give me the sentiment analysis for each of the following comments in order. Do not explain the sentiment, do not add any extra information. Only separate the sentiments by a comma..\n"
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
    i += 1
    fa = open(f"./data/sentiments/sentiments{i}.csv", "w")
    itemsPerBatch = 7
    for j in range(len(splitVals)):
        print(len(currentVals))
        if len(currentVals) > 2500:
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
            
            currentVals = ""
            # Needed to slow down the receiving otherwise google would get mad for sending too many
            sleep(5)
        # Sleep between files to give extra safety
        currentVals += splitVals[j]
    responses += getSentiment(currentVals)
    # Add the rest of the values to the sentiment
    # print(sentiments)
    fa.writelines(responses.replace(".", ""))
    sleep(30) #Extra slowdown to be more sure we wont have any issues
