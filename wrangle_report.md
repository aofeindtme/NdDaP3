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

#### 1. Noteable tidiness issue - Source saved in HTML Format
<img width="1132" alt="image" src="https://user-images.githubusercontent.com/79275883/200114118-eb86723c-dc0d-4845-b10f-1d3d16be83ec.png">

#### 2. Noteable quality issue - Dog ages spread over columns
<img width="722" alt="image" src="https://user-images.githubusercontent.com/79275883/200114289-a3b3398b-842b-4896-8dbb-9a9298576f06.png">

#### 3. Noteable tidiness issue - Columns not interesting for further analyse
<img width="671" alt="image" src="https://user-images.githubusercontent.com/79275883/200114491-99897b03-50ce-4cd2-b84e-bde030a997f5.png">



### Noteable quality issues observating the given files
### Noteable tidiness issues observating the given files
## Cleaning
