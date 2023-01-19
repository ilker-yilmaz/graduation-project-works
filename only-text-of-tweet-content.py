import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list2 = []  # Creating list to append tweet data to
# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
    # change the search term here
    sntwitter.TwitterSearchScraper('Fırat Üniversitesi').get_items()):
    print(i)  # print the number of tweets for debugging
    if i > 50000:
        break
    tweets_list2.append([tweet.content])  # change the columns here

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Text'])

# write to csv the dataframe
tweets_df2.to_csv('trial-dataset.csv', index=False)
# 20:40 - 21:12 49889 tweets scraped


