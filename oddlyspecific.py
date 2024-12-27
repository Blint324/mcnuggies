number = 1
import mpmath
import webbrowser

type = input("fib or pi or add or mult my nigga ")
type.lower()
if type == "mult":
    multtimes = input("by how much bro?????????????? ")
numbertimes = input("penis ")

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
else:
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
