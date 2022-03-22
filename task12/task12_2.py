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
        

#Красивый вывод в таблицу
def print_table(table):
    count_param = what_degree_two(len(table[0]) + 1)
    sp = pask_tr(count_param)
    mx = 1
    for i in range(0 , len(sp)-1):
        mx += (3 * (count_param-i) + 3)*sp[i]
    div = '='*mx
    mini_div = '-'*mx
    print(div)
    for i in range(len(table)):
        s = '|'
        id_sp = 0
        tmp_sp = sp.copy()
        for j in range(len(table[i])):
            space = int(((3 * (count_param-id_sp) + 2) - len(table[i][j]))/2)
            s += ' '*space + table[i][j]
            space = (3 * (count_param-id_sp) + 2) - (space + len(table[i][j]))
            s += ' '*space + '|'
            tmp_sp[id_sp] -= 1
            if tmp_sp[id_sp] == 0:
                id_sp += 1
        print(s)
        if i + 1 != len(table):
            print(mini_div)
    print(div)
 
# Создание таблицы для дальнейшей работы с ней
def creating_table(vec_player):
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
def check_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != '-1':
                return True
    return False

def copy_table(table):
    table2 = []
    for i in range(len(table)):
        ans = []
        for j in range(len(table[i])):
            ans.append(table[i][j])
        table2.append(ans)
    return table2
    

min_ans = ['0']*10000
def min_DNF2(table2, ans2):
    global min_ans
    if len(min_ans) > len(ans2):    
        for i in range(len(table2)):
            for j in range(len(table2[i])-1, -1, -1):
                if table2[i][j] != '-1':
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
                    if check_table(table):
                        min_DNF2(copy_table(table), ans.copy())
                    else:
                        if len(min_ans) > len(ans):
                            min_ans = ans
                        print(ans)
def printf_DNF(ans):
    ret_ans = ''
    for string in ans:
        ret_ans += f'({string})v'
    ret_ans = ret_ans[:len(ret_ans)-1]
    return ret_ans

def min_DNF(table):
    global min_ans
    min_ans = ['0']*10000
    min_DNF2(table, [])
    return printf_DNF(min_ans)
   
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
    table = creating_table(player_string)
    #print_table(table)
    table = reduction_table(table, player_string)
    print_table(table)
    print(min_DNF(table))
    #print(min_DNF(table, player_string))
else:
    print("Ошибка при вводе вектора!")
