import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 5')
root.geometry('600x300+350+150')
root.resizable(False, False)
try:
    root.iconbitmap('icon.ico')
except:
    pass

n_param = tk.IntVar(value=3)

dict_vector = {}  # Словарь ответов для пользователя; Автоматически заполняется в all_vector
list_vector = []

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

def residual(vec, k, n):  # остаточная по вектору; vec - vector; k - какая остаточная; n - переменная
    ans = ""
    tmp = len(vec) / 2 ** n  # размер коробки
    i = k * tmp
    while i < len(vec):
        ans = ans + vec[int(i):int(i) + int(tmp)]
        i = i + tmp * 2
    return ans


def all_vector(vars_count): 
    global dict_vector
    global list_vector
    dict_vector = {}
    list_vector= []

    len_vector = 2 ** vars_count  # len(vec)
    tmp = 0
    count_all_vectors = 2 ** len_vector
    for i in range(count_all_vectors):
        vec = str(bin(tmp)[2:])
        vec = "0" * (len_vector - len(vec)) + vec  # незначащие нули в начало. vec - временно хранится один из векторов
        fict_var = ""  # Фиктивная переменная
        sysh_var = ""  # Существенная переменная
        for j in range(1, vars_count + 1):
            s1 = residual(vec, 0, j)
            s2 = residual(vec, 1, j)
            if s1 == s2:
                fict_var = fict_var + str(j)
            else:
                sysh_var = sysh_var + str(j)
        if len(fict_var) and len(sysh_var) or n_param.get() == 1:
            dict_vector[vec] = [sysh_var, fict_var]
            list_vector.append(vec)
            if len(list_vector) == 100:
                break
        tmp += 1


def check_data(s):  # Проверка введеных данных пользователя
    for i in s:
        if i == ' ' or '0' <= i <= '9':
            continue
        return False
    return True


# Проверка ответа пользователя fic_sysh - 0: существенная пременная; 1: Фиктивная переменная
# player_vec - вектор, который предложен пользователю; player_input - строка которая была введена пользователем
def check_vector(player_vec, fic_sysh, player_input):
    player_input = player_input.replace(' ', '')
    if dict_vector[player_vec][fic_sysh] == player_input:
        return True
    return False


all_vector(n_param.get())
player_vec = list_vector[int(random.random() * 100) % len(list_vector)]  # Вектор, который передают пользователю
sfp = '0'


def mack_sfp():
    global player_vec
    global sfp

    sushi_var_str, fic_var_str = 'существенные переменные для ', 'фиктивные переменные для '
    sfp = int(random.random() * 10) % 2
    if sfp == 0:
        greet_label.configure(text=f'Введите {sushi_var_str} функции:')
    else:
        greet_label.configure(text=f'Введите {fic_var_str} функции:')
    tmp = list_vector[int(random.random() * 100) % len(list_vector)]
    if tmp == player_vec:
        tmp = list_vector[int(random.random() * 100) % len(list_vector)]
    player_vec = tmp
    ans = ''
    for i in range(1, len(player_vec) + 1):
        ans += player_vec[i - 1]
        if i % 4 == 0:
            ans += ' '
    player_vec = ans
    vector_label.configure(text=player_vec)


def send_vector():
    global player_vec
    global sfp

    entry = user_entry.get()
    player_vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(0, len(tmp)):
        player_vec += tmp[i]
    if check_data(entry):
        if check_vector(player_vec, sfp, user_entry.get()):
            error_label.configure(text='Ваш ответ верный:)', fg='green')

            go_next_button.pack(side='left', padx=5)
        else:
            error_label.configure(text='Ответ неверный!', fg='#ff4000')

            go_next_button.pack(side='left', padx=5)
            remake_button.pack(side='left', padx=5)
            correct_answer_button.pack(side='left', padx=5)
    else:
        error_label.configure(text='Ошибка ввода данных!', fg='#ff4000')

        go_next_button.pack(side='left', padx=5)
        remake_button.pack(side='left', padx=5)
        correct_answer_button.pack(side='left', padx=5)

    button_submit['state'] = 'disabled'
    user_entry['state'] = 'disabled'


def go_next():
    all_vector(n_param.get())
    button_submit['state'] = 'normal'
    user_entry['state'] = 'normal'
    user_entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    correct_answer_button.pack_forget()
    error_label.configure(text='')
    mack_sfp()


def remake_task():
    button_submit['state'] = 'normal'
    user_entry['state'] = 'normal'
    user_entry.delete(0, 'end')
    go_next_button.pack_forget()
    remake_button.pack_forget()
    correct_answer_button.pack_forget()
    error_label.configure(text='')


def show_correct_answer():
    global sfp
    player_vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(0, len(tmp)):
        player_vec += tmp[i]
    ans = dict_vector[player_vec][sfp]
    ans = ans.replace('1', 'x\u2081')
    ans = ans.replace('2', 'x\u2082')
    ans = ans.replace('3', 'x\u2083')
    ans = ans.replace('4', 'x\u2084')
    ans = ans.replace('5', 'x\u2085')
    ans = ans.replace('6', 'x\u2086')
    ans = ans.replace('7', 'x\u2087')
    ans = ans.replace('8', 'x\u2088')
    ans = ans.replace('9', 'x\u2089')
    error_label.configure(text=f'Правильный ответ - {ans}', fg='green')
    correct_answer_button.pack_forget()


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\n\nЕсли нет фиктивных или существенных переменных, то пишите 0\n"
    ans += "Пример ввода данных: \n\n"
    ans += "Выберите существенные переменные для функции: 00101001\n\n"
    ans += "\nВведите номер(а): 123\n\n"
    ans += "Если у вас остались вопросы, то их можно задать разработчикам:\n\n"
    ans += "https://vk.com/deltams4\n"
    ans += "https://vk.com/id212348723\n"
    ans += "https://vk.com/otza_to4ka_net\n\n"
    ans += "Приятной игры ;)\n\n\n\n"
    label = tk.Label(child_root, text=ans, font=('Times New Roman', 12, 'normal'), justify='left').pack()


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
    send_vector()

greet_label = tk.Label(root, text='Ваш вектор:', font=('Times New Roman', 16, 'normal'))
greet_label.pack()

vector_label = tk.Label(root, text='', font=('Times New Roman', 16, 'normal'))
vector_label.pack()

error_label = tk.Label(root, text='', font=('Times New Roman', 14, 'normal'), fg='#ff4000')
error_label.pack()

user_entry = tk.Entry(root, font=('Roboto', 14, 'normal'), width=40)
user_entry.pack()

button_submit = tk.Button(root, text='Ответить', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=send_vector)
button_submit.pack(pady=10)

fr = tk.Frame(root)
go_next_button = tk.Button(fr, text='Новое задание', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=go_next)
remake_button = tk.Button(fr, text='Пройти заново', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=remake_task)
correct_answer_button = tk.Button(fr, text='Правильный ответ', font=('Roboto', 12, 'normal'), bg='#bfbfbf', command=show_correct_answer)
fr.pack()

mack_sfp()
draw_menu()
root.bind('<Return>', onclick)
root.mainloop()

s = read_file()
s[1] = '0'
write_file(s)
