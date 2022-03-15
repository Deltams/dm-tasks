import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 7')
root.geometry('600x500+100+100')
root.resizable(False, False)
try:
    root.iconbitmap('icon.ico')
except:
    pass

d = {
    'x': 'x1',
    'y': 'x2',
    'z': 'x3',
    'u': 'x4',
}

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

def string_standard2(player_string):
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
    ans = []
    tmp = 1
    string = ''
    for i in player_string:
        if i == '-' and tmp != 0:
            string += '-'
            continue
        if i == 'v':
            tmp = 1
            continue
        tmp -= 1
        if tmp == -1:
            ans.append(string)
            string = i
            if i == '-':
                tmp = 1
            else:
                tmp = 0
        else:
            string += i
    ans.append(string)
    return ans


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


def knf_check(player_string, vec):
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


def knf_true(player_string):
    global vec
    param = string_standard(player_string)
    vec_mass = []
    vec_ans = []
    for i in range(len(param)):
        vec_mass.append("")
    for i in range(len(vec)):
        vec_ans.append("1")
        t = str(bin(i)[2:])
        t = "0" * (what_degree_two(len(vec)) - len(t)) + t
        for tm in range(len(param)):
            zn = 1
            tmpp = 0
            for j in param[tm]:
                if j == '-':
                    zn = -1
                    continue
                if t[int(j) - 1] == '1' and zn == -1:
                    tmpp += 0
                elif t[int(j) - 1] == '0' and zn == -1:
                    tmpp = 1
                else:
                    tmpp += int(t[int(j) - 1])
                    if tmpp == 2:
                        tmpp = 1
                zn = 1
            vec_mass[tm] += str(tmpp)

    for string in range(len(vec_mass)):
        for j in range(len(vec_mass[string])):
            if vec_mass[string][j] == '0':
                vec_ans[j] = '0'
    return "".join(vec_ans)


def send_answer():
    player_string = entry.get()
    vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(0, len(tmp)):
        vec += tmp[i]
    if knf_check(string_standard2(player_string), vec):
        ans_vec = knf_true(player_string)
        if vec == ans_vec:
            error_label.configure(text='Введеная КНФ верная', fg='green')
        else:
            error_label.configure(text='Введеная КНФ неверная!', fg='red')
    elif len(player_string.replace(' ', '')) == 0 and vec.count('1') == len(vec):
        error_label.configure(text='Введеная КНФ верная', fg='green')
    else:
        error_label.configure(text='Неверный ввод!!!', fg='red')

    button_submit['state'] = 'disabled'
    entry['state'] = 'disabled'
    go_next_button.pack(side='left', padx=5)
    remake_button.pack(side='left', padx=5)


def go_next():
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    error_label.configure(text='')
    vector_label.configure(text=random_vector(n_param.get()))


def remake_task():
    button_submit['state'] = 'normal'
    entry['state'] = 'normal'
    entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    error_label.configure(text='')


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = '\n\nПример ввода:\n\n'
    ans += '(x1 v x2)*(x3 v -x4)\n\n'
    ans += 'x1 v x2x3 v -x4\n\n'
    ans += 'x1vx2x3v-x4\n\n'
    ans += '(x1v-x2vx3)*(-x1vx2v-x3)&(-x1v-x2vx3)\n\n'
    ans += "Приятной игры ;)\n\n\n"
    label = tk.Label(child_root, text=ans, font=('Arial', 14, 'normal'), justify='left').pack()


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


greet_label = tk.Label(root, text='Напишите КНФ для вектора:', font=('Arial', 16, 'normal'))
greet_label.pack(pady=10)

vector_label = tk.Label(root, text=random_vector(n_param.get()), font=('Arial', 16, 'normal'))
vector_label.pack()

error_label = tk.Label(root, text='', font=('Arial', 14, 'normal'))
error_label.pack()

entry = tk.Entry(root, font=('Arial', 14, 'normal'), width=40)
entry.pack()

fr = tk.Frame()
button_submit = tk.Button(fr, text='Ответить', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=10)

go_next_button = tk.Button(fr, text='Новое задание', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=go_next)
remake_button = tk.Button(fr, text='Перепройти', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=remake_task)
fr.pack()


button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')

draw_menu()

root.mainloop()
os.startfile('BoolGame')
