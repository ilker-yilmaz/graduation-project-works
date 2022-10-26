from matplotlib import pyplot as plt
from textblob import TextBlob
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv('datasets/preprocessed-h-g-n-t/preprocessed-n11-2022-10-19.csv')  # read the csv file

# create a function to get the subjectivity

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


# create a function to get the polarity

def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# create two new columns 'Subjectivity' & 'Polarity'

df['Subjectivity'] = df['Text'].apply(get_subjectivity)
df['Polarity'] = df['Text'].apply(get_polarity)

# show the new dataframe with the new columns

print(df)

# plot the Word Cloud

allWords = ' '.join([twts for twts in df['Text']])
wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(allWords)

plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()

# create a function to compute negative (-1), neutral (0) and positive (+1) analysis

def get_analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

df['Analysis'] = df['Polarity'].apply(get_analysis)

# show the dataframe

print(df)

# print all of the positive tweets

j = 1
sortedDF = df.sort_values(by=['Polarity'])
for i in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][i] == 'Positive'):
        print(str(j) + ') ' + sortedDF['Text'][i])
        print()
        j = j + 1

# print all of the negative tweets

j = 1
sortedDF = df.sort_values(by=['Polarity'], ascending='False')
for i in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][i] == 'Negative'):
        print(str(j) + ') ' + sortedDF['Text'][i])
        print()
        j = j + 1

# plot the polarity and subjectivity

plt.figure(figsize=(8, 6))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

# get the percentage of positive tweets

ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Text']

round((ptweets.shape[0] / df.shape[0]) * 100, 1)

# get the percentage of negative tweets

ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets['Text']

round((ntweets.shape[0] / df.shape[0]) * 100, 1)

# show the value counts

df['Analysis'].value_counts()

# plot and visualize the counts

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()

