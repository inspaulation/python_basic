inputNumber = input('Enter an integer positive number:')
maxDigit = 0
for digit in map(int, inputNumber):
    if digit > maxDigit:
        maxDigit = digit

print('Max digit:', maxDigit)
