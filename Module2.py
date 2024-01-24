def q1():
    ii = 1
    i = 1
    while ii <= 1000000000:
        print(i,":",ii)
        ii *= 2
        i += 1
    return

def q2():
    ii = 1
    i = 1
    while ii <= 1000000000:
        print(i,":",ii)
        ii *= 10
        i += 1
    return

def factorial(n: int)-> int:
    if n == 1:
        return n
    return n * factorial(n-1)


if __name__ == "__main__":
    #q1()
    #q2()
    print(factorial(7))