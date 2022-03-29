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

#Расстояние между наборами
def distance(n1, n2):
    tmp = -1
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            if tmp != -1:
                return -1
            tmp = i
    return tmp

#Создание таблицы
def all_table(vec):
    global columns
    ans = []
    check_ans = []
    ret_ans = set()
    for i in range(what_degree_two(len(vec))+1):
        ans.append([])
        check_ans.append([])
    for i in range(len(vec)):
        if vec[i] == '0':
            continue
        tmp_vec = str(bin(i)[2:])
        tmp_vec = "0"*(what_degree_two(len(vec))-len(tmp_vec)) + tmp_vec
        ans[tmp_vec.count('1')].append(tmp_vec)
        check_ans[tmp_vec.count('1')].append(0)
    for i in range(len(ans)-1):
        for j in range(len(ans[i])):
            for qj in range(len(ans[i+1])):
                len_n = distance(ans[i][j], ans[i+1][qj])
                if len_n != -1:
                    string = ans[i][j][:len_n] + '-' + ans[i][j][len_n+1:]
                    ret_ans.add(string)
                    check_ans[i][j] = 1
                    check_ans[i+1][qj] = 1
    for i in range(len(check_ans)):
        for j in range(len(check_ans[i])):
            if check_ans[i][j] == 0:
                columns.append(ans[i][j])
    return list(ret_ans)

#Следующее значение
def next_feature(string):
    ans = list(string)
    p = -1
    check = False
    for i in range(len(string)-1, -1, -1):
        if string[i] == '-':
            ans[i] = '*'
            p += 1
            check = True
        if check:
            if string[i] == '*':
                ans[i] = '-'
                ans[i+1] = '*'
                check = False
                break
    if check:
        return string
    for i in range(len(string)-1, -1, -1):
        if p <= 0:
            break
        ans[i] = '-'
        p -= 1
    return "".join(ans)

#Сортировка таблицы значений
def sort_table(table, kol):
    ret_ans = []
    len_table = len(table[0])
    tr_pask = pask_tr(len_table)
    string = '*'*(len_table-kol) + '-'*kol
    for q in range(tr_pask[kol]):
        ans = []
        for i in range(len(table)):
            tmp = 0
            for char in range(len(string)):
                if string[char] == table[i][char]:
                    tmp += 1
            if tmp == kol:
                ans.append(table[i])
        ret_ans.append(ans)
        string = next_feature(string)
    return ret_ans
            

#Сокращение таблицы
def reduction(table):
    global columns
    check_ans = []
    ret_ans = set()
    for i in range(len(table)):
        tmp = []
        for j in range(len(table[i])):
            tmp.append(0)
        check_ans.append(tmp)
    for i in range(len(table)):
        for j in range(len(table[i])):
            for qj in range(j+1, len(table[i])):
                len_n = distance(table[i][j], table[i][qj])
                if len_n != -1:
                    string = table[i][j][:len_n] + '-' + table[i][j][len_n+1:]
                    check_ans[i][j] = 1
                    check_ans[i][qj] = 1
                    ret_ans.add(string)
    for i in range(len(check_ans)):
        for j in range(len(check_ans[i])):
            if check_ans[i][j] == 0:
                columns.append(table[i][j])
    return list(ret_ans)
                

###Красивый вывод таблицы
##def print_table(table):
##    for i in range(len(table)):
##        print(table[i])

#Cоздание столбцов
def pack_columns(player_string):
    table = all_table(player_string)
    kol = 1
    while len(table) != 0:
        table = sort_table(table, kol)
        table = reduction(table)
        kol += 1
        
#Склейка колонок и столбцев
def creating_table(vec):
    global columns
    columns = []
    pack_columns(vec)
    lines = []
    for i in range(len(vec)):
        if vec[i] == '0':
            continue
        tmp_vec = str(bin(i)[2:])
        tmp_vec = "0"*(what_degree_two(len(vec))-len(tmp_vec)) + tmp_vec
        lines.append(tmp_vec)
    table = []
    tmp = ['-1']
    for j in range(len(columns)):
        tmp.append(columns[j])
    table.append(tmp)
    for i in range(len(lines)):
        tmp = [lines[i]]
        for j in range(len(columns)):
            tmp.append('-1')
        table.append(tmp)
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            n1 = table[0][j]
            n2 = table[i][0]
            check = True
            for char in range(len(n1)):
                if n1[char] == '-':
                    continue
                if n1[char] != n2[char]:
                    check = False
                    break
            if check:
                table[i][j] = '0'
    return table

#Создание копии талицы
def copy_table(table):
    table2 = []
    for i in range(len(table)):
        ans = []
        for j in range(len(table[i])):
            ans.append(table[i][j])
        table2.append(ans)
    return table2

#Выбор из таблицы значений для мин. ДНФ
def table_analysis(table):
    ret_ans = []
    for i in range(1, len(table)):
        t = 0
        id_j = -1
        for j in range(1, len(table[i])):
            if table[i][j] == '0':
                t += 1
                id_j = j
                if t > 1:
                    break
        if t == 1 and table[i][0] != '-1':
            for qi in range(1, len(table)):
                if i != qi and table[qi][id_j] == table[i][id_j]:
                    for qj in range(1, len(table[qi])):
                        table[qi][qj] = '-1'
                    table[qi][0] = '-1'
            table[i][id_j] = '-1'
            table[i][0] = '-1'
            ret_ans.append(table[0][id_j])  
    return ret_ans

#Проверка таблицы на то, что значение еще существует
def check_table(table):
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            if table[i][j] != '-1':
                return True
    return False

set_all_ans = set()
min_ans = ['0']*10000
#Перебор всех значений в таблице и выбор минимальной ДНФ
def min_DNF2(table2, ans2, step2):
    global set_all_ans
    global min_ans
    if len(min_ans) > len(ans2):
        for i in range(1, len(table2)):
            for j in range(1, len(table2[i])):
                if table2[i][j] != '-1':
                    if step2 == 1 and table2[0][j] in set_all_ans:
                        continue
                    set_all_ans.add(table2[0][j])
                    ans = []
                    for q in range(len(ans2)):
                        ans.append(ans2[q])
                    table = copy_table(table2)
                    for qi in range(1, len(table)):
                        if i != qi and table[i][j] == table[qi][j]:
                            for qj in range(1, len(table[qi])):
                                table[qi][qj] = '-1'
                    ans.append(table[0][j])
                    for qj in range(1, len(table[qi])):
                        table[i][qj] = '-1'
                    if check_table(table):
                        min_DNF2(copy_table(table), ans.copy(), step2+1)
                    else:
                        if len(min_ans) > len(ans):
                            min_ans = ans
                        #print(ans)

#Перевод из массива в строку для пользователя                        
def printf_DNF(ans):
    ret_ans = ''
    ans2 = []
    for i in range(len(ans)):
        string = ans[i]
        new_string = ''
        for q in range(len(string)):
            if string[q] != '-' and string[q] == '0':
                new_string += f'-x{q+1}'
            elif string[q] != '-' and string[q] == '1':
                new_string += f'x{q+1}'
        ans2.append(new_string)
    for string in ans2:
        ret_ans += f'({string})v'
    ret_ans = ret_ans[:len(ret_ans)-1]
    return ret_ans

#Упаковывающая функции для вызова минимальной ДНФ
def min_DNF(table, ans):
    global min_ans
    global set_all_ans
    set_all_ans = set()
    min_ans = ['0']*10000
    min_DNF2(table, ans, 1)
    if len(min_ans) == len(['0']*10000):
        min_ans = ans
    return printf_DNF(min_ans)

columns = []

player_string = input("Введите вектор: ")
player_string = player_string.replace(' ', '')
        
if check_vector(player_string):
    table = creating_table(player_string)
    ans = table_analysis(table)
    print(min_DNF(table, ans))
else:
    print("Ошибка при вводе вектора!")
