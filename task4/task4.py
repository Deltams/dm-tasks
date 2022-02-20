import random

map_vector = {} # правильные ответы
player_vector = [] # для перемешивания вектора и выдачи пользователю
vec = 0 # вектор, который выдается пользователю
table_p = [
    "Константа нуля",
    "Конъюкция",
    "Запрет по X_2",
    "Переменная X_1",
    "Запрет по X_1",
    "Переменная X_2",
    "Сложение по модулю 2(xor)",
    "Дизъюнкция",
    "Стрелка Пирса",
    "Эквивалентность",
    "Отрицание X_2",
    "Импликация от X_2 к X_1",
    "Отрицание X_1",
    "Импликация от X_1 к X_2",
    "Штрих Шеффера",
    "Константа единицы"
           ]

for i in range(16):
    tmp = bin(i)[2:]
    map_vector[i+1] = "0"*(4 - len(tmp)) + str(tmp)
    player_vector.append([i+1, table_p[i]])
    
def answer_check(player_string):
    if 2 < len(player_string) < 1:
        return False
    if 1 > int(player_string) > 16:
        return False
    for char in player_string:
        if '0'<=char<='9':
            continue
        return False
    return True

def shuffle(player_vector): # Перемешивает вектор с данными
    tmp = len(player_vector)
    for i in range(tmp):
        a = player_vector[i].copy()
        rand = int(random.random()*100) % tmp
        player_vector[i] = player_vector[rand]
        player_vector[rand] = a

def help(): # Для вывода пользователю на экран таблицы с данными
    global player_vector
    global vec
    vec = int(random.random()*100) % len(player_vector)
    shuffle(player_vector)
    ans = "Выберите имя для функции: " + map_vector[player_vector[vec][0]] + "\n"
    for i in range(1, 17):
        ans += str(i) + ") " + player_vector[i-1][1] + "\n"
    return ans

print(help() + "\n") # Запускать, когда нужно выдать новый вектор
s = input("Введите номер: ")
s = s.replace(' ', '')

if answer_check(s):
    if map_vector[player_vector[vec][0]] == map_vector[player_vector[int(s)-1][0]]:
        print("Ваш ответ верный")
    else:
        print("Ваш ответ неверный")
else:
    print("Вы ввели неверные данные!")
