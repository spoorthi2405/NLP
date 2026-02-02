from nltk.tokenize import PunktSentenceTokenizer

text = "This is sentence one. This is sentence two."

tokenizer = PunktSentenceTokenizer()
sentences = tokenizer.tokenize(text)
print(sentences)
