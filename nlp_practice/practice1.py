import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

sentence = """At the eight o'clock on Thursday morning
... Arthur didn't feel very good."""

tokens = word_tokenize(sentence)
sw = stopwords.words('english')

print('?????',[t for t in tokens if t not in sw])
print('done')