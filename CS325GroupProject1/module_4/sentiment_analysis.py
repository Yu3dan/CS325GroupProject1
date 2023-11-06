from openai import OpenAI
prompt = "I am going to send you a series of comments, give me the sentiment analysis for each of the following comments in order. Do not explain the sentiment, do not add any extra information. Only separate the sentiments by a new line.\n"
# Use the prompt and add the lines
"""A test"""

# Create the client for chatGPT
global client

fa = open("./module_4/apiKey.txt", "r")
key = fa.readline().strip()

client = OpenAI(api_key= key)

def getSentiment(items : str) -> str:
    # inVal = prompt + items
    global client
    print("Getting sentiment: ", items)
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[
                                                  {"role":"system", "content":prompt},
                                                  {"role":"user", "content":items}
                                              ])
    return response['choices'][0]['message']['content']
