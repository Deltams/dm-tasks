import os
import random
import tkinter as tk
import time

root = tk.Tk()
root.title('Загрузка')
root.geometry('500x270+500+250')
root.resizable(False, False)
try:
    root.iconbitmap('icon.ico')
except:
    pass

root.overrideredirect(True)
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")

c = tk.Canvas(width=500, height=270)
c.pack()
bg = tk.PhotoImage(file="step.png")
bg_razm = c.create_image(-250, 135, image=bg)


lst = [255, 11, 11]
lst_put = 2

const_ardiar1 = '' + \
'╔═══╗ ╔═══╗  ╔══╗  ╔╗  ╔╗ ╔══╗ ╔═══╗\n' + \
'║╔═╗║ ║╔═╗║  ║╔╗║  ║║  ╗║ ║╔╗║ ║╔═╗║\n' + \
'║╚═╝║ ║╚═╝║  ║║║║  ║║ ║║║ ║╚╝║ ║╚═╝║\n' + \
'╚╗╔╗║ ║╔══╝  ║║║║  ║║║ ║║ ║╔╗║ ║╔══╝\n' + \
' ║║║║ ║║    ╔╝╚╝╚╗ ║╚  ║║ ║║║║ ║║   \n' + \
' ╚╝╚╝ ╚╝    ╚════╝ ╚╝  ╚╝ ╚╝╚╝ ╚╝   \n' + \
'╔════╗ ╔═══╗ ╔══╗ ╔╗  ╔╗\n' + \
'╚═╗╔═╝ ║╔══╝ ║╔╗║ ║║  ║║\n' + \
'  ║║   ║╚══╗ ║╚╝║ ║╚╗╔╝║\n' + \
'  ║║   ║╔══╝ ║╔╗║ ║╔╗╔╗║\n' + \
'  ║║   ║╚══╗ ║║║║ ║║╚╝║║\n' + \
'  ╚╝   ╚═══╝ ╚╝╚╝ ╚╝  ╚╝\n'

const_ardiar2 = '' + \
'        ╔═══╗ ╔═══╗  ╔══╗    ╔╗   ╔╗ ╔══╗ ╔═══╗\n' + \
'       ║╔═╗║ ║╔═╗║  ║╔╗║    ║║   ╗║ ║╔╗║ ║╔═╗║\n' + \
'        ║╚═╝║ ║╚═╝║  ║║║║    ║║ ║║║ ║╚╝║ ║╚═╝║\n' + \
'      ╚╗╔╗║ ║╔══╝  ║║║║    ║║║ ║║ ║╔╗║ ║╔══╝\n' + \
'     ║║║║ ║║       ╔╝╚╝╚╗  ║╚   ║║ ║║║║ ║║   \n' + \
'    ╚╝╚╝ ╚╝       ╚════╝  ╚╝   ╚╝ ╚╝╚╝ ╚╝   \n' + \
'  ╔════╗ ╔═══╗ ╔══╗ ╔╗     ╔╗\n' + \
'    ╚═╗╔═╝ ║╔══╝ ║╔╗║ ║║     ║║\n' + \
'       ║║      ║╚══╗ ║╚╝║ ║╚╗╔╝║\n' + \
'         ║║      ║╔══╝ ║╔╗║ ║╔╗╔╗║\n' + \
'       ║║      ║╚══╗ ║║║║ ║║╚╝║║\n' + \
'         ╚╝      ╚═══╝ ╚╝╚╝ ╚╝     ╚╝\n'

const_ardiar3 = '' + \
'        ╔═══╗ ╔═══╗  ╔══╗    ╔╗   ╔╗ ╔══╗ ╔═══╗\n' + \
'      ║╔═╗║ ║╔═╗║  ║╔╗║    ║║   ╗║ ║╔╗║ ║╔═╗║\n' + \
'        ║╚═╝║ ║╚═╝║  ║║║║    ║║ ║║║ ║╚╝║ ║╚═╝║\n' + \
'      ╚╗╔╗║ ║╔══╝  ║║║║    ║║║ ║║ ║╔╗║ ║╔══╝\n' + \
'      ║║║║ ║║       ╔╝╚╝╚╗  ║╚   ║║ ║║║║ ║║   \n' + \
'    ╚╝╚╝ ╚╝       ╚════╝  ╚╝   ╚╝ ╚╝╚╝ ╚╝   \n' + \
'    ╔════╗ ╔═══╗ ╔══╗ ╔╗     ╔╗\n' + \
'  ╚═╗╔═╝ ║╔══╝ ║╔╗║ ║║     ║║\n' + \
'         ║║      ║╚══╗ ║╚╝║ ║╚╗╔╝║\n' + \
'       ║║      ║╔══╝ ║╔╗║ ║╔╗╔╗║\n' + \
'         ║║      ║╚══╗ ║║║║ ║║╚╝║║\n' + \
'       ╚╝      ╚═══╝ ╚╝╚╝ ╚╝     ╚╝\n'

const_ardiaro = '' + \
'       ╔═══╗ ╔═══╗  ╔══╗    ╔╗   ╔╗ ╔══╗ ╔═══╗\n' + \
'       ║╔═╗║ ║╔═╗║  ║╔╗║    ║║   ╗║ ║╔╗║ ║╔═╗║\n' + \
'       ║╚═╝║ ║╚═╝║  ║║║║    ║║ ║║║ ║╚╝║ ║╚═╝║\n' + \
'       ╚╗╔╗║ ║╔══╝  ║║║║    ║║║ ║║ ║╔╗║ ║╔══╝\n' + \
'     ║║║║ ║║       ╔╝╚╝╚╗  ║╚   ║║ ║║║║ ║║   \n' + \
'     ╚╝╚╝ ╚╝       ╚════╝  ╚╝   ╚╝ ╚╝╚╝ ╚╝   \n' + \
'   ╔════╗ ╔═══╗ ╔══╗ ╔╗     ╔╗\n' + \
'   ╚═╗╔═╝ ║╔══╝ ║╔╗║ ║║     ║║\n' + \
'        ║║      ║╚══╗ ║╚╝║ ║╚╗╔╝║\n' + \
'        ║║      ║╔══╝ ║╔╗║ ║╔╗╔╗║\n' + \
'        ║║      ║╚══╗ ║║║║ ║║╚╝║║\n' + \
'        ╚╝      ╚═══╝ ╚╝╚╝ ╚╝     ╚╝\n'

text_nash = const_ardiaro
col_nach = ''

def next_text():
    global const_ardiaro
    global const_ardiar1
    global const_ardiar2
    global const_ardiar3
    r = int(random.random()*100) % 7
    s = const_ardiaro
    if r == 0:
        r = int(random.random()*100)%3
        if r == 0:
            s = const_ardiar1
        elif r == 1:
            s = const_ardiar2
        else:
            s = const_ardiar3
    root.after(150, lambda:ardiar())
    return s

def ardiar():
    global lab
    global text_nash
    global col_nach
    text_nash = next_text()
    c.delete(lab)
    lab = c.create_text(250, 145, text=text_nash, fill=col_nach, justify='center', font=('Arial', 14, 'normal'))
    #greet_label.configure(text=next_text())

def next_collor():
    global lst
    global lst_put
    shag = 17
    if lst_put == 2:
        lst[1] += shag
        if lst[1] >= lst[0]:
            lst_put = -1
    elif lst_put == -1:
        lst[0] -= shag
        if lst[0] <= 11:
            lst_put = 3
    elif lst_put == 3:
        lst[2] += shag
        if lst[2] >= lst[1]:
            lst_put = -2
    elif lst_put == -2:
        lst[1] -= shag
        if lst[1] <= 11:
            lst_put = 1
    elif lst_put == 1:
        lst[0] += shag
        if lst[0] >= lst[2]:
            lst_put = -3
    elif lst_put == -3:
        lst[2] -= 1
        if lst[2] <= 11:
            lst_put = 2
    ch1 = '0'*(2 - len(str(hex(lst[0]%256)[2:]))) + str(hex(lst[0]%256)[2:])
    ch2 = '0'*(2 - len(str(hex(lst[1]%256)[2:]))) + str(hex(lst[1]%256)[2:])
    ch3 = '0'*(2 - len(str(hex(lst[2]%256)[2:]))) + str(hex(lst[2]%256)[2:])
    root.after(10, lambda:my_mainloop())
    return f'#{ch1}{ch2}{ch3}'

pros_load = -250
def load():
    global bg_razm
    global pros_load
    pros_load += 1
    c.delete(bg_razm)
    bg_razm = c.create_image(pros_load, 135, image=bg)
    if pros_load == 235:
        file = 'BoolGame'
        os.startfile(file)
    if pros_load >= 250:
        time.sleep(2)
        root.destroy()
        return
    root.after(10, lambda:load())

def my_mainloop():
    global lab
    global text_nash
    global col_nach
    col_nach = next_collor()
    c.delete(lab)
    lab = c.create_text(250, 145, text=text_nash, fill=col_nach, justify='center', font=('Arial', 14, 'normal'))

lab = c.create_text(250, 140, text=const_ardiaro, fill="Black", justify='center', font=('Arial', 14, 'normal'))

root.after(10, lambda:my_mainloop())
root.after(150, lambda:ardiar())
root.after(10, lambda:load())

root.mainloop()
