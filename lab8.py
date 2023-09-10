from tkinter import *
import lab6 as main

matrix = []


def button1():
    global matrix
    n = txt.get()
    if lbl2.cget('text') == '':
        answer = main.start(n)
        if type(answer) == str:
            lbl.configure(text=answer)
        else:
            m = answer
            lbl2.configure(text="Начальная матрица: \n" + main.print_matrix(m))
            lbl.configure(text='Введите желаемый тип перебора массива (rec, iter):')
            txt.delete(0, END)
            matrix = m
    else:
        answer = txt.get()
        if answer == 'iter':
            answer = main.F_iter(matrix, len(matrix[0]))
            windowAnswer = Tk()
            windowAnswer.title('Answer')
            anlbl = Label(windowAnswer, width=30, height=(answer[0] + 1) * 7,
                          text='Кол-во вариантов: ' + str(answer[0]) + '\n', anchor='nw', bg='red')
            for i in range(answer[0]):
                anlbl.configure(text=anlbl.cget('text') + '\n' + main.print_matrix(answer[1][i]))
            ex = Button(windowAnswer, text='Выход', command=exit)
            anlbl.grid()
            ex.place(x=300, y=150)
            windowAnswer.geometry('500x' + str((answer[0] + 1) * 200))
            windowAnswer.mainloop()
        elif answer == 'rec':
            answer = main.F_iter(matrix, len(matrix[0]))
            windowAnswer = Tk()
            windowAnswer.title('Answer')
            anlbl = Label(windowAnswer, width=30, height=(answer[0] + 1) * 7,
                          text='Кол-во вариантов: ' + str(answer[0]) + '\n', anchor='nw', bg='red')
            for i in range(answer[0]):
                anlbl.configure(text=anlbl.cget('text') + '\n' + main.print_matrix(answer[1][i]))
            ex = Button(windowAnswer, text='Выход', command=exit)
            anlbl.grid()
            ex.place(x=300, y=150)
            windowAnswer.geometry('500x' + str((answer[0] + 1) * 200))
            windowAnswer.mainloop()
        else:
            lbl.configure(text='Введите rec для рекурсивного перебора, iter для итеративного')


windowEntry = Tk()
windowEntry.title('Lab 8')

button = Button(windowEntry, text='Продолжить', command=button1)
txt = Entry(windowEntry, width=10)
lbl = Label(windowEntry, width=45, text='Размер матрицы: ')
lbl2 = Label(windowEntry, width=60, height=20, text='')

lbl.place(x=30, y=150)
txt.place(x=100, y=200)
button.place(x=100, y=250)
lbl2.place(x=80, y=300)

txt.focus()
windowEntry.geometry('800x600')
windowEntry.mainloop()

def start():
    windowEntry = Tk()
    windowEntry.title('Lab 8')

    button = Button(windowEntry, text='Продолжить', command=button1)
    txt = Entry(windowEntry, width=10)
    lbl = Label(windowEntry, width=45, text='Размер матрицы: ')
    lbl2 = Label(windowEntry, width=60, height=20, text='')

    lbl.place(x=30, y=150)
    txt.place(x=100, y=200)
    button.place(x=100, y=250)
    lbl2.place(x=80, y=300)

    txt.focus()
    windowEntry.geometry('800x600')
    windowEntry.mainloop()


