text = "Hello, world! Welcome to tokenization."

# Remove punctuation manually
punctuations = ".,!?;:"

for p in punctuations:
    text = text.replace(p, "")

tokens = text.split()
print(tokens)