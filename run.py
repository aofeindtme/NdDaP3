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
import io
import tweepy
from IPython.display import (  # To write (have) code and markdown in the same cell
    Markdown,
    display,
)
from pandas.api.types import is_numeric_dtype, is_object_dtype

# Load csv into df
wrd_archive = pd.read_csv("twitter-archive-enhanced.csv")

# View head of df
wrd_archive.head()

# Fetch tsv file from Udactiy server
url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
response = requests.get(url)
with open(url.split('/')[-1], mode='wb') as file:
    file.write(response.content)
    
# Load downloaded tsv file into df
wrd_image_prediction = pd.read_csv('image-predictions.tsv', sep = '\t')

# View head of df
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
                f.write_(str(count) + '_' + str(tweet_id))
                count +=1
            except Exception as e:
                f.write_(str(count) + '_' + str(tweet_id) + str(e))
                tweet_id_errors[str(count) + '_' + str(tweet_id)] = tweet._json
                count +=1
    end = timer()
    f.write_('Elapsed Time:' + str(end-start))

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

# Top five rows of df
wrd_archive_add.head()

dfs = {'wrd_archive' : wrd_archive,
       'wrd_image_prediction' : wrd_image_prediction,
       'wrd_archive_add':wrd_archive_add
      }

def visual(df, string_name, f):
    head = df.head().to_html()
    tail = df.tail().to_html()
    samples = df.sample(25).to_html()

    f.write(f'<h3>{string_name}')

    f.write('<div style="tableflow">')
    f.write(f'<h4>A. Head from {string_name}</h4>')
    f.write('<br>')
    f.write(head)
    f.write('<br>')

    f.write(f'<h4>B. Tail from {string_name}</h4>')
    f.write('<br>')
    f.write(tail)
    f.write('<br>')

    f.write(f'<h4>C. 25 samples from {string_name}</h4>')
    f.write('<br>')
    f.write(samples)
    f.write('<br>')
    f.write('</div>')

    

def programmatic(df, string_name, f):
    t_shape = str(df.shape)
    
    buffer = io.StringIO()
    df.info(buf=buffer)
    lines = buffer.getvalue().splitlines()
    t_info  = (pd.DataFrame([x.split() for x in lines[5:-2]], columns=lines[3].split())
           .drop('Count',axis=1)
           .rename(columns={'Non-Null':'Non-Null Count'})).to_html()

    t_isnull = pd.DataFrame(df.isnull().sum()).to_html()
    t_dupli = str(sum(df.duplicated()))
    t_describe = pd.DataFrame(df.describe()).to_html()
    t_nunique = pd.DataFrame(df.nunique()).to_html()
    
    f.write(f'<h3>{string_name}')

    f.write('<div style="tableflow">')
    f.write(f'<h4>D. Shape from {string_name}</h4>')
    f.write('<br>')
    f.write(t_shape)
    f.write('<br>')

    f.write(f'<h4>E. Info from {string_name}</h4>')
    f.write('<br>')
    f.write(t_info)
    f.write('<br>')

    f.write(f'<h4>F. isnull sum from {string_name}</h4>')
    f.write('<br>')
    f.write(t_isnull)
    f.write('<br>')

    f.write(f'<h4>G. Duplicates from {string_name}</h4>')
    f.write('<br>')
    f.write(f'<small>The DataFrame {string_name} has {t_dupli} duplicates</small>')
    f.write('<br>')

    f.write(f'<h4>H. Describe from {string_name}</h4>')
    f.write('<br>')
    f.write(t_describe)
    f.write('<br>')
   
    f.write(f'<h4>I. Nunique from {string_name}</h4>')
    f.write('<br>')
    f.write(t_nunique)
    f.write('<br>')

    f.write(f'<h4>J. Duplicates per column from {string_name}</h4>')
    for i, col in zip(df.dtypes, df):
        s = str(sum(df[col].duplicated()))
        f.write('<br>')
        f.write(f'<small>Sum of duplicates in {col} = {s} {i}</small>')

    f.write(f'<h4>K. Sorted numeric values per column in {string_name}</h4>')
    for i, col in zip(df.dtypes, df):
        f.write(f'<h5>Sorted numeric values per column in {col}</h5>')
        if is_numeric_dtype(df[col]):
            num = np.sort(df[col].unique())
            df_num = pd.DataFrame(num)
            num_sorted = df_num.to_html()
            if len(df_num) <= 50:
                f.write(num_sorted)
            else:
                f.write('too long to display')
            f.write('<br>')
        else:
            substring = str(col)
            f.write(f'<small>{substring}, is not numeric</small>')

    f.write(f'<h4>L. Check which column is object type from {string_name}</h4>')
    for i, col in zip(df.dtypes, df):
        f.write('<br>')        
        if is_object_dtype(df[col]):
            f.write(str(col) + ' is '  + str(i))
        else:
            f.write(str(col) +  ' is not')

    f.write(f'<h4>M. Count different values per column from {string_name}</h4>')
    for i, col in zip(df.dtypes, df):
        f.write('<br>') 
        f.write(str(col))
        f.write('<br')
        num = np.sort(df[col].value_counts())
        df_num = pd.DataFrame(num)
        num_sorted = df_num.to_html()
        f.write(num_sorted)
    f.write('</div>')

title_text = "Data Assessment"
v_text = "Visual Assessment"
p_text = "Programmatic Assessment"
with open('assessment.html', 'a') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<link rel="stylesheet" href="DataFrameStyle.css">\n')
    f.write('<title>{page_title_text}</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write(f'<h1>{title_text}</h1>\n')
    f.write(f'<h2>{v_text}</h2>\n')
    for k, v in dfs.items():
        visual(v, k, f)
    f.write('<br>')
    f.write(f'<h2>{p_text}</h2>')
    for k, v in dfs.items():
        programmatic(v, k, f)
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>')

print(wrd_archive.value_counts())

# Make copies of original pieces of data
wrd_archive_clean = wrd_archive.copy()
wrd_image_prediction_clean = wrd_image_prediction.copy()
wrd_archive_add_clean = wrd_archive_add.copy()


