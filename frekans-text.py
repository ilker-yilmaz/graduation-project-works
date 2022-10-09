# Finding the total number of words on the text

import pandas as pd

text = "bu bu bir bir deneme bir metin olarak sayılabilir olarak toplam kaç kelime kaç kelime olduğunu bulalım"

print(text.split())

print(len(text.split()))

print(text.split().count("bu"))

# tekrar etmeyen unique kelimeleri bulalım

print(set(text.split()))

print(len(set(text.split())))

