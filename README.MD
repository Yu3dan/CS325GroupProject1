# Reddit Comment Sentiment Analysis
### CS325 Group Project 3 (Project 6)

This project is focused on using Python to convert multiple Reddit pages given by user in a text file, filtering out the comments of each post and giving a sentiment anaylsis in a final text file and also graphically showing the difference in sentiments in a bar graph for each URL.

If you are interested in using our code above, the first thing you must do is clone this repository by using this command in your terminal:

```
git clone https://github.com/Yu3dan/CS325GroupProject1
```

Once you have done this, make sure you are in the correct directory the repository (and its content) was downloaded to using cd (file location) in your terminal.

The requirements.yaml file included is all the neccesary libraries in the environment we coded this project under while using miniconda.
In order to use the packages needed to run this program, you must create a new environment using the .yaml file given. Before you do this, you must remember to deactivate your current environment using

```
conda deactivate
```

The command to create the new environment is:

```
conda create --name my_yaml_env --file requirements.yaml
```

My_yaml_env would be the name of the new environment in that instance (You may use any name you would like to). Next, activate the new environment with the commmand:

```
conda activate my_yaml_env
```
Once your environment is set up correctly, you must follow a few steps: 

1: Any Reddit URL you want to use, you must replace each "www" in the reddit URLs to "old".
Example: 
https://old.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/
VS
https://www.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/

2: Each URL in the text file used to run the program must be seperated by an empty line, but make sure there are none inbetween. For example the text file should look like this:

https://old.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/
https://old.reddit.com/r/OnePiece/comments/17hq7g9/no_one_hates_kaido_more_than_moria/
https://old.reddit.com/r/OnePiece/comments/17hjder/new_admirals_figurines/

Note: Make sure the cursor ends at the last / of the URL given. If there is an empty line(s) after the URLs you pasted into the text file there will be an error given because it doesn't recognized an empty space as a URL.

There is a limit on how many sentiment anaylsis you are able to run, if you run too many URL's with a lot of comments, you will recieve errors on the sentiment analysis portion however the comments will print properly.

Next, you must give the program your Google Bard cookies, PSID, PSIDCC, and PSIDTS. To get these values (in Firefox), you open bard.google.com, inspect, navigate to storage, click cookies, and copy the data from __Secure-1PSID, __Secure-1PSIDCC, __Secure-1PSIDTS to their respective files in module_4.

Now, the syntax to run this program is: (the name of the text file containing all the Reddit URL's I created are listOfURLS.txt)

```
python run.py listOfURLs.txt
```

The output of this part of the project should be text files where all comments of each post are filtered is under the folder Data and subfolder processed. 
If ran correctly, you should multiple text files named numerically according to what order you had the links in the text file. Along with this there will be a Sentiments subfolder under the data folder that contains .csv files with all of the sentiment analysis of each adjusted post in order. You will be able to see any sentiment of each comment in order whether it is a 'Positive', 'Negaitve', or 'Neutral' comment.

The last part of this project is to be able to graphically see the difference in each sentiment for each URL provided. In order to do this, you must run the command:

```
python plot.py
```

Stored under the plots subfolder of data, there will be multiple graphs depending on how many URL's you provided in the text file. These graphs will show the different number of sentiments in each Reddit post and you will easily be able to compare the number of positive, negative, and neutral sounding comments.

If you want to remove any of the URLs provided and add your own, just make sure you follow the syntax in step 2.

If you would like to edit or change the URL's with no errors, the best way to do so is delete or store all the text/csv files and graphs in the data folder somewhere else so new ones can be written without issue.
