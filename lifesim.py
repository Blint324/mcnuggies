import random
food = 4
pop = 2
day = 1
death = 0
while True:
    for x in range(pop):
        selfish_nigga = random.randint(0, 1)
        if selfish_nigga == 0:
            pop = pop + 1
            food = food - 1
            death = death + 1
        else:
            food = food - 2
            pop = pop + 2
            death = death + 1
    day = day + 1
    pop = pop - death
    if day == 2:
        food = 4
        day = 1
    print(pop)
    if pop == 0 or pop <= 0:
        quit(0)