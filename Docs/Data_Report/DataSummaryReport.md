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

All raw features are "clean". There are no missing values or any out of range values in the raw features.

| index   |    sentiment |         tweetid |
|:--------|-------------:|----------------:|
| count   | 43943        | 43943           |
| mean    |     0.853924 |     8.36797e+17 |
| std     |     0.853543 |     8.56851e+16 |
| min     |    -1        |     5.92633e+17 |
| 25%     |     0        |     7.97038e+17 |
| 50%     |     1        |     8.4023e+17  |
| 75%     |     1        |     9.02e+17    |
| max     |     2        |     9.66702e+17 |



## Target variable

The target variable variable is Sentiment. 


- -1: Anti - The tweet does not believe in man-made climate change                   
- 0: Neutral - The tweet neither supports nor refutes the belief of man-made climate   
- 1: Pro - The tweet supports the belief of man-made climate change                
- 2: News - The tweet links to factual news about climate change                    

|   sentiment |   count |   percentage |
|------------:|--------:|-------------:|
|          -1 |    3990 |         0.09 |
|           0 |    7715 |         0.18 |
|           1 |   22962 |         0.52 |
|           2 |    9276 |         0.21 |


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

A barplot of the count of tweets by date shows that many more tweets are available from the last months of 2016 to the beginning of 2018.

![tweets_by_date](/Docs/Data_Report/images/tweets_by_date.png)

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

We observe a high concentration near 140 characters, which is expected for Twitter data which had this limit before 2017. ![tweets_length](/Docs/Data_Report/images/tweet_length.png)

The number of words within a tweet displays a more symmetric distribution, concentrated around 9-10 words.

![word_count](/Docs/Data_Report/images/word_count.png)

The top 10 words by count (excluding stopwords):

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

A wordcloud showcases the relative frequencies of the words visually.

![wordcloud](/Docs/Data_Report/images/wordcloud.png)

Finally, [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) scores were computed and averaged for each tweet. The distribution of these average scores:

![tf_idf_avg](/Docs/Data_Report/images/tf_idf_avg.png)

## Variable ranking

For variable ranking, an initial analysis using information gain is used to understand the relationship between the target variable 'sentiment' and:
- date
- year
- month
- year_month
- message_length
- word_count
- average_tfidf

The top ten features according to this analysis:

| feature            |   information_gain |
|:-------------------|-------------------:|
| average_tfidf      |         1.18721    |
| message_length     |         0.0747682  |
| word_count         |         0.0261843  |
| month              |         0.0131466  |
| year               |         0.0103976  |
| date_2017-03-06    |         0.00937518 |
| year_month_2016-11 |         0.00877167 |
| year_month_2017-03 |         0.00804246 |
| date_2017-12-29    |         0.00791403 |
| date_2017-05-22    |         0.00737934 |


## Relationship between explanatory variables and target variable

A few relationships are analyzed considering some of the relevant features.

Count of Sentiment vs. Average TF-IDF Bins (Percentage of Total Rows):
| tfidf_bin            |   -1 |    0 |    1 |    2 |
|:---------------------|-----:|-----:|-----:|-----:|
| (1.52e-05, 2.09e-05] | 0.1  | 0.67 | 0.21 | 0.01 |
| (2.09e-05, 2.66e-05] | 0.1  | 0.58 | 0.31 | 0.02 |
| (2.66e-05, 3.22e-05] | 0.1  | 0.35 | 0.44 | 0.11 |
| (3.22e-05, 3.79e-05] | 0.09 | 0.21 | 0.46 | 0.24 |
| (3.79e-05, 4.36e-05] | 0.09 | 0.13 | 0.55 | 0.23 |
| (4.36e-05, 4.93e-05] | 0.1  | 0.14 | 0.56 | 0.2  |
| (4.93e-05, 5.5e-05]  | 0.12 | 0.21 | 0.53 | 0.14 |
| (5.5e-05, 6.07e-05]  | 0.05 | 0.82 | 0.13 | 0    |
| (6.07e-05, 6.64e-05] | 0    | 1    | 0    | 0    |

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


