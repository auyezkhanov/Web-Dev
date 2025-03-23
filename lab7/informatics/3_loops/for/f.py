<<<<<<< HEAD
x = int(input())

digits = []

i = x
while i > 0:
    digits.append(i % 10)
    i //= 10

x_rev = ''.join(map(str, digits))
=======
x = int(input())

digits = []

i = x
while i > 0:
    digits.append(i % 10)
    i //= 10

x_rev = ''.join(map(str, digits))
>>>>>>> d2f3f40 (commit)
print(x_rev.lstrip('0'))