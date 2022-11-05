# Data Wrangling Report
### Project 3 - Udacity Data Analyst Nanodegree
## Data Source (Gathering)
 - Twitter Archive from WeRateDogs sent to Udacity via email from WeRateDogs and stored as `twitter-archve-enhanced.csv` inside my Project Workspace at Udacity
 - Image prediction table with dog breed classification processed by a neural network and stored as `image_predictions.tsv` inside my Project Workspace at Udacity
 - Every Tweets retweet count and "like" count stored as `tweet_json.txt` extracted via the Twitter API and stored inside my Project Workspace at Udacity 
## Investigation (Assessing)
For assessing the data I spend a lot of time in coding and experimenting to create a script that provides the following points:
 - Reproducibility for future investigations with a minimum of new coding
 - Availability without running the script again
 - Clarity

To provide these points I let the code extract a markdown and HTML time each during runtime.
The files are named `assessing.html` and `assessing.md` and also stored inside my Project Workspace at Udacity.
### Process
I load the data sources in separat DataFrames and run code to provide the possibilities for a visual and a programmatical assement.

 1. Noteable tidiness issue - **wrd_archive** `source`value stored in HTML Format
 <img width="1137" alt="image" src="https://user-images.githubusercontent.com/79275883/200125151-e64c4a99-6ec6-4fc9-9b32-b63bb2be53a8.png">

 2. Noteable quality issue - **wrd_archive** Categorical variables for dog ages are represented as separate columns `doggo`, `floofer`, `pupper`and `puppo`
 <img width="727" alt="image" src="https://user-images.githubusercontent.com/79275883/200125158-339961f4-0a2e-4486-851f-71285d077099.png">

 3. Noteable tidiness issue - **wrd_archive** `in_reply_to_status_id`, `in_reply to_user_id`, `retweeted_status_id`, `retweeted_status_user_id`and `retweeted_status_timestamp` not interesting for further analyse
 <img width="1412" alt="image" src="https://user-images.githubusercontent.com/79275883/200125169-6241739d-1ca8-4b5a-ab3a-6b09f6baa631.png">

 4. Noteable quality issue - **wrd_archive** `tweet_id` Type *int64* instead of *string*
 <img width="576" alt="image" src="https://user-images.githubusercontent.com/79275883/200125177-7e6960d1-62b0-409d-9ed8-ed41e8c17cd0.png">
 
 5. Noteable quality issue - **wrd_archive** `timestamp`Type *object* instead of *timestamp*
 <img width="534" alt="image" src="https://user-images.githubusercontent.com/79275883/200125318-a614c241-304d-4dbd-8e2d-6dcdde49e6ae.png">
 
 6. Noteable quality issue - **wrd_archive** `rating_numerator` inaccurate values
 <img width="977" alt="image" src="https://user-images.githubusercontent.com/79275883/200125462-b19107c1-9ecf-433a-a52e-54c89674173c.png">

 7. Noteable quality issue - **wrd_archive** `rating_denominator`inaccurate values != 10
 <img width="657" alt="image" src="https://user-images.githubusercontent.com/79275883/200125785-3b6ab12c-d5ea-42da-bf55-e79664547321.png">


## Cleaning
