def sum_n(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    print(total)

N = int(input('Enter a number: '))
sum_n(N)

def test():
    N = int(input('Enter a number: '))
    if N > 0:
        positive()
    else:
        negative()

def positive():
    print("Positive")

def negative():
    print("Negative")
