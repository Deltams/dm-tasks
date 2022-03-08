import random
import tkinter as tk

root = tk.Tk()
root.title('Задача 6')
root.geometry('600x500+100+100')
root.resizable(False, False)

n_param = tk.IntVar(value=3)

def random_vector(vars_count):
    global vec
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


def string_standard(player_string):
    player_string = player_string.replace(' ', '').lower()
    player_string = player_string.replace('&', '')
    player_string = player_string.replace('*', '')
    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')
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

    player_string = player_string.replace('(', '')
    player_string = player_string.replace(')', '')

    for i in range(1, len(player_string)):  # Проверка повторов символов (Перемер xx, **, &&, 11, 22, 12)
        if player_string[i - 1] == player_string[i] \
                or ('1' <= player_string[i - 1] <= '9' \
                    and '1' <= player_string[i] <= '9'):
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

    return True


def dnf_true(player_string):
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
    # print(vec_mass)

    for string in range(len(vec_mass)):
        for j in range(len(vec_mass[string])):
            if vec_mass[string][j] == '1':
                vec_ans[j] = '1'
    return "".join(vec_ans)


def send_answer():
    player_string = entry.get()
    vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(0, len(tmp)):
        vec += tmp[i]
    if dnf_check(player_string, vec):
        ans_vec = dnf_true(player_string)
        if vec == ans_vec:
            error_label.configure(text='Введеная ДНФ верная', fg='green')
        else:
            error_label.configure(text='Введеная ДНФ неверная!', fg='red')
    elif len(player_string.replace(' ', '')) == 0 and vec.count('0') == len(vec):
        error_label.configure(text='Введеная ДНФ верная', fg='green')
    else:
        error_label.configure(text='Неверный ввод!!!', fg='red')

    button_submit['state'] = 'disabled'
    entry['state'] = 'disabled'
    go_next_button.pack()


def go_next():
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    error_label.configure(text='')
    vector_label.configure(text=random_vector(n_param.get()))


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\n\nПример ввода данных:\n\n"
    ans += '(-x1*-x2&x3)v(-x1x2-x3)V(-x1x2x3)v(x1-x2-x3)v(x1-x2x3)v(x1x2-x3)\n\n\n'
    ans += '-x1*-x2&x3v-x1x2-x3V-x1x2x3vx1-x2-x3vx1-x2x3vx1x2-x3\n\n\n'
    ans += '-x1*-x2&x3v-x1x2-x3V-x1x2x3vx1-x2-x3vx1-x2x3vx1x2-x3\n\n\n'
    ans += '-x1*-x2&x3 v -x1x2-x3 V -x1x2x3 v x1-x2-x3 v x1-x2x3 v x1x2-x3\n\n\n'
    ans += "Приятной игры ;)\n\n\n\n"
    label = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()


def draw_menu():
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_radiobutton(label='1 переменная', value=1, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='2 переменных', value=2, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='3 переменных', value=3, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='4 переменных', value=4, variable=n_param, command=go_next)
    file_menu.add_radiobutton(label='5 переменных', value=5, variable=n_param, command=go_next)
    menu_bar.add_cascade(label='Настройки', menu=file_menu)
    root.configure(menu=menu_bar)


greet_label = tk.Label(root, text='Напишите ДНФ для вектора:', font=('Arial', 16, 'normal'))
greet_label.pack(pady=10)

vector_label = tk.Label(root, text=random_vector(n_param.get()), font=('Arial', 16, 'normal'))
vector_label.pack()

error_label = tk.Label(root, text='', font=('Arial', 14, 'normal'))
error_label.pack()

entry = tk.Entry(root, font=('Arial', 14, 'normal'), width=40)
entry.pack()

button_submit = tk.Button(root, text='Ответить', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=20)

go_next_button = tk.Button(root, text='Новое задание', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=go_next)

button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')

draw_menu()
root.mainloop()
