import re
import pandas as pd

df = pd.read_csv('trial-dataset.csv')  # read the csv file

df['Text'] = df['Text'].str.replace('#\S+', '',regex=True)  # delete hashtags
df['Text'] = df['Text'].str.replace('@\S+', '',regex=True)  # delete mentions
df['Text'] = df['Text'].str.replace('https\S+|www.\S+', '', case=False, regex=True)  # delete urls
df['Text'] = df['Text'].str.replace('http\S+|www.\S+', '', case=False, regex=True)  # delete urls http
df['Text'] = df['Text'].str.replace(r'\d+', '', regex=True)  # delete numbers
df['Text'] = df['Text'].str.replace('[^\w\s]', '', regex=True)  # delete punctuation
df['Text'] = df['Text'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE, regex=True)  # delete emojis
df['Text'] = df['Text'].str.lower()  # convert to lowercase

df.to_csv('trial-dataset.csv', index=False)  # write to csv the dataframe
