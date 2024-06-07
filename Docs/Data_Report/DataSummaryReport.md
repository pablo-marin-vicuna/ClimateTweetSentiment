# Data Report
This file will be generated for each data file received or processed. The Interactive Data Exploration, Analysis, and Reporting (IDEAR) utility developed by TDSP team of Microsoft can help you explore and visualize the data in an interactive way, and generate the data report along with the process of exploration and visualization. 

IDEAR allows you to output the data summary, statistics, and charts that you want to use to tell the data story into the report. You only need to click a few buttons, and the report will be generated for you. 

## General summary of the data

[Twitter Climate Change Sentiment Dataset](https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset) contains 43.943 annotated tweets from Apr 27, 2015 to Feb 21, 2018. The tweets were annotated by 3 reviewers that agreed on their labeling. The collection of this data was funded by a Canada Foundation for Innovation JELF Grant to Chris Bauch, University of Waterloo.

Details of this summary can be seen in [exploratory.ipynb](/Code/Data_Acquisition_and_Understanding/exploratory.ipynb)

The dataset contains three features:
- Sentiment: anti (-1), neutral (0), pro (1), news (2)
- message: text containing tweet
- tweetid: identifier, which can also be used to determine post datetime


## Data quality summary

All features are "clean". There are no missing values or any out of range values in the raw features.


## Target variable

The target variable variable is Sentiment. 

| ID  | Sentiment | Sentiment Description                                             | N      | %      |
|-----|-----------|-------------------------------------------------------------------|--------|--------|
| -1  | Anti      | The tweet does not believe in man-made climate change             | 3,990  | 9.08%  |
| 0   | Neutral   | The tweet neither supports nor refutes the belief of man-made climate change | 7,715  | 17.56% |
| 1   | Pro       | The tweet supports the belief of man-made climate change          | 22,962 | 52.25% |
| 2   | News      | The tweet links to factual news about climate change              | 9,276  | 21.11% |
|     | **Total** |                                                                   | 43,943 | 100.00%|


## Individual variables

Two raw features are available as independent variables: 'tweetid' and 'message'. Additional feature will be generated from those such as datetime, tweet length and word counts.

### 1. tweetid (datetime)
Tweetid is the identifier which can also be converted to datetime. Additional date features were added such as date, year, month, day, year_month and dayofweek. A summary of tweets per year and min and max dates: 

|   year |   count | min_date   | max_date   |
|-------:|--------:|:-----------|:-----------|
|   2015 |    3545 | 2015-04-27 | 2015-12-31 |
|   2016 |   14075 | 2016-01-01 | 2016-12-31 |
|   2017 |   19223 | 2017-01-01 | 2017-12-31 |
|   2018 |    7100 | 2018-01-01 | 2018-02-22 |

### 2. message

Message contains the text of the tweet. Additional features were generated such as the lenght of tweets and word counts.

A summary of the length of tweets:

| length_range   |   count |
|:---------------|--------:|
| [1.0, 21.0)    |       7 |
| [21.0, 41.0)   |     305 |
| [41.0, 61.0)   |     896 |
| [61.0, 81.0)   |    2294 |
| [81.0, 101.0)  |    4423 |
| [101.0, 121.0) |    6958 |
| [121.0, 141.0) |   20291 |
| [141.0, 161.0) |    8712 |
| [161.0, 181.0) |      42 |
| [181.0, inf)   |      15 |

The top 20 words by count (excluding stopwords):

| word    |   count |
|:--------|--------:|
| climate |   33325 |
| rt      |   25265 |
| change  |   24169 |
| global  |   10477 |
| warming |    7183 |
| trump   |    3535 |
| believe |    2293 |
| us      |    1580 |
| via     |    1557 |
| new     |    1485 |

## Variable ranking

Analysis to be performed during modeling.

## Relationship between explanatory variables and target variable

Count of Sentiment vs. Year (Percentage of Total Rows):
|   year |   -1 |    0 |    1 |    2 |
|-------:|-----:|-----:|-----:|-----:|
|   2015 | 0.13 | 0.22 | 0.41 | 0.24 |
|   2016 | 0.08 | 0.16 | 0.58 | 0.18 |
|   2017 | 0.09 | 0.16 | 0.5  | 0.25 |
|   2018 | 0.09 | 0.24 | 0.53 | 0.14 |

Count of Sentiment vs. Length of Tweet (Percentage of Total Rows):
| length_bin     |   -1 |    0 |    1 |    2 |
|:---------------|-----:|-----:|-----:|-----:|
| [0.0, 20.0)    | 0    | 1    | 0    | 0    |
| [20.0, 40.0)   | 0.08 | 0.76 | 0.16 | 0    |
| [40.0, 60.0)   | 0.12 | 0.59 | 0.26 | 0.03 |
| [60.0, 80.0)   | 0.08 | 0.43 | 0.36 | 0.13 |
| [80.0, 100.0)  | 0.08 | 0.23 | 0.37 | 0.31 |
| [100.0, 120.0) | 0.08 | 0.15 | 0.41 | 0.36 |
| [120.0, 140.0) | 0.09 | 0.14 | 0.54 | 0.23 |
| [140.0, 160.0) | 0.1  | 0.14 | 0.64 | 0.12 |
| [160.0, 180.0) | 0.12 | 0.12 | 0.64 | 0.11 |
| [180.0, 200.0) | 0    | 0.09 | 0.91 | 0    |
| [200.0, inf)   | 0    | 0.71 | 0.29 | 0    |


