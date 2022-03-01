import random
import tkinter as tk

root = tk.Tk()
root.title('Задача 11')
root.geometry('600x520+100+100')
root.resizable(False, False)

vec = '01111110'


def random_vector(vars_count):
    global vec
    len_vector = 2 ** vars_count
    count_all_vectors = 2 ** len_vector
    tmp = int(random.random() * (10 ** len(str(count_all_vectors)))) % count_all_vectors
    vec = str(bin(tmp)[2:])
    vec = "0" * (len_vector - len(vec)) + vec
    return vec


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


# Проверка на полноту
def check_completeness(vec):
    ch_t0 = check_t0(vec)
    ch_t1 = check_t1(vec)
    ch_s = check_s(vec)
    ch_ln = check_ln(vec)
    ch_m = check_m(vec)
    if ch_t0 or ch_t1 or ch_s or ch_ln or ch_m:
        return False
    return True


def send_answer():
    vec1 = vector_label1.cget('text').split()[1]
    vec2 = vector_label2.cget('text').split()[1]
    vec3 = vector_label3.cget('text').split()[1]
    vec4 = vector_label4.cget('text').split()[1]
    if var1.get() == check_completeness(vec1):
        error_label.configure(text='Неправильный ответ!', fg='red')
    elif var2.get() == check_completeness(vec2):
        error_label.configure(text='Неправильный ответ!', fg='red')
    elif var3.get() == check_completeness(vec3):
        error_label.configure(text='Неправильный ответ!', fg='red')
    elif var4.get() == check_completeness(vec4):
        error_label.configure(text='Неправильный ответ!', fg='red')
    if var1_t0.get() == check_t0(vec1) and var1_t1.get() == check_t1(vec1) and var1_s.get() == check_s(vec1) and \
            var1_ln.get() == check_ln(vec1) and var1_m.get() == check_m(vec1):
        if var2_t0.get() == check_t0(vec2) and var2_t1.get() == check_t1(vec2) and var2_s.get() == check_s(vec2) and \
            var2_ln.get() == check_ln(vec2) and var2_m.get() == check_m(vec2):
            if var3_t0.get() == check_t0(vec3) and var3_t1.get() == check_t1(vec3) and var3_s.get() == check_s(vec3) and \
            var3_ln.get() == check_ln(vec3) and var3_m.get() == check_m(vec3):
                if var4_t0.get() == check_t0(vec4) and var4_t1.get() == check_t1(vec4) and var4_s.get() == check_s(vec4) and \
            var4_ln.get() == check_ln(vec4) and var4_m.get() == check_m(vec4):
                    error_label.configure(text='Правильный ответ!', fg='green')
                    vector_label1.configure(text=f'1. {random_vector(3)}')
                    vector_label2.configure(text=f'2. {random_vector(3)}')
                    vector_label3.configure(text=f'3. {random_vector(3)}')
                    vector_label4.configure(text=f'4. {random_vector(3)}')

                    cb1.deselect()
                    cb1_t0.deselect()
                    cb1_t1.deselect()
                    cb1_s.deselect()
                    cb1_ln.deselect()
                    cb1_m.deselect()

                    cb2.deselect()
                    cb2_t0.deselect()
                    cb2_t1.deselect()
                    cb2_s.deselect()
                    cb2_ln.deselect()
                    cb2_m.deselect()

                    cb3.deselect()
                    cb3_t0.deselect()
                    cb3_t1.deselect()
                    cb3_s.deselect()
                    cb3_ln.deselect()
                    cb3_m.deselect()

                    cb4.deselect()
                    cb4_t0.deselect()
                    cb4_t1.deselect()
                    cb4_s.deselect()
                    cb4_ln.deselect()
                    cb4_m.deselect()

                    close_cb1()
                    close_cb2()
                    close_cb3()
                    close_cb4()
                    return
    error_label.configure(text='Неправильный ответ!', fg='red')


def open_child_root():
    child_root = tk.Toplevel(root)
    child_root.title('Справка')
    child_root.geometry('550x350+100+100')
    child_root.resizable(False, False)
    child_root.grab_set()
    ans = "\nЕсли вы считаете утверждение верным - нажмите на флажок\n"
    ans += "\nЕсли верных ответов нет - оставьте флажок пустым\n"
    label = tk.Label(child_root, text=ans, font=('Arial', 12, 'normal'), justify='left').pack()


def open_cb1():
    cb1_t0.pack(side='left')
    cb1_t1.pack(side='left')
    cb1_s.pack(side='left')
    cb1_ln.pack(side='left')
    cb1_m.pack(side='left')
    cb1.configure(command=close_cb1)


def close_cb1():
    cb1_t0.pack_forget()
    cb1_t1.pack_forget()
    cb1_s.pack_forget()
    cb1_ln.pack_forget()
    cb1_m.pack_forget()
    cb1.configure(command=open_cb1)


# open_cb2 and close_cb2
def open_cb2():
    cb2_t0.pack(side='left')
    cb2_t1.pack(side='left')
    cb2_s.pack(side='left')
    cb2_ln.pack(side='left')
    cb2_m.pack(side='left')
    cb2.configure(command=close_cb2)


def close_cb2():
    cb2_t0.pack_forget()
    cb2_t1.pack_forget()
    cb2_s.pack_forget()
    cb2_ln.pack_forget()
    cb2_m.pack_forget()
    cb2.configure(command=open_cb2)


# open_cb2 and close_cb2
def open_cb3():
    cb3_t0.pack(side='left')
    cb3_t1.pack(side='left')
    cb3_s.pack(side='left')
    cb3_ln.pack(side='left')
    cb3_m.pack(side='left')
    cb3.configure(command=close_cb3)


def close_cb3():
    cb3_t0.pack_forget()
    cb3_t1.pack_forget()
    cb3_s.pack_forget()
    cb3_ln.pack_forget()
    cb3_m.pack_forget()
    cb3.configure(command=open_cb3)


# open_cb4 and close_cb4
def open_cb4():
    cb4_t0.pack(side='left')
    cb4_t1.pack(side='left')
    cb4_s.pack(side='left')
    cb4_ln.pack(side='left')
    cb4_m.pack(side='left')
    cb4.configure(command=close_cb4)


def close_cb4():
    cb4_t0.pack_forget()
    cb4_t1.pack_forget()
    cb4_s.pack_forget()
    cb4_ln.pack_forget()
    cb4_m.pack_forget()
    cb4.configure(command=open_cb4)


greet_label = tk.Label(root, text='Ответьте на вопросы', font=('Arial', 18, 'normal'))
greet_label.pack()

error_label = tk.Label(root, text='', font=('Arial', 16, 'normal'))
error_label.pack()


# First frame
fr1 = tk.Frame()
vector_label1 = tk.Label(fr1, text=f'1. {random_vector(3)}', font=('Arial', 18, 'normal'))
vector_label1.pack(side='left', anchor="w")

var1 = tk.BooleanVar()
var1.set(0)
cb1 = tk.Checkbutton(fr1, variable=var1, text='Неполная?', command=open_cb1, font=('Arial', 16, 'normal'))
cb1.pack(anchor="w")

child_fr1 = tk.Frame(height=36)

var1_t0 = tk.BooleanVar()
var1_t0.set(0)
cb1_t0 = tk.Checkbutton(child_fr1, variable=var1_t0, text='T0', font=('Arial', 16, 'normal'))

var1_t1 = tk.BooleanVar()
var1_t1.set(0)
cb1_t1 = tk.Checkbutton(child_fr1, variable=var1_t1, text='T1', font=('Arial', 16, 'normal'))

var1_s = tk.BooleanVar()
var1_s.set(0)
cb1_s = tk.Checkbutton(child_fr1, variable=var1_s, text='S', font=('Arial', 16, 'normal'))

var1_ln = tk.BooleanVar()
var1_ln.set(0)
cb1_ln = tk.Checkbutton(child_fr1, variable=var1_ln, text='L', font=('Arial', 16, 'normal'))

var1_m = tk.BooleanVar()
var1_m.set(0)
cb1_m = tk.Checkbutton(child_fr1, variable=var1_m, text='M', font=('Arial', 16, 'normal'))

fr1.pack(anchor="w", padx=150, pady=10)
child_fr1.pack(anchor="w", padx=160)


# Second Frame
fr2 = tk.Frame()
vector_label2 = tk.Label(fr2, text=f'2. {random_vector(3)}', font=('Arial', 18, 'normal'))
vector_label2.pack(side='left', anchor="w")
var2 = tk.BooleanVar()
var2.set(0)
cb2 = tk.Checkbutton(fr2, variable=var2, text='Неполная?', command=open_cb2, font=('Arial', 16, 'normal'))
cb2.pack(anchor="w")

fr2_child = tk.Frame(height=36)

var2_t0 = tk.BooleanVar()
var2_t0.set(0)
cb2_t0 = tk.Checkbutton(fr2_child, variable=var2_t0, text='T0', font=('Arial', 16, 'normal'))

var2_t1 = tk.BooleanVar()
var2_t1.set(0)
cb2_t1 = tk.Checkbutton(fr2_child, variable=var2_t1, text='T1', font=('Arial', 16, 'normal'))

var2_s = tk.BooleanVar()
var2_s.set(0)
cb2_s = tk.Checkbutton(fr2_child, variable=var2_s, text='S', font=('Arial', 16, 'normal'))

var2_ln = tk.BooleanVar()
var2_ln.set(0)
cb2_ln = tk.Checkbutton(fr2_child, variable=var2_ln, text='L', font=('Arial', 16, 'normal'))

var2_m = tk.BooleanVar()
var2_m.set(0)
cb2_m = tk.Checkbutton(fr2_child, variable=var2_m, text='M', font=('Arial', 16, 'normal'))
fr2.pack(anchor="w", padx=150, pady=10)
fr2_child.pack(anchor="w", padx=160)


# Third Frame
fr3 = tk.Frame()
vector_label3 = tk.Label(fr3, text=f'3. {random_vector(3)}', font=('Arial', 18, 'normal'))
vector_label3.pack(side='left', anchor="w")
var3 = tk.BooleanVar()
var3.set(0)
cb3 = tk.Checkbutton(fr3, variable=var3, text='Неполная?', command=open_cb3, font=('Arial', 16, 'normal'))
cb3.pack(anchor="w")

fr3_child = tk.Frame(height=36)

var3_t0 = tk.BooleanVar()
var3_t0.set(0)
cb3_t0 = tk.Checkbutton(fr3_child, variable=var3_t0, text='T0', font=('Arial', 16, 'normal'))

var3_t1 = tk.BooleanVar()
var3_t1.set(0)
cb3_t1 = tk.Checkbutton(fr3_child, variable=var3_t1, text='T1', font=('Arial', 16, 'normal'))

var3_s = tk.BooleanVar()
var3_s.set(0)
cb3_s = tk.Checkbutton(fr3_child, variable=var3_s, text='S', font=('Arial', 16, 'normal'))

var3_ln = tk.BooleanVar()
var3_ln.set(0)
cb3_ln = tk.Checkbutton(fr3_child, variable=var3_ln, text='L', font=('Arial', 16, 'normal'))

var3_m = tk.BooleanVar()
var3_m.set(0)
cb3_m = tk.Checkbutton(fr3_child, variable=var3_m, text='M', font=('Arial', 16, 'normal'))
fr3.pack(anchor="w", padx=150, pady=10)
fr3_child.pack(anchor="w", padx=160)

# 4XD Frame
fr4 = tk.Frame()
vector_label4 = tk.Label(fr4, text=f'4. {random_vector(3)}', font=('Arial', 18, 'normal'))
vector_label4.pack(side='left', anchor="w")
var4 = tk.BooleanVar()
var4.set(0)
cb4 = tk.Checkbutton(fr4, variable=var4, text='Неполная?', command=open_cb4, font=('Arial', 16, 'normal'))
cb4.pack()

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
fr4_child.pack(anchor="w", padx=160)


button_submit = tk.Button(root, text='Ответить', font=('Arial', 14, 'normal'), bg='#bfbfbf', command=send_answer)
button_submit.pack(pady=10)

button_help = tk.Button(root, text='Справка', font=('Arial', 12, 'normal'), bg='#bfbfbf', command=open_child_root)
button_help.pack(side='bottom', anchor='e')


root.mainloop()

