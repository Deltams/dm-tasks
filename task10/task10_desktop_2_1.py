import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 10')
root.geometry('800x580+100+100')
root.resizable(False, False)

try:
    root.iconbitmap('icon.ico')
except:
    pass

vec = '01111110'
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
    for char in range(int(len(vec) / 2)):
        if vec[char] == vec[-1 - char]:
            return False
    return True


# Проверка на линейность
def check_ln(vec):
    param = what_degree_two(len(vec))
    arr = [0] * (param + 1)  # Массив для проверки линейности
    arr[0] = int(vec[0])
    tmp = 1
    for i in range(1, param + 1):
        t = '0' * (param - len(str(tmp))) + str(tmp)
        arr[-i] = (arr[0] + int(vec[int(t, 2)])) % 2
        tmp *= 10
    ans_vec = str(arr[0])
    for i in range(1, len(vec)):
        t = str(bin(i)[2:])
        t = '0' * (param - len(t)) + t
        var_tmp = 0
        for j in range(1, len(arr)):
            if arr[j] == 1:
                var_tmp += int(t[j - 1])
        ans_vec += str((var_tmp + arr[0]) % 2)
    if ans_vec == vec:
        return True
    return False


# Прибавляет 1 по "обычному"
def sum_vec_pp(vec):
    ans = list(vec)
    check = False
    t = -1
    for i in range(len(vec) - 1, -1, -1):
        if vec[i] == '1':
            ans[i] = '0'
            t += 1
            check = True
        if check:
            if vec[i] == '0':
                ans[i] = '1'
                ans[i + 1] = '0'
                check = False
                break
    if check == True:
        return vec
    for i in range(len(vec) - 1, -1, -1):
        if t <= 0:
            break
        ans[i] = '1'
        t -= 1
    return "".join(ans)


# Проверка на монотонность
def check_m(vec):
    param = what_degree_two(len(vec))
    mp_ans = {}
    for i in range(len(vec)):
        t = str(bin(i)[2:])
        t = '0' * (param - len(t)) + t
        mp_ans[t] = int(vec[i])

    for i in range(1, param + 1):
        real = []
        nach_str = '0' * (param - len('1' * i)) + '1' * i
        while nach_str != sum_vec_pp(nach_str):
            for j in range(len(nach_str)):
                if mp_ans[nach_str[:j] + '0' + nach_str[j + 1:]] > mp_ans[nach_str]:
                    return False
            nach_str = sum_vec_pp(nach_str)
        for j in range(len(nach_str)):
            if mp_ans[nach_str[:j] + '0' + nach_str[j + 1:]] > mp_ans[nach_str]:
                return False
    return True


def print_ans():
    vec = ''
    tmp = vector_label.cget('text').split()
    for i in range(len(tmp)):
        vec += tmp[i]
    tmp = [0, 0, 0, 0, 0]
    tmp[0] = check_t0(vec)
    tmp[1] = check_t1(vec)
    tmp[2] = check_s(vec)
    tmp[3] = check_ln(vec)
    tmp[4] = check_m(vec)
    t = tmp[0] + tmp[1] + tmp[2] + tmp[3] + tmp[4]
    ans = 'Система функций '
    if t == 1:
        ans += 'принадлежит следующему классу: '
    elif t == 0:
        ans += 'является полной'
    else:
        ans += 'принадлежит следующим классам: '
    if tmp[0] == 1:
        ans += 'T0 '
    if tmp[1] == 1:
        ans += 'T1 '
    if tmp[2] == 1:
        ans += 'S '
    if tmp[3] == 1:
        ans += 'L '
    if tmp[4] == 1:
        ans += 'M '
    error_label.configure(text=f'{ans}', fg='green')
    ans_button.pack_forget()


def send_answer():
    vec = ''
    tmp = vector_label.cget('text').split()
    check_false_ans = False
    for i in range(len(tmp)):
        vec += tmp[i]
    if var1.get() == check_t0(vec) and var2.get() == check_t1(vec) and var3.get() == check_s(vec) and \
            var4.get() == check_ln(vec) and var5.get() == check_m(vec):
        error_label.configure(text='Правильный ответ!', fg='green')

        new_button.pack(side='left')
    else:
        error_label.configure(text='Неправильный ответ!', fg='red')
        check_false_ans = True

        new_button.pack(side='left', padx=5)
        remake_task_button.pack(side='left', padx=5)
        if check_false_ans:
            ans_button.pack(padx=5)

    button_submit['state'] = 'disabled'
    c1['state'] = 'disabled'
    c2['state'] = 'disabled'
    c3['state'] = 'disabled'
    c4['state'] = 'disabled'
    c5['state'] = 'disabled'


def go_next():
    button_submit['state'] = 'normal'
    c1['state'] = 'normal'
    c2['state'] = 'normal'
    c3['state'] = 'normal'
    c4['state'] = 'normal'
    c5['state'] = 'normal'
    vector_label.configure(text=random_vector(n_param.get()))

    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()

    error_label.configure(text='')
    new_button.pack_forget()
    remake_task_button.pack_forget()
    ans_button.pack_forget()


def remake_task():
    button_submit['state'] = 'normal'
    c1['state'] = 'normal'
    c2['state'] = 'normal'
    c3['state'] = 'normal'
    c4['state'] = 'normal'
    c5['state'] = 'normal'

    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()

    error_label.configure(text='')
    new_button.pack_forget()
    remake_task_button.pack_forget()
    ans_button.pack_forget()


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\nЕсли вы считаете утверждение верным - нажмите на флажок\n"
    ans += "\nЕсли верных ответов нет - оставьте флажок пустым\n"
    label = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()


# Выпадающие меню
def draw_menu():
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_radiobutton(label='1 переменная', value=1, variable=n_param, command=go_next,
                              font=('Arial', 12, 'normal'))
    file_menu.add_radiobutton(label='2 переменных', value=2, variable=n_param, command=go_next,
                              font=('Arial', 12, 'normal'))
    file_menu.add_radiobutton(label='3 переменных', value=3, variable=n_param, command=go_next,
                              font=('Arial', 12, 'normal'))
    file_menu.add_radiobutton(label='4 переменных', value=4, variable=n_param, command=go_next,
                              font=('Arial', 12, 'normal'))
    file_menu.add_radiobutton(label='5 переменных', value=5, variable=n_param, command=go_next,
                              font=('Arial', 12, 'normal'))
    menu_bar.add_cascade(label='Настройки', menu=file_menu)
    root.configure(menu=menu_bar)

def onclick(event):
    send_answer()

greet_label = tk.Label(root, text='Отметьте верные утверждения для функции', font=('Arial', 18, 'normal'))
greet_label.pack(pady=5)

vector_label = tk.Label(root, text=random_vector(n_param.get()), font=('Arial', 17, 'normal'))
vector_label.pack(pady=5)

error_label = tk.Label(root, text='', font=('Arial', 16, 'normal'))
error_label.pack()

checkbox_frame = tk.Frame(root)

fr1 = tk.Frame(checkbox_frame)
label1 = tk.Label(fr1, text='Функция сохраняет ноль', font=('Arial', 14, 'normal'), justify='left')
label1.pack(side='left')
var1 = tk.BooleanVar()
var1.set(0)
c1 = tk.Checkbutton(fr1, text="T0", variable=var1, offvalue=0, onvalue=1, font=('Arial', 14, 'normal'))
c1.pack(side='left', padx=144)
fr1.pack(anchor="w", pady=10, padx=90)

fr2 = tk.Frame(checkbox_frame)
label2 = tk.Label(fr2, text='Функция сохраняет единицу', font=('Arial', 14, 'normal'), justify='left')
label2.pack(side='left')
var2 = tk.BooleanVar()
var2.set(0)
c2 = tk.Checkbutton(fr2, text="T1", variable=var2, offvalue=0, onvalue=1, font=('Arial', 14, 'normal'))
c2.pack(side='left', padx=114)
fr2.pack(anchor="w", pady=10, padx=90)

fr3 = tk.Frame(checkbox_frame)
label3 = tk.Label(fr3, text='Функция является самодвойственной', font=('Arial', 14, 'normal'))
label3.pack(side='left')
var3 = tk.BooleanVar()
var3.set(0)
c3 = tk.Checkbutton(fr3, text="S", variable=var3, offvalue=0, onvalue=1, font=('Arial', 14, 'normal'))
c3.pack(side='left', padx=31)
fr3.pack(anchor="w", pady=10, padx=90)

fr4 = tk.Frame(checkbox_frame)
label4 = tk.Label(fr4, text='Функция является линейной', font=('Arial', 14, 'normal'))
label4.pack(side='left')
var4 = tk.BooleanVar()
var4.set(0)
c4 = tk.Checkbutton(fr4, text="L", variable=var4, offvalue=0, onvalue=1, font=('Arial', 14, 'normal'))
c4.pack(side='left', padx=115)
fr4.pack(anchor="w", pady=10, padx=90)

fr5 = tk.Frame(checkbox_frame)
label5 = tk.Label(fr5, text='Функция является монотонной', font=('Arial', 14, 'normal'))
label5.pack(side='left')
var5 = tk.BooleanVar()
var5.set(0)
c5 = tk.Checkbutton(fr5, text="M", variable=var5, offvalue=0, onvalue=1, font=('Arial', 14, 'normal'))
c5.pack(side='left', padx=92)
fr5.pack(anchor="w", pady=10, padx=90)

checkbox_frame.pack(anchor="w", padx=30)

button_submit = tk.Button(root, text='Ответить', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=20)

but_fr = tk.Frame(root)
new_button = tk.Button(but_fr, text='Новое задание', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=go_next)
remake_task_button = tk.Button(but_fr, text='Перепройти', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=remake_task)
ans_button = tk.Button(but_fr, text='Показать ответ', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=print_ans)
but_fr.pack()

button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')

draw_menu()
root.bind('<Return>', onclick)
root.mainloop()

s = read_file()
s[4] = '0'
write_file(s)
