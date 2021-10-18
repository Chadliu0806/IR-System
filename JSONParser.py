import json
from Regex import getChars, getWords, getSentences, getMatch

nChars = 0
nWords = 0
nSentences = 0

def tweets_parser(tweet, pattern):
    
    count = 0
    vtweet = []
    global nChars
    global nWords
    global nSentences
   

    # Only process tweet content which property name is "tweet_text"
    vtweet.append(tweet['tweet_text'])

    if (pattern != ''):
        getMatch(pattern, str(vtweet[0]))
    count = getChars(vtweet[0])
    nChars += count
    print('The number of characters in \'tweet_text\':', count)
    count  = 0
    count  = getWords(vtweet[0])
    nWords += count
    print('The number of words in \'tweet_text\':', count)
    count  = 0
    count  = getSentences(vtweet[0])
    nSentences += count
    print('The number of sentences in \'tweet_text\':', count)
    print('\n')
    contents = str(vtweet[0])
    
    
def JSONParser(filename, pattern):

    ntweet = 1
    global contents

    with open(filename, encoding='UTF-8') as f:
        buf = json.load(f)
        
        if type(buf) == list:
            for brackets in buf:
                subdict = dict(brackets)
                sz = 'tweet' + str(ntweet)
                print(sz)
                tweets_parser(subdict, pattern)
                ntweet += 1
        print('\n')
        print('The total number of characters :', nChars)
        print('The total number of words :', nWords)
        print('The total number of sentences :', nSentences)
           
