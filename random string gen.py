import string
import random

f = open("random string.txt", "w")

while True:
    random1 = random.randint(0, 1)
    if random1 == 0:
        f.write(random.choice(string.ascii_letters))
    else:
        f.write(str(random.randint(0, 9)))
