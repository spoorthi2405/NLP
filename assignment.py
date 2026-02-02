import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Task 1: Clean and Process
def clean_and_process(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z\s]', '', sentence)
    tokens = sentence.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens

# Task 2: Levenshtein Distance
def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# Task 3: Spam Detector
def spam_detector(message, spam_words):
    message_lower = message.lower()
    found_spam_words = [word for word in spam_words if word in message_lower]
    is_spam = len(found_spam_words) > 0
    return is_spam, found_spam_words

# Tests
print("Task 1:")
print(clean_and_process("The quick, BROWN foxes...they are JUMPING over 10 lazy dogs!"))

print("\nTask 2:")
print(f"Distance: {levenshtein_distance('start', 'stare')}")

print("\nTask 3:")
is_spam, words = spam_detector("you are wining a free price now!", ["win", "cash", "free"])
print(f"Is Spam: {is_spam}")
print(f"Spam words: {words}")