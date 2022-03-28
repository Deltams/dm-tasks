import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 6')
root.geometry('600x300+350+150')
root.resizable(False, False)

try:
    root.iconbitmap('icon.ico')
except:
    pass

n_param = tk.IntVar(value=3)

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

def random_vector(vars_count):
    len_vector = 2 ** vars_count
    count_all_vectors = 2 ** len_vector
    tmp = int(random.random() * (10 ** len(str(count_all_vectors)))) % count_all_vectors
    vec = str(bin(tmp)[2:])
    vec = "0" * (len_vector - len(vec)) + vec
    ans = ''
    for i in range(1, len(vec) + 1):
        ans += vec[i - 1]
        if i % 4 == 0:
            ans += ' '
    return ans

def string_standard2(player_string):
    player_string = player_string.lower()
    player_string = player_string.replace('x\u2081', 'x1')
    player_string = player_string.replace('x\u2082', 'x2')
    player_string = player_string.replace('x\u2083', 'x3')
    player_string = player_string.replace('x\u2084', 'x4')
    player_string = player_string.replace('x\u2085', 'x5')
    player_string = player_string.replace('x\u2086', 'x6')
    player_string = player_string.replace('x\u2087', 'x7')
    player_string = player_string.replace('x\u2088', 'x8')
    player_string = player_string.replace('x\u2089', 'x9')
    player_string = player_string.replace('x', 'x1')
    player_string = player_string.replace('y', 'x2')
    player_string = player_string.replace('z', 'x3')
    player_string = player_string.replace('u', 'x4')
    for i in range(1, 10):
        player_string = player_string.replace(f'{1}{i}', f'{i}')
    return player_string

def string_standard(player_string):
    player_string = player_string.replace(' ', '').lower()
    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')
    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')
    player_string = string_standard2(player_string)
    player_string = player_string.replace('x', '')
    player_string = player_string.split('v')
    return player_string


def what_degree_two(number):  # В какую степень двойки возведено число; -1: не является степенью двойки
    tmp = 1
    ans = 0
    while tmp < number:
        tmp *= 2
        ans += 1
    if number == tmp:
        return ans
    else:
        return -1


def dnf_check(player_string, vec):
    global set_param

    player_string = player_string.replace(' ', '').lower()

    if len(player_string) == 0 or len(player_string) == 1 and 'x' != player_string[0]:
        return False

    # Проверка в начале есть ли недопустимый символ
    if player_string[0] != '(' and player_string[0] != '-' and 'x' != player_string[0]:
        return False

    # Проверка в конце есть ли недопустимый символ
    if player_string[-1] != ')' and '1' > player_string[-1] > '9':
        return False

    # Проверяет переменные, чтоб они не превышали допустимые значения
    for char in player_string:
        if '1' <= char <= '9':
            if char > str(what_degree_two(len(vec))):
                return False

    for char in player_string:  # Проверка на допустимые символы
        if char == '*' or char == 'v' \
                or char == '&' or 'x' == char \
                or char == '(' or char == ')' \
                or char == '-' or '1' <= char <= '9':
            continue
        return False

    psp = 0
    for char in player_string:  # Проверка ПСП (Если конечно скобки есть)
        if char == '(':
            psp += 1
        elif char == ')':
            psp -= 1
            if psp < 0:
                return False
    if psp > 0:
        return False

    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')

    for i in range(1, len(player_string)):  # Проверка повторов символов (Перемер xx, **, &&, 11, 22, 12)
        if player_string[i - 1] == player_string[i] \
                or ('1' <= player_string[i - 1] <= '9' and '1' <= player_string[i] <= '9'):
            return False

    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')

    stack_param = 0
    for i in range(0, len(player_string)):  # Проверка на правильные переменные переменные
        if player_string[i] == '-':
            continue
        elif '1' <= player_string[i] <= '9':
            if stack_param == 0:
                return False
            stack_param -= 1
        elif player_string[i] != 'v' \
                and player_string[i] == 'x':
            stack_param = 1
        else:
            stack_param = 0
        if stack_param < 0:
            return False

    player_string = player_string.split('v')
    for i in range(len(player_string)):
        for j in range(1, 10):
            if player_string[i].count(f'x{j}') > 1:
                return False
    
    return True


def dnf_true(player_string, vec):
    param = string_standard(player_string)
    vec_mass = []
    vec_ans = []
    for i in range(len(param)):
        vec_mass.append("")
    for i in range(len(vec)):
        vec_ans.append("0")
        t = str(bin(i)[2:])
        t = "0" * (what_degree_two(len(vec)) - len(t)) + t
        for tm in range(len(param)):
            zn = 1
            tmpp = 1
            for j in param[tm]:
                if j == '-':
                    zn = -1
                    continue
                if t[int(j) - 1] == '1' and zn == -1:
                    tmpp *= 0
                elif t[int(j) - 1] == '0' and zn == -1:
                    tmpp *= 1
                else:
                    tmpp *= int(t[int(j) - 1])
                zn = 1
            vec_mass[tm] += str(tmpp)

    for string in range(len(vec_mass)):
        for j in range(len(vec_mass[string])):
            if vec_mass[string][j] == '1':
                vec_ans[j] = '1'
    return "".join(vec_ans)


def send_answer():
    global ch_entry
    player_string = entry.get()
    vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(0, len(tmp)):
        vec += tmp[i]
    if dnf_check(string_standard2(player_string), vec):
        ans_vec = dnf_true(player_string, vec)
        if vec == ans_vec:
            error_label.configure(text='Введенная ДНФ верная', fg='green')
        else:
            error_label.configure(text='Введенная ДНФ неверная!', fg='red')
    elif len(player_string.replace(' ', '')) == 0 and vec.count('0') == len(vec):
        error_label.configure(text='Введенная ДНФ верная', fg='green')
    elif len(player_string.replace(' ', '')) == 1 and int(player_string.replace(' ', '')) == 1:
        error_label.configure(text='Введенная ДНФ верная', fg='green')
    else:
        error_label.configure(text='Неверный ввод!!!', fg='red')

    ch_entry = True
    button_submit['state'] = 'disabled'
    entry['state'] = 'disabled'
    go_next_button.pack(side='left', padx=5)
    remake_button.pack(side='left', padx=5)


def go_next():
    global ch_entry
    ch_entry = False
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    error_label.configure(text='')
    vector_label.configure(text=random_vector(n_param.get()))
    root.after(500, lambda:check_entry())


def remake_task():
    global ch_entry
    ch_entry = False
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    error_label.configure(text='')
    root.after(500, lambda:check_entry())


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\n\nПример ввода данных:\n\n"
    ans += '(-x1*-x2&x3)v(-x1x2-x3)V(-x1x2x3)v(x1-x2-x3)v(x1-x2x3)v(x1x2-x3)\n\n\n'
    ans += '-x1*-x2&x3v-x1x2-x3V-x1x2x3vx1-x2-x3vx1-x2x3vx1x2-x3\n\n\n'
    ans += '-x*-y&zv-xy-zV-xyzvx-y-zvx-yzvxy-z\n\n\n'
    ans += '-x*-y&z v -xy-z V -xyz v x-y-z v x-yz v xy-z\n\n\n'
    ans += "Приятной игры ;)\n\n\n\n"
    label = tk.Label(child_root, text=ans, font=('Times New Roman', 14, 'normal'), justify='left').pack()


def draw_menu():
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_radiobutton(label='1 переменная', value=1, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='2 переменных', value=2, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='3 переменных', value=3, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='4 переменных', value=4, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='5 переменных', value=5, variable=n_param, command=go_next)
    menu_bar.add_cascade(label='Настройки', menu=file_menu)
    menu_bar.add_cascade(label='Справка', command=open_child_root)
    root.configure(menu=menu_bar)

def onclick(event):
    send_answer()

ch_entry = False
def check_entry():
    global ch_entry
    if ch_entry:
        return
    player_string = entry.get()
    player_string = player_string.lower()
    player_string = player_string.replace('x1', 'x\u2081')
    player_string = player_string.replace('x2', 'x\u2082')
    player_string = player_string.replace('x3', 'x\u2083')
    player_string = player_string.replace('x4', 'x\u2084')
    player_string = player_string.replace('x5', 'x\u2085')
    player_string = player_string.replace('x6', 'x\u2086')
    player_string = player_string.replace('x7', 'x\u2087')
    player_string = player_string.replace('x8', 'x\u2088')
    player_string = player_string.replace('x9', 'x\u2089')
    message = tk.StringVar()
    message.set(player_string)
    entry.configure(textvariable=message)
    root.after(500, lambda:check_entry())
    

greet_label = tk.Label(root, text='Напишите ДНФ для вектора:', font=('Times New Roman', 16, 'normal'))
greet_label.pack(pady=10)

vector_label = tk.Label(root, text=random_vector(n_param.get()), font=('Times New Roman', 16, 'normal'))
vector_label.pack()

error_label = tk.Label(root, text='', font=('Times New Roman', 14, 'normal'))
error_label.pack()

entry = tk.Entry(root, font=('Roboto', 16, 'normal'), width=40)
entry.pack()

fr = tk.Frame(root)
button_submit = tk.Button(fr, text='Ответить', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=10)
go_next_button = tk.Button(fr, text='Новое задание', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=go_next)
remake_button = tk.Button(fr, text='Пройти заново', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=remake_task)
fr.pack()

draw_menu()
root.bind('<Return>', onclick)
root.after(500, lambda:check_entry())
root.mainloop()

s = read_file()
s[2] = '0'
write_file(s)
