def string_standard(player_string):
    player_string = player_string.replace(' ', '').lower()
    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')
    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')
    player_string = player_string.replace('x', '')
    player_string = player_string.split('v')
    return player_string

def degree_two(number): # проверяет является ли число степенью двойки
    tmp = 1
    while tmp < number:
        tmp *= 2
    if number == tmp:
        return True
    else:
        return False

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

def sdnf(player_string, ):
    tmp = 0
    deg_t = what_degree_two(len(player_string))
    ans = ""
    for char in player_string:
        if char == '1':
            t = '0'*(deg_t - len(str(bin(tmp)[2:]))) + str(bin(tmp)[2:])
            num_arg = 1
            ans += "("
            for i in t:
                if i == '0':
                    ans += f"-x{num_arg}"
                else:
                    ans += f"x{num_arg}"
                num_arg += 1
            ans += ")v"
        tmp += 1
    ans = ans[:len(ans)-1]
    return ans

def check_vector(vec):
    if len(vec) < 2:
        return False
    for char in vec:
        if "0"<= char <= "1":
            continue
        return False
    return True

def reduction(player_string, rek):
    s = player_string
    for q in range(rek):
        ans = set()
        tmp_ans = []
        for ti in range(len(s)):
            tmp_ans.append(0)
        for ti in range(len(s)):
            map_tmp1 = []
            zn = 1
            for char in s[ti]:
                if char == '-':
                    zn = -1
                    continue
                map_tmp1.append(zn*int(char))
                zn = 1
            for tj in range(ti+1,len(s), 1):
                map_tmp2 = []
                zn = 1
                for char in s[tj]:
                    if char == '-':
                        zn = -1
                        continue
                    map_tmp2.append(zn*int(char))
                    zn = 1
                if len(map_tmp2) == len(map_tmp1):
                    razl = 0
                    for i in range(len(map_tmp1)):
                        if abs(map_tmp2[i]) != abs(map_tmp1[i]):
                            razl = -1
                            break
                        if map_tmp2[i] != map_tmp1[i]:
                            razl += 1
                    if razl == 1:
                        s1 = ""
                        for i in range(len(map_tmp1)):
                            if map_tmp2[i] != map_tmp1[i]:
                                continue
                            s1 += str(map_tmp1[i])
                        tmp_ans[ti] = 1
                        tmp_ans[tj] = 1
                        ans.add(s1)
        for i in range(len(s)):
            if 0 == tmp_ans[i]:
                ans.add(s[i])
        s = list(ans)
    ans_string = ""
    for i in range(len(s)):
        zn = ""
        ans_string += "("
        for j in s[i]:
            if j == '-':
                zn = "-"
                continue
            ans_string += zn + "x" + j
            zn = ""
        ans_string += ")"
        ans_string += "v"
    return ans_string[:len(ans_string)-1]
    
    

player_string = input("Введите вектор: ")
player_string = player_string.replace(' ', '')

if degree_two(len(player_string)) and check_vector(player_string):
    s = string_standard(sdnf(player_string))
    ans = reduction(s, what_degree_two(len(player_string)))
    print(ans)  
else:
    print("Ошибка при вводе вектора!")
