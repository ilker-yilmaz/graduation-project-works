# Tweet'ler üzerinde duygu analizi
# Gerekli kütüphaneler
import nltk
import re
from nltk.corpus import stopwords
import string
from nltk.classify import SklearnClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import random

# Gerekli kütüphanelerin indirilmesi
nltk.download("stopwords")
nltk.download('punkt')

# Duygu analizi için gerekli olan veriler
short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()

# Verilerin temizlenmesi
all_words = []
documents = []
allowed_word_types = ["J"]
stop_words = set(stopwords.words('english'))

for p in short_pos.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            if w[0] not in stop_words:
                all_words.append(w[0].lower())

for p in short_neg.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            if w[0] not in stop_words:
                all_words.append(w[0].lower())

# Tüm kelimelerin frekanslarının belirlenmesi
all_words = nltk.FreqDist(all_words)

# En sık kullanılan 5000 kelimenin alınması
word_features = list(all_words.keys())[:5000]

# Kelimelerin verilerle eşleştirilmesi
def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# Tüm verilerin eşleştirilmesi
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Eğitim ve test verilerinin belirlenmesi
random.shuffle(featuresets)
training_set = featuresets[:10000]
testing_set = featuresets[10000:]

# Sınıflandırıcıların belirlenmesi
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)


# Sınıflandırıcıların kaydedilmesi
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# Sınıflandırıcıların yüklenmesi
classifier_f = open("naivebayes.pickle", "rb")

classifier = pickle.load(classifier_f)
classifier_f.close()

# Yeni tweet'lerin analiz edilmesi
custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."
custom_tokens = word_tokenize(custom_tweet)
custom_set = find_features(custom_tweet)
print(custom_tweet, classifier.classify(custom_set), "Confidence %:", classifier.confidence(custom_set))

custom_tweet = "I love the new iPhone. It is so awesome."
custom_tokens = word_tokenize(custom_tweet)
custom_set = find_features(custom_tweet)
print(custom_tweet, classifier.classify(custom_set), "Confidence %:", classifier.confidence(custom_set))
