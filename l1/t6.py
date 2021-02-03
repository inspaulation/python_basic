firstResult = float(input('Enter your first day result in kilometers:'))
targetResult = float(input('Enter your target result in kilometers:'))
currentResult = firstResult
dayCounter = 1
while currentResult < targetResult:
    dayCounter += 1
    currentResult *= 1.1

print('You need {} days to reach your target results'.format(dayCounter))
