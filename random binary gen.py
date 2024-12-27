import random

f = open("random binary.txt", "w").close()
f = open("random binary.txt", "w")

while True:

    for x in range(8):
        f.write(str(random.randint(0, 1)))
    f.write(" ")