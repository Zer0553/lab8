from tkinter import *
import random
import copy

matrix = []
allmat = []

def number_check(n):
    while True:
        try:
            k = int(n)
            if k > 0:
                return k
            else:
                return 'Должно быть положиельное число.'

        except ValueError:
            if n == 'test':
                return 'test'
            return 'Введенное значение не является числом.'


def print_matrix(matrix):
    cuteM = ''
    for row in matrix:
        for elem in row:
            cuteM += '{:4}'.format(elem)
        cuteM += ' \n'
    return cuteM


def F_rec(matrix, row, column, count, n, exist=[[], []]):
    global allmat
    if row == len(matrix):
        return [count - 1, allmat]
    F_rec(copy.deepcopy(matrix), row + 1, column + 1, count, n)

    if matrix[row][row] == 0 and row not in exist[0]:
        exist[0].append(row)
        new_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
        allmat.append(new_matrix)
        count[0] += 1
    if matrix[row][n - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
        exist[1].append(row)
        new_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            new_matrix[row][i], new_matrix[n - i][n - column] = new_matrix[n - i][n - column],  new_matrix[row][i]
        allmat.append(new_matrix)
        count[0] += 1
    F_rec(matrix, row + 1, column + 1, count, n, exist)


def F_iter(matrix, n):
    global allmat
    count = 0
    exist=[[], []]
    stack = [(copy.deepcopy(matrix), 0, 0)]
    k = n - 1
    while stack:
        matrix, row, column = stack.pop()
        if row == len(matrix):
            count += 1
            continue
        stack.append((copy.deepcopy(matrix), row + 1, column + 1))
        if matrix[row][row] == 0 and row not in exist[0]:
            exist[0].append(row)
            new_matrix = copy.deepcopy(matrix)
            for i in range(len(matrix)):
                new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
            allmat.append(new_matrix)
            stack.append((matrix, row + 1, column + 1))
        if matrix[row][k - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
            exist[1].append(row)
            new_matrix = copy.deepcopy(matrix)
            for i in range(len(matrix)):
                new_matrix[row][i], new_matrix[k - i][k - column] = new_matrix[k - i][k - column],  new_matrix[row][i]
            allmat.append(new_matrix)
            stack.append((matrix, row + 1, column + 1))
    return [count - 1, allmat]


def start(n):
    n = number_check(n)
    try:
        array = [[random.randint(0, 5) for i in range(n)] for j in range(n)]
    except TypeError:
        return n
    return array


def rec9(array, n):
    count = [0]
    print('Рекурсивный перебор возможных вариантов.')
    F_rec(array, 0, 0, count, n - 1)


def button1():
    global matrix
    n = entr.get()
    if txt.get('2.0') == '':
        answer = start(n)
        if type(answer) == str:
            if answer == 'test':
                m = [[1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1]]
                txt.insert('1.0', "Начальная матрица: \n")
                txt.insert(END, print_matrix(m))
                lbl.configure(text='Введите желаемый тип перебора массива (rec, iter):')
                entr.delete(0, END)
                matrix = m
            lbl.configure(text=answer)
        else:
            m = answer
            txt.insert('1.0', "Начальная матрица: \n")
            txt.insert(END, print_matrix(m))
            lbl.configure(text='Введите желаемый тип перебора массива (rec, iter):')
            entr.delete(0, END)
            matrix = m
    else:
        try:
            answer = entr.get()
            if answer == 'iter':
                windowEntry.destroy()
                answer = F_iter(matrix, len(matrix[0]))
                windowAnswer = Tk()
                windowAnswer.title('Answer')
                txt_answ = Text(windowAnswer, width=100, height=50)
                scrolmat = Scrollbar(windowAnswer, orient="vertical", command=txt_answ.yview)
                if answer[0] > 0:
                    txt_answ.insert('1.0', 'Кол-во вариантов ' + str(answer[0]) + '\n')
                    for i in range(answer[0]):
                        txt_answ.insert(END, str(print_matrix(answer[1][i])) + '\n')
                        txt_answ.insert(END, '\n')
                    scrolmat.place(x=781, y=0, height=800)
                    txt_answ.grid()
                    txt_answ["yscrollcommand"] = scrolmat.set
                    windowAnswer.geometry('800x800')
                else:
                    txt_answ.insert('1.0', 'Матрица не подошла под условие ')
                    txt_answ.grid()
                    txt_answ["yscrollcommand"] = scrolmat.set
                    windowAnswer.geometry('800x800')
                windowAnswer.mainloop()
            elif answer == 'rec':
                answer = F_iter(matrix, len(matrix[0]))
                windowAnswer = Tk()
                windowAnswer.title('Answer')
                txt_answ = Text(windowAnswer, width=100, height=50)
                scrolmat = Scrollbar(windowAnswer, orient="vertical", command=txt_answ.yview)
                if answer[0] > 0:
                    txt_answ.insert('1.0', 'Кол-во вариантов ' + str(answer[0]) + '\n')
                    for i in range(answer[0]):
                        txt_answ.insert(END, str(print_matrix(answer[1][i])) + '\n')
                        txt_answ.insert(END, '\n')
                    scrolmat.place(x=781, y=0, height=800)
                    txt_answ.grid()
                    txt_answ["yscrollcommand"] = scrolmat.set
                    windowAnswer.geometry('800x800')
                else:
                    txt_answ.insert('1.0', 'Матрица не подошла под условие ')
                    txt_answ.grid()
                    txt_answ["yscrollcommand"] = scrolmat.set
                    windowAnswer.geometry('800x800')
                windowAnswer.mainloop()
        except:
            lbl.configure(text='Введите rec для рекурсивного перебора, iter для итеративного')

windowEntry = Tk()
windowEntry.title('Lab 8')

button = Button(windowEntry, text='Продолжить', command=button1)
entr = Entry(windowEntry, width=10)
lbl = Label(windowEntry, width=45, text='Размер матрицы: ')
txt = Text(windowEntry, width=100)
scrollbar = Scrollbar(orient="vertical", command=txt.yview)
info = Label(windowEntry, text='Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путем'
                               ' \n перестановки строк и столбцов, в которых диагональный элемент равен нулю.'
                               ' \n + сумма элементов сторки с диагональным элементом равным нулю не должна быть больше размера матрицы уноженного на 5'
                               ' \n + переставляем только четные столбцы и строки')

lbl.place(x=30, y=150)
entr.place(x=100, y=200)
button.place(x=100, y=250)
txt.place(x=0, y=300)
scrollbar.place(x=800, y=300, height=300)
info.place(x=30, y=50)

txt["yscrollcommand"] = scrollbar.set
entr.focus()
windowEntry.geometry('900x600')
windowEntry.mainloop()

