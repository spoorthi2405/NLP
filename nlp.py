import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

text = "NLTK is a popular NLP library. It is widely used in AI. Sentence detection is important."

sentences = sent_tokenize(text)
print(sentences)

