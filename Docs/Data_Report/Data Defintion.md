# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

<!--
For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

When applicable, the Interactive Data Exploration, Analysis, and Reporting (IDEAR) utility developed by Microsoft is applied to explore and visualize the data, and generate the data report. Instructions of how to use IDEAR can be found [here](). 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_
-->

## Raw Data Sources


| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Twitter Climate Change Sentiment Datset | Kaggle: [Twitter Climate Change Sentiment Dataset](https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset) | Dataset available : [twitter_sentiment_data.csv](/Sample_Data/Raw/twitter_sentiment_data.csv)  | Manual download from Kaggle to destination location | [Dataset 1 Report](/Docs/Data_Report/DataSummaryReport.md)|
<!--
| Dataset 2 | Brief description of its orignal location | Brief description of its destination location | [script2.R](link/to/R/script/file/in/Code) | [Dataset 2 Report](link/to/report2)|
-->

### Dataset1 summary

The Twitter Climate Change Sentiment Dataset contains 43,943 tweets collected between April 27, 2015, and February 21, 2018. Each tweet is annotated by three reviewers and classified into one of four sentiment categories: News, Pro, Neutral, and Anti.
- contains 43.943 annotated tweets from Apr 27, 2015 to Feb 21, 2018. 
- 3 features avaibale: sentiment, message, tweetid.

<!--
* Dataset2 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset2 Report.> 
-->

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| processed.csv | [twitter_sentiment_data.csv](/Sample_Data/Raw/twitter_sentiment_data.csv) | [dataPrep.py](/Code/Data_Acquisition_and_Understanding/dataPrep.py) | [Dataset 1 Report](/Docs/Data_Report/DataSummaryReport.md)|

<!--
| Processed Dataset 2 | [Dataset2](link/to/dataset2/report) |[script2.R](link/to/R/script/file/in/Code) | [Processed Dataset 2 Report](link/to/report2)|
-->

* Processed Data1 summary:  the raw dataset features are processed to incorporate additional features:
    - tweetid -> datetime, date, year, month, day, year_month, dayofweek
    - message -> message_length


<!--
* Processed Data2 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data2 Report.> 
-->

## Feature Sets

Feature sets are unique for the moment, equal to the processed data described above. 

<!--
| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
-->