import random
import tkinter as tk

root = tk.Tk()
root.title('Задача 4')
root.geometry('600x500+100+100')
root.resizable(False, False)

map_vector = {}  # правильные ответы
player_vector = []  # для перемешивания вектора и выдачи пользователю
vec = 0  # вектор, который выдается пользователю
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
    map_vector[i + 1] = "0" * (4 - len(tmp)) + str(tmp)
    player_vector.append([i + 1, table_p[i]])


def answer_check(player_string):
    if 2 < len(player_string) < 1:
        return False
    if 1 > int(player_string) > 16:
        return False
    for char in player_string:
        if '0' <= char <= '9':
            continue
        return False
    return True


def shuffle(player_vector):  # Перемешивает вектор с данными
    tmp = len(player_vector)
    for i in range(tmp):
        a = player_vector[i].copy()
        rand = int(random.random() * 100) % tmp
        player_vector[i] = player_vector[rand]
        player_vector[rand] = a


def help():  # Для вывода пользователю на экран таблицы с данными
    global player_vector
    global vec
    vec = int(random.random() * 100) % len(player_vector)
    shuffle(player_vector)
    ans = "Выберите имя для функции: " + map_vector[player_vector[vec][0]] + "\n"
    for i in range(1, 17):
        ans += str(i) + ") " + player_vector[i - 1][1] + "\n"
    return ans


def btn_func():
    user_entry = entry.get()
    if user_entry:
        if map_vector[player_vector[vec][0]] == map_vector[player_vector[int(user_entry) - 1][0]]:
            ans_label.configure(text="Ваш ответ верный", fg='green')
        else:
            ans_label.configure(text="Ваш ответ неверный", fg='red')
    else:
        ans_label.configure(text="Вы ввели неверные данные!", fg='red')
    greet_label.configure(text=help())


top_frame = tk.Frame(root, pady=6)
bottom_frame = tk.Frame(root)

greet_label = tk.Label(top_frame, text=help(), font=('Arial', 14, 'normal'), justify='left')
greet_label.pack(pady=6)

top_frame.pack()

ans_label = tk.Label(top_frame, text='', font=('Arial', 14, 'normal'))
ans_label.pack()

entry = tk.Entry(bottom_frame, font=('Arial', 14, 'normal'))
entry.pack(side='left', padx=10)

button_submit = tk.Button(bottom_frame, text='Ответить',  font=('Arial', 12, 'normal'), bg='#d4d4d4', command=btn_func)
button_submit.pack(side='left')

bottom_frame.pack(side='top')

root.mainloop()
