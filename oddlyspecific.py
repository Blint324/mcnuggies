number = 1
x = [0]
y = [0]
filename = 1
xnum = 1
import mpmath
import webbrowser
import random
import sys
import matplotlib.pyplot as plt
import math
import os
sys.set_int_max_str_digits(999999999)


runmult = input("run multiple times? (y/n) (only works for rand and truerand) ")
runmult.lower()
if runmult == "y":
    runmulthowmany = input("how many times? ")
type = input("fact, truerand, rand, sub, div, fib or pi or add or mult ")
type.lower()
if type == "mult":
    multtimes = input("by how much bro?????????????? ")
numbertimes = input("how many times ")
if type == "sub" or type == "div":
    times = input("ok but by how much ")
    number = input("whats da faken starten numba? ")
if type == "rand":
    randmaxinc = input("maximum increment ")
    randmaxdec = input("maximum decrement (type a negative number or else it'll just keep going up) ")
    randstartnumber = input("starting number ")
if type == "truerand":
    truerandmax = input("maximum number ")
    truerandmin = input("minimum number ")

print(f"{os.getcwd()}{os.sep}oddlyspecific.txt")
f = open("oddlyspecific.txt", "w")

if type == "add":
    for n in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = number + 1
        xnum = xnum + 1
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("add nums")
    plt.show()
    f.close()
elif type == "fib":
    prevnumber1 = 0
    prevnumber2 = 1
    for n in range(int(numbertimes)):
        f.write(f"{number}, ")
        prevnumber = number
        number = prevnumber1 + prevnumber2
        prevnumber1 = prevnumber2
        prevnumber2 = number
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("add nums")
    plt.show()
    f.close()
elif type == "pi":
    digitspi = 1
    for n in range(int(numbertimes)):
        digitspi = digitspi + 1
        mpmath.mp.dps = digitspi
        f.write(f"{mpmath.mp.pi}, ")
        f.close()
elif type == "mult":
    for n in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = number * int(multtimes)
        xnum = xnum + 1
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("mult nums")
    plt.show()
    f.close()
elif type == "sub":
    for n in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = int(number) - 1
        xnum = xnum + 1
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("sub nums")
    plt.show()
    f.close()
elif type == "div":
    for n in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = float(number) / float(times)
        xnum = xnum + 1
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("div nums")
    plt.show()
    f.close()
elif type == "rand":
    if runmult == "y":
        number = randstartnumber
        for n in range(int(runmulthowmany)):
            for n in range(int(numbertimes)):
                f.write(f"{number}, ")
                randamount = random.randint(int(randmaxdec), int(randmaxinc))
                number = int(number) + int(randamount)
                xnum = xnum + 1
                x.append(xnum)
                y.append(number)
            plt.plot(x, y)
            plt.title("rand nums")
            plt.savefig(str(filename))
            filename = filename + 1
            x = [0]
            y = [0]
            xnum = 1
            number = randstartnumber
            plt.clf()
            f.close()
    else:
        for n in range(int(numbertimes)):
            f.write(f"{number}, ")
            randamount = random.randint(int(randmaxdec), int(randmaxinc))
            number = int(number) + int(randamount)
            xnum = xnum + 1
            x.append(xnum)
            y.append(number)
        plt.plot(x, y)
        plt.title("rand nums")
        plt.show()
        filename = filename + 1
        x = [0]
        y = [0]
        xnum = 1
        number = randstartnumber
        plt.clf()
        f.close()
elif type == "truerand":
    if runmult == "y":
        for n in range(int(runmulthowmany)):
            for n in range(int(numbertimes)):
                number = random.randint(int(truerandmin), int(truerandmax))
                f.write(f"{number}, ")
                xnum = xnum + 1
                x.append(xnum)
                y.append(number)
            plt.plot(x, y)
            plt.title("true rand nums")
            plt.savefig(str(filename))
            filename = filename + 1
            x = [0]
            y = [0]
            xnum = 1
            plt.clf()
            f.close()
    else:
        for n in range(int(numbertimes)):
            number = random.randint(int(truerandmin), int(truerandmax))
            f.write(f"{number}, ")
            xnum = xnum + 1
            x.append(xnum)
            y.append(number)
        plt.plot(x, y)
        plt.title("truerand nums")
        plt.show()
        filename = filename + 1
        x = [0]
        y = [0]
        xnum = 1
        plt.clf()
        f.close()
elif type == "fact":
    factcount = 1
    for n in range(int(numbertimes)):
        number = math.factorial(factcount)
        f.write(f"{number}, ")
        factcount = factcount + 1
        xnum = xnum + 1
        x.append(xnum)
        y.append(number)
    plt.plot(x, y)
    plt.title("factorial nums")
    plt.show()
    filename = filename + 1
    x = [0]
    y = [0]
    xnum = 1
    plt.clf()
    f.close()
else:
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

