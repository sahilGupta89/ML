import nltk
import random
from nltk.tokenize import sent_tokenize,word_tokenize,RegexpTokenizer
from nltk.corpus import movie_reviews,stopwords
import  pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk.data

tokenizer = RegexpTokenizer(r'\w+')

neg_raw_txt = nltk.data.load('tweeter_review/neg/negative.txt',format='auto')
pos_raw_txt = nltk.data.load('tweeter_review/neg/negative.txt',format='auto')

# line wise tokanized
neg_raw_lines = sent_tokenize(neg_raw_txt)
pos_raw_lines = sent_tokenize(pos_raw_txt)
stop_words = set(stopwords.words('english'))

# document = [([],neg),([],pos)]
all_words = []
document = []

def prepDoc(tag):
    if tag=='neg':
        for line in neg_raw_lines:
            tokenized_words = tokenizer.tokenize(line)
            filtered_words = [w for w in tokenized_words if w not in stop_words]
            if(len(filtered_words)!=0):
                all_words.extend(filtered_words)
                document.append((filtered_words,tag))
    elif tag =='pos':
        for line in pos_raw_lines:
            tokenized_words = tokenizer.tokenize(line)
            filtered_words = [w for w in tokenized_words if w not in stop_words]
            if(len(filtered_words)!=0):
                all_words.extend(filtered_words)
                document.append((filtered_words,tag))
    else:
        return 'wrong tag'
    # return document

prepDoc('neg')
prepDoc('pos')

# print('doc',document)
random.shuffle(document)

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:1900]
print(len(word_features))

# print(all_words)

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return  features

# print(len(document))
#
featuresets = [(find_features(rev), category) for (rev, category) in document]
print(len(featuresets))

# set that we'll train our classifier with
training_set = featuresets[:2500]

# set that we'll test against.
testing_set = featuresets[2500:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

save_classifier = open("classifier.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

classifier_f = open("classifier.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set)*100)

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set)*100)





print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)

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