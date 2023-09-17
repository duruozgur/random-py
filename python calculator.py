import math
import time

print("This is calculator. Yea")
time.sleep(1)

commands = ["round", "ceil", "floor", "abs", "pow", "sqrt", "max", "min", "exit"]
print("Commands: round, ceil, floor, abs, pow, sqrt, max, min, multiply, subtract, add, divide, exit")
time.sleep(2)
while True:
    problem = input("What do you wanna do?:")

    if problem == "round":
        print("This command will round the decimal number into the nearest integer.")
        num = float(input("give a number:"))
        print(round(num))

    if problem == "ceil":
        print("This command will round the decimal number into the nearest integer that is bigger than the number you gave.")
        num1 = float(input("give a number:"))
        print(math.ceil(num1))

    if problem == "floor":
        print("This command will round the decimal number into the nearest integer that is smaller than the number you gave.")
        num2 = float(input("give a number:"))
        print(math.floor(num2))

    if problem == "abs":
        print("This command will give you the absolute value of the number you gave.")
        num3 = float(input("give a number:"))
        print(abs(num3))

    if problem == "pow":
        print("This command will raise a base number to a power.")
        num4 = float(input("give a base number:"))
        power = float(input("give a power:"))
        print(pow(num4,power))

    if problem == "sqrt":
        print("This command will give the square root of the number you gave.")
        num5 = float(input("give a number:"))
        print(math.sqrt(num5))

    if problem == "multiply":
        print("This command will multiply the two numbers you gave.")
        num6 = float(input("give a number:"))
        num7 = float(input("give a number:"))
        print(num6*num7)

    if problem == "subtract":
        print("This command will subtract the two numbers you gave.")
        num8 = float(input("give a diminishing number:"))
        num9 = float(input("give a subtrahend number:"))
        print(num8-num9)

    if problem == "add":
        print("This command will add the two numbers you gave together.")
        num10 = float(input("give a number:"))
        num11 = float(input("give a number:"))
        print(num10+num11)

    if problem == "divide":
        print("This command will divide the two numbers you gave.")
        num12 = float(input("give a dividend number:"))
        num13 = float(input("give a divider number:"))
        print(num12/num13)

    if problem == "max":
        print("This command will return you the largest one of the numbers you gave.")
        numofval = float(input("how many values do you want?(max num of values:10):"))
        if numofval == 2:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            print(max(a,b))
        elif numofval == 3:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            print(max(a,b,c))
        elif numofval == 4:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            print(max(a,b,c,d))
        elif numofval == 5:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            print(max(a,b,c,d,e))
        elif numofval == 6:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            print(max(a,b,c,d,e,f))
        elif numofval == 7:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            print(max(a,b,c,d,e,f,g))
        elif numofval == 8:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            print(max(a,b,c,d,e,f,g,h))
        elif numofval == 9:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            i = float(input("give a number:"))
            print(max(a,b,c,d,e,f,g,h,i))
        elif numofval == 10:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            i = float(input("give a number:"))
            j = float(input("give a number:"))
            print(max(a,b,c,d,e,f,g,h,i,j))

    if problem == "min":
        print("This command will return you the smallest one of the numbers you gave.")
        numofval = float(input("how many values do you want?(max num of values:10):"))
        if numofval == 2:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            print(min(a,b))
        elif numofval == 3:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            print(min(a,b,c))
        elif numofval == 4:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            print(min(a,b,c,d))
        elif numofval == 5:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            print(min(a,b,c,d,e))
        elif numofval == 6:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            print(min(a,b,c,d,e,f))
        elif numofval == 7:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            print(min(a,b,c,d,e,f,g))
        elif numofval == 8:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            print(min(a,b,c,d,e,f,g,h))
        elif numofval == 9:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            i = float(input("give a number:"))
            print(min(a,b,c,d,e,f,g,h,i))
        elif numofval == 10:
            a = float(input("give a number:"))
            b = float(input("give a number:"))
            c = float(input("give a number:"))
            d = float(input("give a number:"))
            e = float(input("give a number:"))
            f = float(input("give a number:"))
            g = float(input("give a number:"))
            h = float(input("give a number:"))
            i = float(input("give a number:"))
            j = float(input("give a number:"))
            print(min(a,b,c,d,e,f,g,h,i,j))

    if problem == "exit":
        print("Sure")
        time.sleep(1.3)
        break