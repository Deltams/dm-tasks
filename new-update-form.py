import random
from tkinter import *
root = Tk()
root.title('TEST')
root.geometry('600x500+100+100')
root.resizable(False, False)


def submit():
    if entry.get() == label1.cget('text'):
        label2.configure(text=f'Вы ответили верно! Ваш ответ {entry.get()}', fg='green')
    else:
        label2.configure(text=f'Вы ответили неверно! Ваш ответ {1}', fg='red')
    help_button.pack()
    submit_button['state'] = DISABLED
    entry['state'] = DISABLED
    entry.delete(0, 'end')


def go_next():
    submit_button['state'] = NORMAL
    entry['state'] = NORMAL
    entry.delete(0, 'end')
    label1.configure(text=f'{random.random():.2f}')
    label2.configure(text='')
    help_button.pack_forget()


label1 = Label(root, text=f'{random.random():.2f}')
label1.pack()

label2 = Label(root, text='')
label2.pack()

entry = Entry(root)
entry.pack()

submit_button = Button(text='Ответить', command=submit)
submit_button.pack()

help_button = Button(text='Новое задание', command=go_next)


root.mainloop()
