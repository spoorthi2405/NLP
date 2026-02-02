import math

documents = [
    "I love NLP",
    "I love AI"
]


vocab = set()
for doc in documents:
    vocab.update(doc.split())
vocab = list(vocab)


def tf(word, doc):
    return doc.split().count(word) / len(doc.split())


def idf(word, docs):
    count = 0
    for d in docs:
        if word in d.split():
            count += 1
    return math.log(len(docs) / count)


for doc in documents:
    vector = []
    for word in vocab:
        vector.append(round(tf(word, doc) * idf(word, documents), 3))
    print(doc, ":", vector)
    
    
