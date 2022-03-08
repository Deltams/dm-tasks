import random
import tkinter as tk

root = tk.Tk()
root.title('Задача 5')
root.geometry('600x500+100+100')
root.resizable(False, False)

attempts = 1  # кол-во попыток
vars_count = 3  # кол-во переменных
dict_vector = {}  # Словарь ответов для пользователя; Автоматически заполняется в all_vector
list_vector = []


def residual(vec, k, n):  # остаточная по вектору; vec - vector; k - какая остаточная; n - переменная
    ans = ""
    tmp = len(vec) / 2 ** n  # размер коробки
    i = k * tmp
    while i < len(vec):
        ans = ans + vec[int(i):int(i) + int(tmp)]
        i = i + tmp * 2
    return ans


def all_vector(vars_count):  # Заполнение map_vector; p - param
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
        if len(fict_var) and len(sysh_var):
            dict_vector[vec] = [sysh_var, fict_var]
            list_vector.append(vec)
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


all_vector(vars_count)
player_vec = list_vector[int(random.random() * 100) % len(list_vector)]  # Вектор, который передают пользователю
sfp = '0'


def mack_sfp():
    global attempts
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
    attempts = 1
    vector_label.configure(text=player_vec)


def send_vector():
    global attempts
    global player_vec
    global sfp

    entry = user_entry.get()
    if check_data(entry):
        if check_vector(player_vec, sfp, user_entry.get()):
            error_label.configure(text='Ваш ответ верный:)', fg='green')
        else:
            error_label.configure(text='Ответ неверный!', fg='#ff4000')
            attempts -= 1
    else:
        error_label.configure(text='Ошибка ввода данных!', fg='#ff4000')
        attempts -= 1

    button_submit['state'] = 'disabled'
    user_entry['state'] = 'disabled'
    go_next_button.pack()


def go_next():
    button_submit['state'] = 'normal'
    user_entry['state'] = 'normal'
    user_entry.delete(0, 'end')
    go_next_button.pack_forget()
    error_label.configure(text='')
    mack_sfp()


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\n\nЕсли нет фиктивных или существенных переменных, то пишите 0\n"
    ans += "Пример ввода данных: \n\n"
    ans += "Выберите существенные переменные для функции: 00101001\n\n"
    ans += "Попыток осталось: n\nВведите номер(а): 123\n\n"
    ans += "Если у вас остались вопросы, то их можно задать разработчикам:\n\n"
    ans += "https://vk.com/deltams4\n"
    ans += "https://vk.com/id212348723\n"
    ans += "https://vk.com/otza_to4ka_net\n\n"
    ans += "Приятной игры ;)\n\n\n\n"
    label = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()


greet_label = tk.Label(root, text='Ваш вектор:', font=('Arial', 16, 'normal'))
greet_label.pack()

vector_label = tk.Label(root, text='', font=('Arial', 16, 'normal'))
vector_label.pack()

error_label = tk.Label(root, text='', font=('Arial', 14, 'normal'), fg='#ff4000')
error_label.pack()

user_entry = tk.Entry(root, font=('Arial', 14, 'normal'), width=40)
user_entry.pack()

button_submit = tk.Button(root, text='Ответить', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=send_vector)
button_submit.pack()

go_next_button = tk.Button(root, text='Новое задание', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=go_next)

button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')

mack_sfp()

root.mainloop()
