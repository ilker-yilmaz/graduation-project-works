import pandas as pd

df = pd.read_csv('datasets/big-dataset-preprocessed-2.csv')  # read the csv file

print("Verisetinde hangi kelime kaç defa tekrar ediyor:")
print(df['Text'].str.split(expand=True).stack().value_counts())
# print all words and their frequencies
# for word in df['Text'].str.split(expand=True).stack().value_counts().index:
#     print(word, df['Text'].str.split(expand=True).stack().value_counts()[word])

# save the all words and their frequencies to a csv file
df['Text'].str.split(expand=True).stack().value_counts().to_csv('word-frequencies.csv', index=True, header=True)

#print(df['Text'].str.split(expand=True).stack().value_counts())  # Hangi kelime kaç defa tekrar ediyor

print("Verisetinde Toplam kaç kelime var sayalım:")
print(df['Text'].str.split(expand=True).stack().value_counts().sum())  # Verisetinde Toplam kaç kelime var sayalım:

print("verisetinde toplam kaç unique kelime var sayalım:")
print(df['Text'].str.split(expand=True).stack().value_counts().count())  # Verisetinde tekrarsız kaç kelime var sayalım:

print("Verisetinde toplam kaç unique kelime var sayalım") # Verisetinde Toplam kaç unique kelime var sayalım:
print(df['Text'].str.split(expand=True).stack().value_counts().nunique())  # 6. yöntem -- 499
