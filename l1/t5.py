revenue = float(input('Revenue value $:'))
costs = float(input('Costs value $:'))
profit = revenue - costs
if profit > 0:
    print('Congrats! Your profit is positive: {}$, Profitability: {:.3f}'.format(profit, profit / revenue))
    employees = int(input('Number of employees:'))
    print('Earnings per employee: {}$'.format(profit / employees))
else:
    print('Sad news.. Your profit is non-positive:', profit)