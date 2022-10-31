# Load libraries
import json
import os
from timeit import default_timer as timer
from mdutils.mdutils import MdUtils
from mdutils import Html
import numpy as np
import pandas as pd
import requests
import tabulate
import tweepy
from IPython.display import (  # To write (have) code and markdown in the same cell
    Markdown,
    display,
)
from pandas.api.types import is_numeric_dtype, is_object_dtype

# Load csv into dataframe
wrd_archive = pd.read_csv("twitter-archive-enhanced.csv")

# View head of dataframe
wrd_archive.head()

# Fetch tsv file from Udactiy server
url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
response = requests.get(url)
with open(url.split('/')[-1], mode='wb') as file:
    file.write(response.content)
    
# Load downloaded tsv file into dataframe
wrd_image_prediction = pd.read_csv('image-predictions.tsv', sep = '\t')

# View head of dataframe
wrd_image_prediction.head()

# Fetch the data from Twitter if you haven't done it already... because it can take 20 - 30 minutes
file_name = 'tweet_json.txt'
if not os.path.isfile(file_name):
    
    consumer_key = 'jK#######################JQ'
    consumer_secret = 'QZ#######################MX'
    access_token = '62#######################oJ'
    access_secret = 'Gr#######################nZ'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

    # Getting tweet details for a single tweet_id from the twitter archive
    tweet = api.get_status(	892420643555336193, tweet_mode = 'extended' )

    # Viewing the json data
    tweet._json

    # Verifying the presence of retweet count of tweet_id in json data
    tweet._json['retweet_count']

    # Verifying the presence of favorite count of tweet_id in json data
    tweet._json['favorite_count']

    # Creating file
    open(file_name, 'w').close()

    # Query Twitter's API for JSON data for each tweet ID in the Twitter archive & writing twitter json data to tweet_json.txt file
    tweet_id_errors = {}
    count = 0
    start = timer()
    with open(file_name, mode = 'w') as file:
        for tweet_id in wrd_archive.tweet_id:
            try:
                tweet = api.get_status(tweet_id, tweet_mode='extended')
                file.write(json.dumps(tweet._json) + '\n')
                mdFile.new_(str(count) + '_' + str(tweet_id))
                count +=1
            except Exception as e:
                mdFile.new_(str(count) + '_' + str(tweet_id) + str(e))
                tweet_id_errors[str(count) + '_' + str(tweet_id)] = tweet._json
                count +=1
    end = timer()
    mdFile.new_('Elapsed Time:' + str(end-start))

    # Reading twitter json data from tweet_json.txt file by converting each json string into python dictionary
# and appending them to a list (row by row) and this list of dictionaries will eventually be converted to a pandas DataFrame 

df_list = []
with open('tweet_json.txt', mode = 'r') as file:
    for row in file.readlines():
        tweet_dict = json.loads(row)
        retweet_count = tweet_dict['retweet_count']
        favorite_count = tweet_dict['favorite_count']
        tweet_id = tweet_dict['id']
        df_list.append({'tweet_id': tweet_id, 
                        'retweet_count': retweet_count, 
                        'favorite_count': favorite_count})  

# Creating DataFrame from list of dictionaries
wrd_archive_add = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count', 'favorite_count'])

# Top five rows of dataframe
wrd_archive_add.head()

def create_md_table(df):
    columns = len(df.columns)
    rows = len(df)+1

    a = df.columns.values.tolist()
    b = df.values.tolist()

    b.insert(0, a)
    c = [item for sublist in b  for item in sublist]
    return columns, rows, c

def visual(dataframe, string_name, f):
    mdFile.new_header(level=3, title="A. Head from " + str(string_name), add_table_of_contents='n')
    
    df = dataframe.head(5)
    
    mdFile.new_line()
    columns, rows, text = create_md_table(df)
    mdFile.new_table(columns=columns, rows=rows, text=text, text_align='center')

    df = dataframe.tail(5)
    
    mdFile.new_line()
    columns, rows, text = create_md_table(df)
    mdFile.new_table(columns=columns, rows=rows, text=text, text_align='center')

    df = dataframe.sample(n=25)
    
    mdFile.new_line()
    columns, rows, text = create_md_table(df)
    mdFile.new_table(columns=columns, rows=rows, text=text, text_align='center')


def programmatic(dataframe, string_name, f):
    mdFile.new_header(level=3, title = "D. Shape from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")
    #mdFile.new_(dataframe.shape.to_string())
    mdFile.new_header(level=3, title = "E. Info from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")

    #mdFile.new_(dataframe.info().to_string(header=False, index=False))
    mdFile.new_header(level = 3, title = "F. isnull sum from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")
    mdFile.new_paragraph(dataframe.isnull().sum().to_string(header=False, index=False))

    mdFile.new_header(level = 3, title = "G. Duplicates from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")
    mdFile.new_paragraph(str(sum(dataframe.duplicated())))
    mdFile.new_header(level = 3, title = "H. Describe from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")
    mdFile.new_paragraph(dataframe.describe().to_string(header=False, index=False))
    mdFile.new_header(level = 3, title = "I. Nunique from " + str(string_name), add_table_of_contents='n')
    mdFile.new_line("")
    mdFile.new_paragraph(dataframe.nunique().to_string(header=False, index=False))

    mdFile.new_header(level = 3, title = "J. Duplicates per column from " + str(string_name), add_table_of_contents='n')
    for i, col in zip(dataframe.dtypes, dataframe):
        mdFile.new_line("")
        mdFile.new_paragraph(
            "Sum of duplicates in {col} = "
            + str(sum(dataframe[col].duplicated()))
            + str(i)
        )

    mdFile.new_header(level = 3, title = "K. Sorted numeric values per column in " + str(string_name), add_table_of_contents='n')
    for i, col in zip(dataframe.dtypes, dataframe):
        mdFile.new_line("")
        mdFile.new_header(level = 4, title = "Sorted numeric values per column in " + str(col), add_table_of_contents='n')

        if is_numeric_dtype(
            dataframe[col]
        ):
            mdFile.new_paragraph(str(np.sort(dataframe[col].unique())))
        else:
            mdFile.new_paragraph(str(col) + " is not numeric")

    mdFile.new_header(level = 3, title = "L. Check which column is object type from " + str(string_name), add_table_of_contents='n')
    for i, col in zip(dataframe.dtypes, dataframe):
        mdFile.new_line("")
        if is_object_dtype(dataframe[col]):
            mdFile.new_paragraph(str(col) + 'is'  + str(i))
        else:
            mdFile.new_paragraph(str(col) +  'is not')

    mdFile.new_header(level = 3, title = "M. Count different values per column from " + str(string_name), add_table_of_contents='n')
    
    for i, col in zip(dataframe.dtypes, dataframe):
        mdFile.new_line("")
        mdFile.new_paragraph(str(col))
        #mdFile.new_(dataframe[col].value_counts())


dfs = {'wrd_archive' : wrd_archive,
       'wrd_image_prediction' : wrd_image_prediction,
       'wrd_archive_add':wrd_archive_add
      }

f = open('test.md','w+')

mdFile = MdUtils(file_name='DataAssessment', title='Data Assessment')



for k, v in dfs.items():
    
    mdFile.new_header(level=2, title= str(k) + ' - Visual Assessment', add_table_of_contents='n') 
    visual(v, k, mdFile)

    mdFile.new_header(level=2, title = str(k) + ' - Programmatic Assessment', add_table_of_contents='n')
    programmatic(v, k, mdFile)
    mdFile.new_line("")


# 1. Set up multiple variables to store the titles, text within the report
page_title_text='My report'
title_text = 'Scrollable table'
text = 'Hello, welcome to your Scrollable table test!'
prices_text = 'Twitter Data'

# 2. Combine them together using a long f-string
html = f'''

            <html>
                <head>
                <link rel="stylesheet" href="DataFrameStyle.css">

                    <title>{page_title_text}</title>
                </head>
                <body>
                    <h1>{title_text}</h1>
                    <p>{text}</p>
                    <h2>{prices_text}</h2>
                    <div style="overflow-x:auto; overflow-y:auto; width: 98%; height: 50%;">

                    {wrd_archive.to_html()}
                    
                    </div>
                    <h2>{prices_text}</h2>
                    <h2>{prices_text}</h2>
                </body>

            </html>
 
    '''
# 3. Write the html string as an HTML file
with open('html_report.html', 'w') as f:
    f.write(html)

mdFile.create_md_file()
# Make copies of original pieces of data
wrd_archive_clean = wrd_archive.copy()
wrd_image_prediction_clean = wrd_image_prediction.copy()
wrd_archive_add_clean = wrd_archive_add.copy()


