import random

f = open("random numbers.txt", "w")

while True:
        f.write(str(random.randint(0, 9)))
