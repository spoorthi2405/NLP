import random
import matplotlib.pyplot as plt

numbers = []
for i in range(100):
    numbers.append(random.randint(1, 10))

# Histogram
plt.hist(numbers, bins=10)
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers")
plt.show()
