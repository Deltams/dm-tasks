import random

vec = '01010000'

def random_vector(vars_count):
    global vec
    len_vector = 2 ** vars_count
    count_all_vectors = 2 ** len_vector
    tmp = int(random.random()*(10**len(str(count_all_vectors)))) % count_all_vectors
    vec = str(bin(tmp)[2:])
    vec = "0" * (len_vector - len(vec)) + vec

def string_standard(player_string):
    player_string = player_string.replace(' ', '').lower()
    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')
    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')
    player_string = player_string.replace('x', '')
    player_string = player_string.split('v')
    return player_string

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

def dnf_check(player_string, vec):
    global set_param
    
    player_string = player_string.replace(' ', '').lower()

    if len(player_string) == 0 or len(player_string) == 1 and 'x' != player_string[0]:
        return False
    
    # Проверка в начале есть ли недопустимый символ
    if player_string[0] != '(' and player_string[0] != '-' and 'x' != player_string[0]:
        return False

    # Проверка в конце есть ли недопустимый символ
    if player_string[-1] != ')' and '1' > player_string[-1] > '9':
        return False
    
    for char in player_string: # Проверка на допустимые символы
        if char == '*' or char == 'v' \
        or char == '&' or 'x' == char \
        or char == '(' or char == ')' \
        or char == '-' or '1' <= char <= '9':
            continue
        return False
    
    psp = 0
    for char in player_string: # Проверка ПСП (Если конечно скобки есть)
        if char == '(':
            psp += 1
        elif char == ')':
            psp -= 1
            if psp < 0:
                return False
            
    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')

    for i in range(1, len(player_string)): # Проверка повторов символов (Перемер xx, **, &&, 11, 22, 12)
        if player_string[i-1] == player_string[i] \
        or ('1' <= player_string[i-1] <= '9' \
        and '1' <= player_string[i] <= '9'):
            return False
    
    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')

    stack_param = 0
    for i in range(0, len(player_string)): # Проверка на правильные переменные переменные
        if player_string[i] == '-':
            continue
        elif '1' <= player_string[i] <= '9':
            if stack_param == 0:
                return False
            stack_param -= 1
        elif player_string[i] != 'v' \
        and player_string[i] == 'x':
            stack_param = 1
        else:
            stack_param = 0
        if stack_param < 0:
            return False
    
    return True

def dnf_true(player_string):
    param = string_standard(player_string)
    vec_mass = []
    vec_ans = []
    for i in range(len(param)):
        vec_mass.append("")
    for i in range(len(vec)):
        vec_ans.append("0")
        t = str(bin(i)[2:])
        t = "0" * (what_degree_two(len(vec)) - len(t)) + t
        for tm in range(len(param)):
            zn = 1
            tmpp = 1
            for j in param[tm]:
                if j == '-':
                    zn = -1
                    continue
                if t[int(j)-1] == '1' and zn == -1:
                    tmpp *= 0
                elif t[int(j)-1] == '0' and zn == -1:
                    tmpp *= 1
                else:
                    tmpp *= int(t[int(j)-1])
                zn = 1
            vec_mass[tm] += str(tmpp)
            
    for string in range(len(vec_mass)):
        for j in range(len(vec_mass[string])):
            if vec_mass[string][j] == '1':
                vec_ans[j] = '1'
    return "".join(vec_ans)
    
    

#random_vector(3)
vec = '11011001'
print("Напишите ДНФ для вектора: " + vec)
player_string = input('Введите ДНФ: ')

if dnf_check(player_string, vec):
    ans_vec = dnf_true(player_string)
    if vec == ans_vec:
        print("Введеная ДНФ верная XD")
    else:
        print("Введеная ДНФ неверная!")
    
else:
    print("Не выебывайся!")
