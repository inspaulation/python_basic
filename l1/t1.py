a = 10 ** 100
b = 'kek'
print('a:', a, 'b:', b)
c = int(input('Type int:'))
d = int(input('Type int:'))
e = float(input('Type float:'))
f = str(input('Type str:'))

print('c:{}({})\nd:{}({})\ne:{}({})\nf:{}({})'.format(c, type(c), d, type(d), e, type(e), f, type(f)))