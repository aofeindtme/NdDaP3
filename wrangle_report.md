# Data Wrangling Report
### Project 3 - Udacity Data Analyst Nanodegree
## Data Source (Gathering)
 - Twitter Archive from WeRateDogs sent to Udacity via email from WeRateDogs and stored as `twitter-archve-enhanced.csv` inside my Project Workspace at Udacity
 - Image prediction table with dog breed classification processed by a neural network and stored as `image_predictions.tsv` inside my Project Workspace at Udacity
 - Every Tweets retweet count and "like" count stored as `tweet_json.txt` extracted via the Twitter API and stored inside my Project Workspace at Udacity 
## Investigation (Assessing)
For assessing the data I spend a lot of time in coding and experimenting to create a script that provides the following points:
 - Reproducibility for future investigations with a minimum of new coding
 - Availability without running the script again (I couldn't get this solved in the Udacity Worspace, only in my own enviroment on Github with a native .py file)
 - Clarity

~~To provide the 2nd point I let the code extract a markdown and HTML time each during runtime.
The files are named `assessing.html` and `assessing.md` and also stored inside my Project Workspace at Udacity.~~

I load the data sources in separat DataFrames and run code to provide the possibilities for a visual and a programmatical assement. Based on the outputs I found the following tidiness and quality issues concerning the data.

 1. Noteable quality issue - **wrd_archive** `source` multiple values combined in one column
 <img width="852" alt="image" src="https://user-images.githubusercontent.com/79275883/200127508-46a78a99-daf6-4630-9e6f-c1ea2df22088.png">

 2. Noteable quality issue - **wrd_archive** Categorical variables for dog ages are represented as separate columns `doggo`, `floofer`, `pupper`and `puppo`
 <img width="727" alt="image" src="https://user-images.githubusercontent.com/79275883/200125158-339961f4-0a2e-4486-851f-71285d077099.png">

 3. Noteable tidiness issue - **wrd_archive** `retweeted_status_id`, `retweeted_status_user_id`and `retweeted_status_timestamp` mark not necessary observations of uninterested reply rows
 ![image](https://user-images.githubusercontent.com/79275883/200128906-255667e5-baeb-4aa0-a970-3bc00899bcba.png)

 4. Noteable tidiness issue - **wrd_archive** `in_reply_to_status_id`, `in_reply to_user_id`, `retweeted_status_id`, `retweeted_status_user_id`and `retweeted_status_timestamp` not interesting for further analyse
 <img width="1412" alt="image" src="https://user-images.githubusercontent.com/79275883/200125169-6241739d-1ca8-4b5a-ab3a-6b09f6baa631.png">

 5. Noteable quality issue - **wrd_archive** `tweet_id` Type *int64* instead of *string*
 <img width="576" alt="image" src="https://user-images.githubusercontent.com/79275883/200125177-7e6960d1-62b0-409d-9ed8-ed41e8c17cd0.png">
 
 6. Noteable quality issue - **wrd_archive** `timestamp`Type *object* instead of *timestamp*
 <img width="534" alt="image" src="https://user-images.githubusercontent.com/79275883/200125318-a614c241-304d-4dbd-8e2d-6dcdde49e6ae.png">
 
 7. Noteable quality issue - **wrd_archive** `rating_numerator` inaccurate values
 <img width="977" alt="image" src="https://user-images.githubusercontent.com/79275883/200125462-b19107c1-9ecf-433a-a52e-54c89674173c.png">

 8. Noteable quality issue - **wrd_archive** `rating_denominator` inaccurate values != 10
 <img width="657" alt="image" src="https://user-images.githubusercontent.com/79275883/200125785-3b6ab12c-d5ea-42da-bf55-e79664547321.png">

 9. Noteable tidiness issue - **wrd_archive** `expanded urls` sometimes more than one value
 <img width="1208" alt="image" src="https://user-images.githubusercontent.com/79275883/200126525-c583c69e-8c9a-4d92-a795-f13392beba43.png">
 
 10. Noteable tidiness issue - **wrd_archive** `name` invalid names or non-names
 <img width="262" alt="image" src="https://user-images.githubusercontent.com/79275883/200126658-1d8cd211-e3c7-457f-af1f-5f8c4fa96301.png">

 11. Noteable tidiness issue - **wrd_archive** `text` ‘&’ and ‘\n’ in (sub)strings
 <img width="904" alt="image" src="https://user-images.githubusercontent.com/79275883/200126851-d47afade-187a-4cda-b290-9afdbaabb263.png">
 
 12. Noteable quality issue - **wrd_image_prediction** `p1_conf`, `p2_conf` and `p3_conf` FALSE in all of these columns
 <img width="924" alt="image" src="https://user-images.githubusercontent.com/79275883/200127060-685ce3f6-ed56-45c2-99e7-5e8c11071d31.png">

 13. Noteable quality issue - **wrd_image_prediction** `p1`, `p2` and `p3` one prediction data with TRUE and the highest confidence value is enough
 <img width="711" alt="image" src="https://user-images.githubusercontent.com/79275883/200127300-d52fdc1d-9522-4ec5-8474-c0962a4bdfb9.png">

 14. Noteable quality issue - **wrd_archive**, **wrd_image_prediction** and **wrd_archive_add** `tweet_id` is a duplicate column
 <img width="482" alt="image" src="https://user-images.githubusercontent.com/79275883/200127903-bef1e2a5-3540-4da5-9f66-8454e6ed67ea.png">
 
 15. Noteable tidiness issue - **wrd_image_prediction** `p1`, `p2`and `p3` have underlines in strings of Dog race column
 <img width="863" alt="image" src="https://user-images.githubusercontent.com/79275883/200128030-6796008d-83a1-48b0-8765-029865957771.png">

 16. Noteable tidiness issue - **wrd_image_prediction** `p1`, `p2`and `p3` not capitalized
 <img width="896" alt="image" src="https://user-images.githubusercontent.com/79275883/200128172-50441421-d1cc-4dda-ad82-b1f8e4da984c.png">

## Cleaning
In the first steps I created copies of the DataFrames before iterating over the given steps `Define`, `Code` and `Test`. I solved the issues under the choosen points and saved the cleaned DataFrames merged in a requested Master-DataFrame.
