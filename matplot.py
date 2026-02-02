import random
import matplotlib.pyplot as plt


numbers = []


for i in range(100):
    n = random.randint(1, 10)
    numbers.append(n)


frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] = frequency[n] + 1
    else:
        frequency[n] = 1


x = []
y = []

for key in frequency:
    x.append(key)
    y.append(frequency[key])


plt.figure()
plt.bar(x, y)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.title("Random Number Frequency")
plt.show()
