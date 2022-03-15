import random

t = 1 #кол-во попыток
param = 3 #кол-во переменных
map_vector = {} # Словарь ответов для пользователя; Автоматически заполняется в all_vector
list_vector = []

def residual(vec, k, n): #остаточная по вектору; vec - vector; k - какая остаточная; n - переменная
    ans = ""
    tmp = len(vec) / 2**n
    i = k * tmp
    while i < len(vec):
        ans = ans + vec[int(i):int(i)+int(tmp)]
        i = i + tmp*2
    return ans

def all_vector(p): #Заполнение map_vector; p - param
    n = 2**p
    tmp = 0
    nn = 2**n
    for i in range(nn):
        vec = str(bin(tmp)[2:])
        vec = "0"*(n-len(vec)) + vec #vec - временно хронится один из векторов
        fic_p = "" # Фиктивная переменная
        sysh_p = "" # Существенная переменная
        for j in range(1, p+1):
            s1 = residual(vec, 0, j)
            s2 = residual(vec, 1, j)
            if s1 == s2:
                fic_p = fic_p + str(j)
            else:
                sysh_p = sysh_p + str(j)
        if len(fic_p) != 0 and len(sysh_p) != 0:
            map_vector[vec] = [sysh_p, fic_p]
            list_vector.append(vec)
        tmp = tmp + 1

def check_data(s): # Проверка введеных данных пользователя
    for i in s:
        if '0' <= i and i <= '9':
            continue
        return 0
    return 1

def check_vector(plaer_vec, fic_sysh, plaer_string): # Проверка ответа пользователя fic_sysh - 0: существенная пременная; 1: Фиктивная переменная
    s = ""
    for i in plaer_string:
        if i == ' '
            continue
        s += i
    plaer_string = s
    if map_vector[plaer_vec][fic_sysh] == plaer_string: # plaer_vec - вектор, который предложен пользователю; plaer_string - строка которая была введена пользователем 
        return 1;
    return 0;
        

def help():
    ans = "\n\nЕсли нет фиктивных или существенных переменных, то пишите 0\n"
    ans += "Пример ввода данных: \n\n"
    ans += "Выберите существенные переменные для функции: 00101001\n\n"
    ans += "Попыток осталось: n\nВведите номер(а): 123\n\n"
    ans += "Если у вас остались вопросы, то их можно задать разработчикам:\n\n"
    ans += "https://vk.com/deltams4\n"
    ans += "https://vk.com/id212348723\n"
    ans += "https://vk.com/otza_to4ka_net\n\n"
    ans += "Приятной игры ;)\n\n\n\n"
    print(ans)

all_vector(param)

plaer_vec = list_vector[int(random.random()*100) % len(list_vector)] # Вектор, который передают пользователю

