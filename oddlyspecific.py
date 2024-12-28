number = 1
import mpmath
import webbrowser

type = input("sub, fib or pi or add or mult ")
type.lower()
if type == "mult":
    multtimes = input("by how much bro?????????????? ")
numbertimes = input("how many times ")
if type == "sub":
    subtimes = input("ok but by how much ")
    number = input("whats da faken starten numba?")

f = open("oddlyspecific.txt", "w")
if type == "add":
    for x in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = number + 1
elif type == "fib":
    prevnumber1 = 0
    prevnumber2 = 1
    for x in range(int(numbertimes)):
        f.write(f"{number}, ")
        prevnumber = number
        number = prevnumber1 + prevnumber2
        prevnumber1 = prevnumber2
        prevnumber2 = number
elif type == "pi":
    digitspi = 1
    for x in range(int(numbertimes)):
        digitspi = digitspi + 1
        mpmath.mp.dps = digitspi
        f.write(f"{mpmath.mp.pi}, ")
elif type == "mult":
    for x in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = number * int(multtimes)
elif type == "sub":
    for x in range(int(numbertimes)):
        f.write(f"{number}, ")
        number = int(number) - 1
else:
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

