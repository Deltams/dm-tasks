import random
import tkinter as tk
import os

root = tk.Tk()
root.title('Задача 11')
root.geometry('800x580+100+100')
root.resizable(False, False)

try:
    root.iconbitmap('icon.ico')
except:
    pass

n_param = tk.IntVar(value=3)


def return_norm_vec(svec, start):
    ans = ''
    for i in range(start, len(svec)):
        ans += svec[i]
    return ans.replace(' ', '')


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


def random_vector2(vars_count):
    ans = []
    r = int(random.random() * 10) % 6  # Выбор к какому классу будет принадлежать
    if r == 0:
        while len(ans) < 4:
            v = random_vector(vars_count)
            if check_t0(return_norm_vec(v, 0)):
                ans.append(v)
    elif r == 1:
        while len(ans) < 4:
            v = random_vector(vars_count)
            if check_t1(return_norm_vec(v, 0)):
                ans.append(v)
    elif r == 2:
        while len(ans) < 4:
            v = random_vector(vars_count)
            if check_s(return_norm_vec(v, 0)):
                ans.append(v)
    elif r == 3:
        while len(ans) < 4:
            v = random_vector(vars_count)
            if check_ln(return_norm_vec(v, 0)):
                ans.append(v)
    elif r == 4:
        while len(ans) < 4:
            v = random_vector(vars_count)
            if check_m(return_norm_vec(v, 0)):
                ans.append(v)
    else:
        while len(ans) < 4:
            v = random_vector(vars_count)
            ans.append(v)
    print(r)
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


# Прибовляет 1 по "обычному"
def sum_vec_pp(vec):
    ans = list(vec)
    check = False
    for i in range(len(vec) - 1, -1, -1):
        if vec[i] == '1':
            check = True
        if check:
            if vec[i] == '0':
                ans[i] = '1'
                ans[i + 1] = '0'
                break
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


# Проверка системы на полноту
def check_completeness(vec):
    ans = [1, 1, 1, 1, 1]
    for v in vec:
        if not check_t0(v):
            ans[0] = 0
        if not check_t1(v):
            ans[1] = 0
        if not check_s(v):
            ans[2] = 0
        if not check_ln(v):
            ans[3] = 0
        if not check_m(v):
            ans[4] = 0
    return ans


def print_ans():
    vec1 = return_norm_vec(vector_label1.cget('text').split(), 1)
    vec2 = return_norm_vec(vector_label2.cget('text').split(), 1)
    vec3 = return_norm_vec(vector_label3.cget('text').split(), 1)
    vec4 = return_norm_vec(vector_label4.cget('text').split(), 1)

    tmp = check_completeness([vec1, vec2, vec3, vec4])
    t = 0
    for i in tmp:
        if i == 1:
            t += 1
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


# Проверка ответа пользователя
def send_answer():
    vec1 = return_norm_vec(vector_label1.cget('text').split(), 1)
    vec2 = return_norm_vec(vector_label2.cget('text').split(), 1)
    vec3 = return_norm_vec(vector_label3.cget('text').split(), 1)
    vec4 = return_norm_vec(vector_label4.cget('text').split(), 1)

    ans = check_completeness([vec1, vec2, vec3, vec4])
    p_sis = 1
    for i in ans:
        if i == 1:
            p_sis = 0
            break
    check_false_ans = False
    if (var1.get() == True and p_sis == 1) or (var1.get() == False and p_sis == 0):
        error_label.configure(text='Неправильный ответ!', fg='red')
        check_false_ans = True

        new_button.pack(side='left', padx=5)
        remake_task_button.pack(side='left', padx=5)
        if check_false_ans:
            ans_button.pack(side='left', padx=5)
    elif var1.get() == False and p_sis == 1:
        error_label.configure(text='Правильный ответ!', fg='green')

        new_button.pack(side='left')
    elif var4_t0.get() == ans[0] and var4_t1.get() == ans[1] and var4_s.get() == ans[2] and \
            var4_ln.get() == ans[3] and var4_m.get() == ans[4]:
        error_label.configure(text='Правильный ответ!', fg='green')

        new_button.pack(side='left')
    else:
        error_label.configure(text='Неправильный ответ!', fg='red')
        check_false_ans = True

        new_button.pack(side='left', padx=5)
        remake_task_button.pack(side='left', padx=5)

        if check_false_ans:
            ans_button.pack(side='left', padx=5)

    button_submit['state'] = 'disabled'
    cb1['state'] = 'disabled'
    cb4_t0['state'] = 'disabled'
    cb4_t1['state'] = 'disabled'
    cb4_s['state'] = 'disabled'
    cb4_ln['state'] = 'disabled'
    cb4_m['state'] = 'disabled'


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\nЕсли вы считаете утверждение верным - нажмите на флажок\n"
    label_ch1 = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()
    ans = "\nЕсли верных ответов нет - оставьте флажок пустым\n"
    label_ch2 = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()


def open_cb1():
    cb4_t0.pack(side='left')
    cb4_t1.pack(side='left')
    cb4_s.pack(side='left')
    cb4_ln.pack(side='left')
    cb4_m.pack(side='left')
    cb1.configure(command=close_cb1)


def close_cb1():
    cb4_t0.pack_forget()
    cb4_t1.pack_forget()
    cb4_s.pack_forget()
    cb4_ln.pack_forget()
    cb4_m.pack_forget()
    cb1.configure(command=open_cb1)


def go_next():
    button_submit['state'] = 'normal'
    cb1['state'] = 'normal'
    cb4_t0['state'] = 'normal'
    cb4_t1['state'] = 'normal'
    cb4_s['state'] = 'normal'
    cb4_ln['state'] = 'normal'
    cb4_m['state'] = 'normal'
    vec = random_vector2(n_param.get())
    vector_label1.configure(text=f'1. {vec[0]}')
    vector_label2.configure(text=f'2. {vec[1]}')
    vector_label3.configure(text=f'3. {vec[2]}')
    vector_label4.configure(text=f'4. {vec[3]}')

    cb1.deselect()

    cb4_t0.deselect()
    cb4_t1.deselect()
    cb4_s.deselect()
    cb4_ln.deselect()
    cb4_m.deselect()

    close_cb1()
    error_label.configure(text='')
    new_button.pack_forget()
    remake_task_button.pack_forget()
    ans_button.pack_forget()


def remake_task():
    button_submit['state'] = 'normal'
    cb1['state'] = 'normal'
    cb4_t0['state'] = 'normal'
    cb4_t1['state'] = 'normal'
    cb4_s['state'] = 'normal'
    cb4_ln['state'] = 'normal'
    cb4_m['state'] = 'normal'

    cb1.deselect()
    cb4_t0.deselect()
    cb4_t1.deselect()
    cb4_s.deselect()
    cb4_ln.deselect()
    cb4_m.deselect()
    close_cb1()

    error_label.configure(text='')
    new_button.pack_forget()
    remake_task_button.pack_forget()
    ans_button.pack_forget()


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


greet_label = tk.Label(root, text='Определите является ли набор функций полным', font=('Arial', 18, 'normal'))
greet_label.pack()

error_label = tk.Label(root, text='', font=('Arial', 16, 'normal'))
error_label.pack()

# First frame
fr1 = tk.Frame()
vector_label1 = tk.Label(fr1, text=f'1. {random_vector(n_param.get())}', font=('Arial', 18, 'normal'))
vector_label1.pack(side='left', anchor="w")

fr1.pack(anchor="w", padx=150, pady=10)

# Second Frame
fr2 = tk.Frame()
vector_label2 = tk.Label(fr2, text=f'2. {random_vector(n_param.get())}', font=('Arial', 18, 'normal'))
vector_label2.pack(side='left', anchor="w")

fr2.pack(anchor="w", padx=150, pady=10)

# Third Frame
fr3 = tk.Frame()
vector_label3 = tk.Label(fr3, text=f'3. {random_vector(n_param.get())}', font=('Arial', 18, 'normal'))
vector_label3.pack(side='left', anchor="w")

fr3.pack(anchor="w", padx=150, pady=10)

# 4XD Frame
fr4 = tk.Frame()
vector_label4 = tk.Label(fr4, text=f'4. {random_vector(n_param.get())}', font=('Arial', 18, 'normal'))
vector_label4.pack(side='left', anchor="w")

fr4_child = tk.Frame(height=36)

var4_t0 = tk.BooleanVar()
var4_t0.set(0)
cb4_t0 = tk.Checkbutton(fr4_child, variable=var4_t0, text='T0', font=('Arial', 16, 'normal'))

var4_t1 = tk.BooleanVar()
var4_t1.set(0)
cb4_t1 = tk.Checkbutton(fr4_child, variable=var4_t1, text='T1', font=('Arial', 16, 'normal'))

var4_s = tk.BooleanVar()
var4_s.set(0)
cb4_s = tk.Checkbutton(fr4_child, variable=var4_s, text='S', font=('Arial', 16, 'normal'))

var4_ln = tk.BooleanVar()
var4_ln.set(0)
cb4_ln = tk.Checkbutton(fr4_child, variable=var4_ln, text='L', font=('Arial', 16, 'normal'))

var4_m = tk.BooleanVar()
var4_m.set(0)
cb4_m = tk.Checkbutton(fr4_child, variable=var4_m, text='M', font=('Arial', 16, 'normal'))

fr4.pack(anchor="w", padx=150, pady=10)

# Неполная?
fr1_1 = tk.Frame()
var1 = tk.BooleanVar()
var1.set(0)
cb1 = tk.Checkbutton(fr1_1, variable=var1, text='Неполная?', command=open_cb1, font=('Arial', 16, 'normal'))
cb1.pack()

fr1_1.pack(anchor="w", padx=150, pady=10)
# Неполная?

fr4_child.pack(anchor="w", padx=160)

button_submit = tk.Button(root, text='Ответить', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=10)

but_fr = tk.Frame(root)
new_button = tk.Button(but_fr, text='Новое задание', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=go_next)
remake_task_button = tk.Button(but_fr, text='Перепройти', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=remake_task)
ans_button = tk.Button(but_fr, text='Показать ответ', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=print_ans)
but_fr.pack()

button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')

draw_menu()

root.mainloop()
os.startfile('BoolGame')
