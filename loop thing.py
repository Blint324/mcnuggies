number = 0
howmanytimes = input("How many numbers? ")
for x in range(int(howmanytimes)):
    number = number + 1
    print(number)
    if not number == 1:
        if int(number) % 2 == 0:
            number = int(number) / 2
        else:
            number = int(number) * 3 + 1
        print(number)
    else:
        number = number + 1
    number = number + 1