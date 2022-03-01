import random

vec = '01111110'
def random_vector(vars_count):
    global vec
    len_vector = 2 ** vars_count
    count_all_vectors = 2 ** len_vector
    tmp = int(random.random()*(10**len(str(count_all_vectors)))) % count_all_vectors
    vec = str(bin(tmp)[2:])
    vec = "0" * (len_vector - len(vec)) + vec

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

# Проверка на сохраняющую 0
def check_t0(vec):
    if vec[0] == '0':
        return True
    return False

# Проверка на сохраняющую 1  
def check_t1(vec):
    if vec[-1] == '1':
        return True
    return False

# Проверка на самодвойственность
def check_s(vec):
    for char in range(int(len(vec)/2)):
        if vec[char] == vec[-1-char]:
            return False
    return True

# Проверка на линейность
def check_ln(vec):
    param = what_degree_two(len(vec))
    arr = [0]*(param+1) # Массив для проверки линейности
    arr[0] = int(vec[0])
    tmp = 1
    for i in range(1, param+1):
        t = '0'*(param - len(str(tmp))) + str(tmp)
        arr[-i] = (arr[0] + int(vec[int(t, 2)])) % 2
        tmp *= 10 
    ans_vec = str(arr[0])
    for i in range(1, len(vec)):
        t = str(bin(i)[2:])
        t = '0'*(param - len(t)) + t
        var_tmp = 0
        for j in range(1, len(arr)):
            if arr[j] == 1:
                var_tmp += int(t[j-1])
        ans_vec += str((var_tmp + arr[0]) % 2)
    if ans_vec == vec:
        return True
    return False

# Прибовляет 1 по "обычному"
def sum_vec_pp(vec):
    ans = list(vec)
    check = False
    for i in range(len(vec)-1, -1, -1):
        if vec[i] == '1':
            check = True
        if check:
            if vec[i] == '0':
                ans[i] = '1'
                ans[i+1] = '0'
                break
    return "".join(ans)

    
# Проверка на монотонность
def check_m(vec):
    param = what_degree_two(len(vec))
    mp_ans = {}
    for i in range(len(vec)):
        t = str(bin(i)[2:])
        t = '0'*(param - len(t)) + t
        mp_ans[t] = int(vec[i])

    for i in range(1, param+1):
        real = []
        nach_str = '0'*(param - len('1'*i)) + '1'*i
        while nach_str != sum_vec_pp(nach_str):
            for j in range(len(nach_str)):
                if mp_ans[nach_str[:j] + '0' + nach_str[j+1:]] > mp_ans[nach_str]:
                    return False
            nach_str = sum_vec_pp(nach_str)
        for j in range(len(nach_str)):
            if mp_ans[nach_str[:j] + '0' + nach_str[j+1:]] > mp_ans[nach_str]:
                return False
    return True

# Проверка на полноту
def check_completeness(vec):
    ch_t0 = check_t0(vec)
    ch_t1 = check_t1(vec)
    ch_s = check_s(vec)
    ch_ln = check_ln(vec)
    ch_m = check_m(vec)
    if ch_t0 or ch_t1 or ch_s or ch_ln or ch_m:
        return False
    return True

for i in range(10):
    print()
    random_vector(3)
    print(f"Ваш вектор: {vec}")
    print(f'Функция полная? {check_completeness(vec)}')
    print()


