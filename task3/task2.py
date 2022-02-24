def what_degree_two(number): # В какую степень двойки возведено число; -1: не является степенью двойки
    tmp = 1
    ans = 0
    while tmp < number:
        tmp *= 2
        ans += 1
    if number == tmp:
        return ans
    else:
        return -1

def residual(vec, k, n): #остаточная по вектору; vec - vector; k - какая остаточная; n - переменная
    ans = ""
    tmp = len(vec) / 2**n
    i = k * tmp
    while i < len(vec):
        ans = ans + vec[int(i):int(i)+int(tmp)]
        i = i + tmp*2
    return ans

def check_vector(vec):
    if len(vec) < 2:
        return False
    if what_degree_two(len(vec)) == -1:
        return False
    for char in vec:
        if "0"<= char <= "1":
            continue
        return False
    return True

while True:
    player_string = input("Введите вектор функции: ")
    player_string = player_string.replace(' ', '').lower()
    vec = player_string
    k = 0
    n = 0
    if check_vector(player_string):
        while True:
            player_string = input("Введите какая остаточная интересует: ")
            player_string = player_string.replace(' ', '').lower()
            check = False
            for char in player_string:
                if '0' <= char <= '1':
                    continue
                check = True
                break
            if check:
                print('Остаточная введена неверно!')
                continue
            k = int(player_string)
            break
        while True:
            tmp = what_degree_two(len(vec))
            player_string = input(f"Введите номер аргумента(1 - {tmp}): ")
            player_string = player_string.replace(' ', '').lower()
            check = False
            for char in player_string:
                if '1' <= char <= str(tmp):
                    continue
                check = True
                break
            if check:
                print('Номер аргумента введен неверно!')
                continue
            n = int(player_string)
            break
        print(f"Ответ: {residual(vec, k, n)}")
        break
    print('Вектор введен с ошибками!')

