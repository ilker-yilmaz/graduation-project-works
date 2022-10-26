# get tweets from twitter
import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list2 = []  # Creating list to append tweet data to
# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('"@hepsiburada" until:2022-10-19 since:2022-01-01').get_items()):  # change the search term here
    print(i)  # print the number of tweets for debugging
    # if i > 50000:
    #     break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])  # change the columns here

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])  # Creating a dataframe from the tweets list above

tweets_df2.to_csv('hepsiburada-2022-10-19.csv', index=False)  # write to csv the dataframe
