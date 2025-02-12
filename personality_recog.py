import nltk
import jsonlines
import re
from pymongo import MongoClient
client = MongoClient()
db = client.twitter_profiles
posts = db.twitter_timeline


def get_tweets(username):
    stweet = ''
    count = 0
    name=""
    query = { "username": username }

    queryRes = posts.find(query)

    for obj in queryRes:
        text = str(obj['content']['text'])
        stweet += text
        count = count + 1
    return stweet, count, username

# function to get
def get_count(text_given):
    tokenizer = nltk.tokenize.TweetTokenizer()

    c_user_mentions = 0
    c_url = 0
    c_exclam = 0
    c_Hash = 0
    c_question = 0
    c_rt = 0
    tokens = tokenizer.tokenize(str(text_given))
    for word in tokens:
        if word.startswith('@'):
            c_user_mentions += 1
        if word.startswith('http'):
            c_url += 1
        if word.startswith('#'):
            c_Hash += 1
        if word.startswith('RT') or word.startswith('rt'):
            c_rt += 1
        if word.startswith('!'):
            c_exclam += 1
        if word.startswith('?'):
            c_question += 1
    return c_user_mentions, c_url, c_Hash, c_rt, c_exclam, c_question

def clean_with_regex(unregTweet):
 return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", unregTweet).split())

