import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 4')
root.geometry('600x580+100+100')
root.resizable(False, False)

try:
    root.iconbitmap('icon.ico')
except:
    pass

map_vector = {}  # правильные ответы
player_vector = []  # для перемешивания вектора и выдачи пользователю
vec = 0  # вектор, который выдается пользователю
table_p = [
    "Константа нуля (0)",
    "Конъюкция (&)",
    "Коимпликация (\u219A)",
    "Переменная x\u2081",
    "Обратная коимпликация (\u219B)",
    "Переменная x\u2082",
    "Сложение по модулю 2 (\u2295)",
    "Дизъюнкция (\u2228)",
    "Стрелка Пирса (\u2193)",
    "Эквивалентность (\u2261)",
    "Отрицание x\u2082 (\u00ACx\u2082)",
    "Обратная импликация (\u2190)",
    "Отрицание x\u2081 (\u00ACx\u2081)",
    "Импликация (\u2192)",
    "Штрих Шеффера (\u2191)",
    "Константа единицы (1)"
]

def read_file():
    s = ''
    file = os.path.abspath(os.path.join('seve.txt',"../../..")) + '\menu\seve.txt'
    with open(file, 'r') as f:
        s = f.readline()
        s = s.replace(' ', '').split(',')
    return s

def write_file(s):
    file = os.path.abspath(os.path.join('seve.txt',"../../..")) + '\menu\seve.txt'
    with open(file, 'w') as f:
        ans = ''
        for i in s:
            ans += i + ', '
        ans = ans[:len(ans)-2]
        f.write(ans)

for i in range(16):
    tmp = bin(i)[2:]
    map_vector[i + 1] = "0" * (4 - len(tmp)) + str(tmp)
    player_vector.append([i + 1, table_p[i]])

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
        try:
            if map_vector[player_vector[vec][0]] == map_vector[player_vector[int(user_entry) - 1][0]]:
                ans_label.configure(text="Ваш ответ верный", fg='green')

                go_next_button.pack(side='left', padx=5)
            else:
                ans_label.configure(text="Ваш ответ неверный", fg='red')

                go_next_button.pack(side='left', padx=5)
                remake_button.pack(side='left', padx=5)
                ans_button.pack(side='left', padx=5)

        except Exception:
            ans_label.configure(text="Вводите числа от 1 до 16!", fg='red')

            go_next_button.pack(side='left', padx=5)
            remake_button.pack(side='left', padx=5)
            ans_button.pack(side='left', padx=5)
    else:
        ans_label.configure(text="Вы ввели некорректные данные!", fg='red')

        go_next_button.pack(side='left', padx=5)
        remake_button.pack(side='left', padx=5)
        ans_button.pack(side='left', padx=5)
    button_submit['state'] = 'disabled'
    entry['state'] = 'disabled'


def print_ans():
    global player_vector
    global vec
    ans = table_p[player_vector[vec][0] - 1]
    ans_label.configure(text=f'{ans}', fg='green')
    ans_button.pack_forget()


def go_next():
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'

    greet_label.configure(text=help())
    ans_label.configure(text='')
    entry.delete(0, 'end')

    go_next_button.pack_forget()
    remake_button.pack_forget()
    ans_button.pack_forget()


def remake_button():
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    ans_label.configure(text='')
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    ans_button.pack_forget()

def onclick(event):
    btn_func()
        

top_frame = tk.Frame(root, pady=6)
bottom_frame = tk.Frame(root)

greet_label = tk.Label(top_frame, text=help(), font=('Arial', 14, 'normal'), justify='left')
greet_label.pack()

top_frame.pack()

ans_label = tk.Label(top_frame, text='', font=('Arial', 14, 'normal'))
ans_label.pack()

entry = tk.Entry(bottom_frame, font=('Arial', 14, 'normal'))
entry.pack(side='left', padx=10)

button_submit = tk.Button(bottom_frame, text='Ответить', font=('Arial', 12, 'normal'), bg='#d4d4d4', command=btn_func)
button_submit.pack(side='left')

bottom_frame.pack(side='top')

fr = tk.Frame(root)
go_next_button = tk.Button(fr, text='Новое задание', font=('Arial', 12, 'normal'), bg='#d4d4d4', command=go_next)
remake_button = tk.Button(fr, text='Перепройти', font=('Arial', 12, 'normal'), bg='#d4d4d4', command=remake_button)
ans_button = tk.Button(fr, text='Показать ответ', font=('Arial', 12, 'normal'), bg='#d4d4d4', command=print_ans)
fr.pack(pady=10)

root.bind('<Return>', onclick)

root.mainloop()

s = read_file()
s[0] = '0'
write_file(s)
