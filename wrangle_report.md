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

 1. Noteable tidiness issue - Source saved in HTML Format
 <img width="1137" alt="image" src="https://user-images.githubusercontent.com/79275883/200125151-e64c4a99-6ec6-4fc9-9b32-b63bb2be53a8.png">

 2. Noteable quality issue - Categorical variables for dog ages are represented as separate columns
 <img width="727" alt="image" src="https://user-images.githubusercontent.com/79275883/200125158-339961f4-0a2e-4486-851f-71285d077099.png">

 3. Noteable tidiness issue - Columns not interesting for further analyse
 <img width="1412" alt="image" src="https://user-images.githubusercontent.com/79275883/200125169-6241739d-1ca8-4b5a-ab3a-6b09f6baa631.png">

 4. Noteable quality issue - `tweet_id Type *int64* instead of *string*
 <img width="576" alt="image" src="https://user-images.githubusercontent.com/79275883/200125177-7e6960d1-62b0-409d-9ed8-ed41e8c17cd0.png">

## Cleaning
