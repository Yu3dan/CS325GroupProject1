import os
import regex, re
from module_4 import sentiment_analysis
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
commentVals.append("""""")
i = 0
for file in fileData:
    for val in file:
        # For each comment
        if len(commentVals[i]) + len(val[0]) > 4000:
            # A basic check to see how many tokens this will have taken up. Not accurate but should always be lower than actuality so should be safe
            print(sentiment_analysis.getSentiment(commentVals[i]))
            commentVals.append("""""")
            i += 1
        valLine = val[0] + "\n\n"
        # print("ValLine: ", valLine)
        commentVals[i] += valLine
        
    # print(len(commentVals))
    