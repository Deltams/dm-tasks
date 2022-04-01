import os
import random
import tkinter as tk

root = tk.Tk()
root.title('Меню')
root.geometry('800x540+350+150')
root.resizable(False, False)
try:
    root.iconbitmap('icon.ico')
except:
    pass

def read_file():
    s = ''
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\seve.txt'
    with open(file, 'r') as f:
        s = f.readline()
        s = s.replace(' ', '').split(',')
    return s

def write_file(s):
    file = os.path.abspath(os.path.join('seve.txt',"../..")) + '\seve.txt'
    with open(file, 'w') as f:
        ans = ''
        for i in s:
            ans += i + ', '
        ans = ans[:len(ans)-2]
        f.write(ans)
        
def task4_desktop():
    s = read_file()
    if s[0] != '1':
        s[0] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame4.exe',"../../..")) + '\\task4\dist\BoolGame4.exe'
        os.startfile(file)

def task5_desktop():
    s = read_file()
    if s[1] != '1':
        s[1] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame5.exe',"../../..")) + '\\task5\dist\BoolGame5.exe'
        os.startfile(file)

def task6_desktop():
    s = read_file()
    if s[2] != '1':
        s[2] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame6.exe',"../../..")) + '\\task6\dist\BoolGame6.exe'
        os.startfile(file)

def task7_desktop():
    s = read_file()
    if s[3] != '1':
        s[3] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame7.exe',"../../..")) + '\\task7\dist\BoolGame7.exe'
        os.startfile(file)

def task10_desktop():
    s = read_file()
    if s[4] != '1':
        s[4] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame10.exe',"../../..")) + '\\task10\dist\BoolGame10.exe'
        os.startfile(file)

def task11_desktop():
    s = read_file()
    if s[5] != '1':
        s[5] = '1'
        write_file(s)
        file = os.path.abspath(os.path.join('BoolGame11.exe',"../../..")) + '\\task11\dist\BoolGame11.exe'
        os.startfile(file)

def draw_menu():
    menu_bar = tk.Menu(root)
    menu_bar.add_cascade(label='Узнать имя функции  ', command=task4_desktop)
    menu_bar.add_cascade(label='Сущ. фик. переменные ', command=task5_desktop)
    menu_bar.add_cascade(label='Построение ДНФ ', command=task6_desktop)
    menu_bar.add_cascade(label='Построение КНФ ', command=task7_desktop)
    menu_bar.add_cascade(label='Замкнутые классы б. ф. ', command=task10_desktop)
    menu_bar.add_cascade(label='Полные системы б. ф.', command=task11_desktop)
    root.configure(menu=menu_bar)

draw_menu()

c = tk.Canvas(width=800, height=540)
c.pack()
bg = tk.PhotoImage(file="icon.png")
bg_razm = c.create_image(456, 180, image=bg)
lab = c.create_text(298, 185, text='B', fill="Black", justify='center', font=('Harlow Solid Italic', 120, 'normal'))
lab2 = c.create_text(400, 300, text='Game', fill="Black", justify='center', font=('Harlow Solid Italic', 120, 'normal'))

##menu_label_1 = tk.Label(root, text='   Bool \n Game ', font=('Harlow Solid Italic', 120, 'normal'))
##menu_label_1.pack(pady=60)

root.mainloop()
