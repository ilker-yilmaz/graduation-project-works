import re
import pandas as pd

df = pd.read_csv('tweets_df3.csv')  # read the csv file

df['Text'] = df['Text'].str.replace('#\S+', '')  # delete hashtags
df['Text'] = df['Text'].str.replace('@\S+', '')  # delete mentions
df['Text'] = df['Text'].str.replace('https\S+|www.\S+', '', case=False)  # delete urls
df['Text'] = df['Text'].str.replace(r'\d+', '', regex=True)  # delete numbers
df['Text'] = df['Text'].str.replace('[^\w\s]', '', regex=True)  # delete punctuation
df['Text'] = df['Text'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)  # delete emojis

df.to_csv('tweets_df3.csv', index=False)  # write to csv the dataframe
