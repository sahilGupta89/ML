from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
from nltk.corpus import  stopwords

text = "Born and raised on the Portuguese island of Madeira, Ronaldo was diagnosed with a racing heart at age 15. " \
       "He underwent an operation to treat his condition, and began his senior club career playing for Sporting CP," \
       " before signing with Manchester United at age 18 in 2003. After winning his first trophy, the FA Cup, during his" \
       " first season in England, he helped United win three successive Premier League titles, a UEFA Champions League title," \
       " and a FIFA Club World Cup. By age 22, he had received Ballon d'Or and FIFA World Player of the Year nominations " \
       "and at age 23, he won his first Ballon d'Or and FIFA World Player of the Year awards. In 2009, Ronaldo was the subject " \
       "of the most expensive association football transfer when he moved from Manchester United to Real Madrid in a " \
       "transfer worth €94 million (£80 million).With Real Madrid, Ronaldo won 15 trophies, including two La Liga titles, " \
       "two Copas del Rey, four UEFA Champions League titles, two UEFA Super Cups, and three FIFA Club World Cups. " \
       "Real Madrid's all-time top goalscorer, Ronaldo scored a record 34 La Liga hat-tricks, including a record-tying " \
       "eight hat-tricks in the 2014–15 season[note 3] and is the only player to reach 30 goals in six consecutive La Liga" \
       " seasons. After joining Madrid, Ronaldo finished runner-up for the Ballon d'Or three times, behind Lionel Messi," \
       " his perceived career rival, before winning back-to-back Ballons d'Or in 2013 and 2014. After winning the 2016 and " \
       "2017 Champions Leagues, Ronaldo secured back-to-back Ballons d'Or again in 2016 and 2017. A historic third " \
       "consecutive Champions League followed, making Ronaldo the first player to win the trophy five times.[7] In 2018, " \
       "he signed for Juventus in a transfer worth an initial €100 million; the highest ever paid by an Italian club and " \
       "the highest fee ever paid for a player over 30 years old."

tokenizer = RegexpTokenizer(r'\w+')
tokenized = tokenizer.tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [w for w in tokenized if w not in stop_words]

ps = PorterStemmer()

stem_word = [ps.stem(sw) for sw in filtered_words]

print(filtered_words)
print(stem_word)



