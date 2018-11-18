# ml_assignment
Sentiment analysis
This project has 2 python files
get_sentiment_score.py
topic_identification.py

get_sentiment_score.py uses textblob to get Sentiment score for every pro and con in the file given [glassdoortest1.csv] file
New csv file[sentimentglassdoor.csv] is created with details like year, quater sentiment score for pro, sentiment score for con and overall sentiment scrore for every record
Generate bar chart for Overall Sentiment score
Generate bar chart for Cons Sentiment score
Generate bar chart for Pros Sentiment score

topic_identification.py uses Kmean clustering to cluster Pros and Cons. Picked top 3 clusters and named them as topics
Generate bar chart for Top reason for Positivity [Pros]
Generate bar chart for Top reason for Positivity [Cons]

Steps to run the applicaton
First run get_sentiment_score.py as this creates the CSV file required for topic_identification.py
