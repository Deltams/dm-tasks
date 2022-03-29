import os

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

#Получение числа сочетаний
#Входные данные: 123, 4; 124, 4
#Выходные данные: 124;   134
def next_znach(tmp, mx):
    id_i = 0
    if len(tmp) == 1 and mx == int(tmp):
        return tmp
    for i in range(len(tmp)-1, 0, -1):
        if int(tmp[i]) < mx:
            tmp = tmp[:i] + str(int(tmp[i])+1) + tmp[i+1:]
            return tmp
        else:
            while i >= 0 and int(tmp[i]) == mx:
                mx -= 1
                i -= 1
            if i < 0:
                return tmp
            else:
                id_i = i
                break
    t = tmp[:id_i] + str(int(tmp[id_i])+1)
    for i in range(id_i, len(tmp)-1):
        t += str(int(t[i])+1)
    return t
    

#Вид входной строки: '-x1x2x3' и 'x1x2'
#Вид выходного массива: ['-x1x2', '-x1x3', 'x2x3', '-x1', 'x2', 'x3'] и ['x1', 'x2']
#Использовать до x9
def iterating_values(string):
    ans = []
    tmp = ''
    for i in range(len(string)):
        tmp += string[i]
        if '1' <= string[i] <= '9':
            ans.append(tmp)
            tmp = ''
    len_param = string.count('x')
    tmp_ans = []
    tmp_ans.append(string)
    for q in range(len_param-1):
        tmp = ''
        for i in range(0, len_param-1-q):
            tmp += str(i+1)
        i = len(tmp)-1
        mx = len_param
        tmp_ans.append(tmp)
        while next_znach(tmp, mx) != tmp:
            tmp = next_znach(tmp, mx)
            tmp_ans.append(tmp)
    for i in range(1, len(tmp_ans)):
        t = ''
        for j in range(len(tmp_ans[i])):
            t += ans[int(tmp_ans[i][j])-1]
        tmp_ans[i] = t
    return tmp_ans

#Треугольник паскаля по номеру начиная с 0 [1]
def pask_tr(number):
    ans = [1]
    for i in range(number):
        tmp = [1]
        for j in range(len(ans)-1):
            tmp.append(ans[j]+ans[j+1])
        tmp.append(1)
        ans = tmp
    return ans

def write_file(s):
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\seve.txt'
    with open(file, 'w') as f:
        f.write(s)

#Красивый вывод в таблицу
def print_table(table):
    ans = ''
    count_param = what_degree_two(len(table[0]) + 1)
    sp = pask_tr(count_param)
    mx = 1
    for i in range(0 , len(sp)-1):
        mx += (3 * (count_param-i) + 3)*sp[i]
    div = '='*mx
    mini_div = '-'*mx
    #print(div)
    ans += div + '\n'
    for i in range(len(table)):
        #s = '|'
        ans += '|'
        id_sp = 0
        tmp_sp = sp.copy()
        for j in range(len(table[i])):
            space = int(((3 * (count_param-id_sp) + 2) - len(table[i][j]))/2)
            ans += ' '*space + table[i][j]
            #s += ' '*space + table[i][j]
            space = (3 * (count_param-id_sp) + 2) - (space + len(table[i][j]))
            ans += ' '*space + '|'
            #s += ' '*space + '|'
            tmp_sp[id_sp] -= 1
            if tmp_sp[id_sp] == 0:
                id_sp += 1
        ans += '\n'
        #print(s)
        if i + 1 != len(table):
            ans += mini_div + '\n'
            #print(mini_div)
    ans += div + '\n'
    #print(div)
    write_file(ans)
 
# Создание таблицы для дальнейшей работы с ней
def creating_table2(vec_player):
    len_vec_player = len(vec_player)
    ans_table = []
    for i in range(len_vec_player):
        vec = str(bin(i)[2:])
        vec = "0" * (what_degree_two(len_vec_player) - len(vec)) + vec
        
        #Проходим по таблице истинности
        tmp = ''
        for j in range(1, len(vec)+1):
            if vec[j-1] == '0':
                tmp += f'-x{j}'
            else:
                tmp += f'x{j}'
        ans_table.append(iterating_values(tmp))
    return ans_table
        
# Сокращение в таблице
def reduction_table(table, vec):
    for q in range(len(vec)):
        if vec[q] == '0':
            for i in range(len(table[q])):
                for j in range(len(table)):
                    if q != j and table[q][i] == table[j][i]:
                        table[j][i] = '-1'
                table[q][i] = '-1'
    return table

# Есть ли в таблице еще значения?
def check_table2(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != '-1':
                return True
    return False

#Создание копии талицы
def copy_table(table):
    table2 = []
    for i in range(len(table)):
        ans = []
        for j in range(len(table[i])):
            ans.append(table[i][j])
        table2.append(ans)
    return table2
    
#Перебор всех значений в таблице и выбор минимальной ДНФ
set_all_ans = set()
min_ans = ['0']*10000
def min_DNF22(table2, ans2, step2):
    global min_ans
    global set_all_ans
    if len(min_ans) > len(ans2):
        for i in range(len(table2)):
            for j in range(len(table2[i])-1, -1, -1):
                if table2[i][j] != '-1':
                    if step2 == 1 and table2[i][j] in set_all_ans:
                        continue
                    set_all_ans.add(table2[i][j])
                    #print(set_all_ans)
                    ans = []
                    for q in range(len(ans2)):
                        ans.append(ans2[q])
                    table = copy_table(table2)
                    for qi in range(len(table)):
                        if i != qi and table[i][j] == table[qi][j]:
                            for qj in range(len(table[qi])):
                                table[qi][qj] = '-1'
                    ans.append(table[i][j])
                    for qj in range(len(table[i])):
                        table[i][qj] = '-1'
                    if check_table2(table):
                        min_DNF22(copy_table(table), ans.copy(), step2+1)
                    else:
                        if len(min_ans) > len(ans):
                            min_ans = ans
                        #print(ans)


#Перевод из массива в строку для пользователя                        
def printf_DNF2(ans):
    ret_ans = ''
    for string in ans:
        ret_ans += f'({string})v'
    ret_ans = ret_ans[:len(ret_ans)-1]
    return ret_ans

#Упаковывающая функции для вызова минимальной ДНФ
def min_DNF2(table, ans):
    global min_ans
    global set_all_ans
    set_all_ans = set()
    min_ans = ['0']*10000
    min_DNF22(table, ans, 1)
    return printf_DNF2(min_ans)

def selecting_single_values(table):
    ans = []
    for i in range(len(table)):
        count_var = 0
        id_j = -1
        for j in range(1, len(table[i])):
            if table[i][j] != '-1':
                count_var += 1
                id_j = j
        if count_var == 1:
            for qi in range(len(table)):
                if qi != i and table[qi][id_j] == table[i][id_j]:
                    for qj in range(len(table[qi])):
                        table[qi][qj] = '-1'
            ans.append(table[i][id_j])
            for qj in range(len(table[i])):
                table[i][qj] = '-1'
    return ans
            
   
### Выбор минимальной ДНФ по таблице
##def min_DNF(table, vec):
##    ans = set()
##    count_param = what_degree_two(len(table[0]) + 1)
##    pask_treyg = pask_tr(count_param)
##    # Проходим и смотрим какие одиночные значения существуют
##    for i in range(len(table)):
##        id_ans = -1
##        count_var = 0
##        for j in range(1, len(table[i])):
##            if table[i][j] != '-1':
##                count_var += 1
##                id_ans = j
##        if count_var == 1:
##            for j in range(len(table)):
##                if j != i and table[j][id_ans] == table[i][id_ans]:
##                    for q in range(len(table[j])):
##                        table[j][q] = '-1'
##            ans.add(table[i][id_ans])
##            for q in range(len(table[i])):
##                table[i][q] = '-1'
##    # Проходим и смотрим значения по столбцам и делим их по кол-ву переменных
##    pask_treyg = pask_tr(count_param)
##    id_pt = len(pask_treyg)-2 # Для прохода по выделенной группе переменных
##    qj = len(table[0])-1
##    while True:
##        for qi in range(len(table)):
##            for pt in range(0, pask_treyg[id_pt]):
##                if table[qi][qj-pt] != '-1':
##                    for i in range(len(table)):
##                        if i != qi and table[qi][qj-pt] == table[i][qj-pt]:
##                            for j in range(len(table[i])):
##                                table[i][j] = '-1'
##                    ans.add(table[qi][qj-pt])
##                    for j in range(len(table[qi])):
##                        table[qi][j] = '-1'
##        qj = qj - pask_treyg[id_pt]
##        id_pt -= 1
##        if id_pt < 0:
##            break
##    return printf_DNF(ans)

# Для тестов, можно удалить
##def all_vec(n):
##    global min_ans
##    var_ch = 2**n
##    for i in range(0, 2**2**n):
##        t = str(bin(i)[2:])
##        t = (var_ch-len(t))*'0' + t
##        table = creating_table(t)
##        table = reduction_table(table, t)
##        #print_table(table)
##        print(t)
##        min_DNF2(table, [])
##        print(printf_DNF(min_ans))
##        min_ans = ['0']*10000
##        print(min_DNF(table, t))
##        print()

##all_vec(3)

player_string = input("Введите вектор: ")
player_string = player_string.replace(' ', '')
        
if check_vector(player_string):
    table = creating_table2(player_string)
    #print_table(table)
    table = reduction_table(table, player_string)
    #print_table(table)
    ans = []
    while True:
        tmp_ans = selecting_single_values(table)
        if len(tmp_ans) == 0:
            break
        for i in tmp_ans:
            ans.append(i)
    print_table(table)
    #print(ans)
    if check_table2(table):
        print(min_DNF2(table, ans))
    else:
        print(printf_DNF2(ans))
else:
    print("Ошибка при вводе вектора!")
