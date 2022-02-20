
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
    
def check_vector(vec):
    if len(vec) < 2:
        return False
    for char in vec:
        if "0"<= char <= "1":
            continue
        return False
    return True

player_string = input("Введите вектор: ")
player_string = player_string.replace(' ', '')

if degree_two(len(player_string)) and check_vector(player_string):
    tmp = 0
    deg_t = what_degree_two(len(player_string))
    ans = ""
    for char in player_string:
        if char == '0':
            t = '0'*(deg_t - len(str(bin(tmp)[2:]))) + str(bin(tmp)[2:])
            num_arg = 1
            ans += "("
            for i in t:
                if i == '1':
                    ans += f"-x{num_arg}"
                else:
                    ans += f"x{num_arg}"
                ans += "v"
                num_arg += 1
            ans = ans[:len(ans)-1]
            ans += ")&"
        tmp += 1
    ans = ans[:len(ans)-1]
    print("СКНФ: "+ ans)
else:
    print("Ошибка при вводе вектора!")
