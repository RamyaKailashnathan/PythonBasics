#Program to find Prime factors of a given number

list = []

def factor(x):
    d = 2
    while (d < x):
        if (x % d == 0):
            list.append(d)
            print(x)
            x = x // d
        else:
            d += 1
    print(list)
    return (list)


# main program
num = int(input("Enter the number to be evaluated: "))
factor(num)

