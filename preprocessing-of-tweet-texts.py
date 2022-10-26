import re
import pandas as pd

df = pd.read_csv('datasets/hepsiburada-gittigidiyorin11-trendyol-2022-10-19/n11-2022-10-19.csv')  # read the csv file

df['Text'] = df['Text'].str.replace('#\S+', '',regex=True)  # delete hashtags
df['Text'] = df['Text'].str.replace('@\S+', '',regex=True)  # delete mentions
df['Text'] = df['Text'].str.replace('https\S+|www.\S+', '', case=False, regex=True)  # delete urls
df['Text'] = df['Text'].str.replace('http\S+|www.\S+', '', case=False, regex=True)  # delete urls http
df['Text'] = df['Text'].str.replace(r'\d+', '', regex=True)  # delete numbers
df['Text'] = df['Text'].str.replace('[^\w\s]', '', regex=True)  # delete punctuation
df['Text'] = df['Text'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE, regex=True)  # delete emojis
df['Text'] = df['Text'].str.lower()  # convert to lowercase
# delete datetime, tweet id, username
df = df.drop(['Datetime', 'Tweet Id', 'Username'], axis=1)
# add to new column for all rows. name of the column is ''
df['n11'] = 'n11'

df.to_csv('datasets/preprocessed-n11-2022-10-19.csv', index=False)  # write to csv the dataframe

# rastgele seçilen 1000 tweet'i yeni bir csv dosyasına yazdırma
#
# import pandas as pd
# import random
#
# df = pd.read_csv('datasets/preprocessed-n11-2022-10-19.csv')  # read the csv file
#
# # rastgele seçilen 1000 tweet'i yeni bir csv dosyasına yazdırma
# df = df.sample(n=10000, random_state=1)
# df.to_csv('datasets/1000-preprocessed-n11-2022-10-19-1000.csv', index=False)  # write to csv the dataframe