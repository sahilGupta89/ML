import nltk
import random
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import movie_reviews,stopwords
import nltk.corpus.reader.plaintext as rd
import  pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk.data
# mypath = os.path.expanduser('~/nltk_data')
#
# negative = nltk.data.load('tweeter_review/neg/negative.txt',format='auto')
# positive = nltk.data.load('tweeter_review/neg/negative.txt',format='auto')

# document = [([],neg),([],pos)]
# final_pos_file = sent_tokenize(positive)
# final_neg_file = sent_tokenize(negative)
#
# documents = [(data,'neg') for data in negative]
#
# # for data in final_neg_file:
# #     documents.append((data, 'neg'))
#
# for data in final_pos_file:
#     documents.append((data, 'pos'))
#
# random.shuffle(documents)
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens_pos = word_tokenize(positive)
# word_tokens_neg = word_tokenize(negative)
#
# all_words = [w.lower() for w in word_tokens_pos if not w in stop_words]
#
# for w in word_tokens_neg:
#     if w not in stop_words:
#         all_words.append(w.lower())
#
# all_words = nltk.FreqDist(all_words)
#
# word_features = list(all_words.keys())[:1500]
#
#
# def find_features(document):
#     print(document, 'asdasdasd')
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#
#     return features
#
#
# featuresets = [(find_features(rev), category) for (rev, category) in documents]
#
# print('\nAAAAAAAAAAAA', featuresets[:100])























documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
print('document',documents,movie_reviews,movie_reviews.categories())


















random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(len(all_words))
word_features = list(all_words.keys())[:3000]
print(len(word_features))
def find_features(document):
    words = set(document)

    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
print(len(featuresets))

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()



MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))





print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)