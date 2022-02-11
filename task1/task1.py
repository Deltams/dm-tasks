n = int(input('Введите n - '))
# print('Число всех вариантов - ', 2**2**n)
# print('Число всех цифр - ', 2**n)
if n >= 0:
    for i in range(0, 2**2**n):
        t = str(bin(i)[2:])
        print(
            (2**n-len(t))*'0' + t
        )
else:
    print('error')