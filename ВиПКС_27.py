import random
import pickle


numbers = []

for i in range(10000):
    numbers.append(random.choice([-1, 1]))

with open("data.bin", "wb") as file:
    pickle.dump(numbers, file)

with open("data.bin", "rb") as file:
    arr = pickle.load(file)

print(sum(arr))