def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def max_digit(n):
    return max(int(digit) for digit in str(n))

def min_digit(n):
    return min(int(digit) for digit in str(n))

while True:
    N = int(input('Enter a number: '))
    action = input('Enter an action (sum, max, min): ')
    
    if action == 'sum':
        print(sum_digits(N))
    elif action == 'max':
        print(max_digit(N))
    elif action == 'min':
        print(min_digit(N))
    else:
        print('Unknown action')
