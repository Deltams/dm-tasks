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

def my_pow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return my_pow(a*a, p / 2)
    return a * my_pow(a, p-1)

def check_vector(vec):
    if len(vec) < 1:
        return False
    if what_degree_two(len(vec)) == -1:
        return False
    for char in vec:
        if "0"<= char <= "1":
            continue
        return False
    return True

def restoration_of_residual(v1, v2, n):
    ans = ''
    tmp = int(len(v1)*2 / my_pow(2, n))
    for i in range(0,len(v1), tmp):
        for j in range(i, i + tmp):
            ans += v1[j]
        for j in range(i, i + tmp):
            ans += v2[j]
    return ans

vec_z = ''
vec_o = ''
n = 1
while True:
    player_string = input("Введите нулевую остаточную: ")
    player_string = player_string.replace(' ', '').lower()
    vec_z = player_string
    if check_vector(player_string):
        break
    print('Нулевая остаточная введена с ошибками!')
    
while True:
    player_string = input("Введите единичную остаточную: ")
    player_string = player_string.replace(' ', '').lower()
    vec_o = player_string
    if check_vector(player_string):
        break
    print('Единичная остаточная введена с ошибками!')

while True:
    tmp = what_degree_two(len(vec_z)*2)
    player_string = input(f"Введите номер аргумента(1 - {tmp}): ")
    player_string = player_string.replace(' ', '').lower()
    check = False
    if len(player_string) != 1:
        print('Номер аргумента введен неверно!')
        continue
    for char in player_string:
        if '1' <= char <= str(what_degree_two(len(vec_z)*2)):
            continue
        check = True
        break
    if check:
        print('Номер аргумента введен неверно!')
        continue
    n = int(player_string)
    break

print(f"Ответ: {restoration_of_residual(vec_z, vec_o, n)}")

