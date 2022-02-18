import tkinter as tk


root = tk.Tk()

root.geometry('600x500+100+100')
root.resizable(False, False)


def summa():
    answer_label.config(text=int(entry_a.get())+int(entry_b.get()))


label_a = tk.Label(root, text='Введите a')
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text='Введите b')
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

button = tk.Button(root, text='Submit', command=summa)
button.grid(row=2, column=0)
answer_label = tk.Label(root, text='')
answer_label.grid(row=3, column=0)


root.mainloop()
