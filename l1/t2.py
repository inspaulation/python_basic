inputSeconds = int(input("Type seconds:"))
s = inputSeconds % 60
m = inputSeconds // 60
h = m // 60
m = m % 60

print('{:02d}:{:02d}:{:02d}'.format(h, m, s))