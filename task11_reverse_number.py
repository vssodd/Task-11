def reverse_number(n):
    return int(str(n)[::-1])

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("Program terminated!")
        break
    else:
        print("Reversed number:", reverse_number(num))
