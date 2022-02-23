while True:
    n = input('Введите n - ')
    n = n.replace(' ', '').lower()
    check = False
    for i in n:
        if '0' <= i <= '9':
            continue
        print("Ошибка при вводе данных!")
        check = True
        break
    if check:
        continue
    break
# print('Число всех вариантов - ', 2**2**n)
# print('Число всех цифр - ', 2**n)
n = int(n)
var_ch = 2**n
if n >= 0:
    for i in range(0, 2**2**n):
        t = str(bin(i)[2:])
        print((var_ch-len(t))*'0' + t)
else:
    print('error')
