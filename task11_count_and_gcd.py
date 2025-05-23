text = input("Enter text: ")
digit = input("Which digit are we looking for? ")
letter = input("Which letter are we looking for? ")

count_letters(text, digit, letter)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
