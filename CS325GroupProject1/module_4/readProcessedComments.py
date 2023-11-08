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

from openai import OpenAI
prompt = """I am going to send you a series of comments, give me the sentiment analysis for each of the following comments in order. Do not explain the sentiment, do not add any extra information. Only separate the sentiments by a comma..\n
"""
# Use the prompt and add the lines


# Create the client for chatGPT
global client

fa = open("./module_4/api_key.txt", "r")
key = fa.readline().strip()

client = OpenAI(key)

def getSentiment(items : str) -> str:
    # inVal = prompt + items
    global client
    print("Getting sentiment: ", items)
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[
                                                  {"role":"system", "content":prompt},
                                                  {"role":"user", "content":items}
                                              ])
    
    return response.choices[0].message.content
i = 0
for val in commentVals:
    sentiments = getSentiment(val)
    i += 1
    fa = open(f"../data/sentiments/sentiments{i}.csv", "w")
    fa.writelines(sentiments)