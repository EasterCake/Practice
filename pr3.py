from tkinter import *
import tkinter as tk
from sympy import *


def derivative():
        try:
          output_field.delete(0, END)
          equation = input_field.get()
          x = symbols("x")
          differential = diff(equation, x)
          output_field.insert(0, differential)
        except Exception:
            output_field.delete(0, END)
            output_field.insert(0, 'Поставте знак * убрав = ')

def definite_integral():
              integral()
              eq = output_field.get()
              eq_low = eq
              upper_limit = upper_limit_field.get()
              lower_limit = lower_limit_field.get()
              output_field.delete(0, END)
              try:
                eq_edited = eq.replace("x", upper_limit, -1)
                eq_low_ed = eq_low.replace("x", lower_limit, -1)
                upper_res = str(eval(eq_edited[:]))
                lower_res = str(eval(eq_low_ed[:]))
                res = str(float(upper_res) - float(lower_res))
                output_field.insert(END, res)
              except Exception:
                output_field.delete(0, END)
                output_field.insert(0, 'Error')


def integral():
    output_field.delete(0, END)
    equation = input_field.get()
    x = symbols('x')
    integration = integrate(equation, x)
    output_field.insert(0, integration)


def btn_click(item):
        global expression, result
        output_field.delete(0, END)
        check_str = input_field.get()
        expression = input_field.get()
        eq_with_x = False
        try:
            expression += item
            if item == '=':
                for char in check_str:
                    if char == 'x' or char == 'х':
                        eq_with_x = True
                if eq_with_x:
                    output_field.insert(0, " Вам нужна кнопка ` ")
                else:
                    result = str(eval(expression[:-1]))
                    output_field.insert(END, result)
                    expression = ''
            input_field.insert(END, item)
        except ZeroDivisionError:
            output_field.delete(0, END)
            output_field.insert(0, 'Деление на 0')
        except SyntaxError:
            output_field.delete(0, END)
            output_field.insert(0, 'Error')



def bt_clear1():
        global expression
        ex = int(len(expression[:]))
        input_field.delete(ex -1)







def bt_clear():
        global expression
        expression = ''
        input_field.delete(0, END)
        output_field.delete(0, END)





root = Tk()
root.iconbitmap('cap.ico')
root.title("Калькулятор")
root.geometry("515x380")
root.resizable(0, 0)
l = tk.Entry(root)
k = tk.Entry(root)
frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky='nsew')
input_field = Entry(frame_input, font='Arial 15 bold', width=24)
output_field = Entry(frame_input, font='Arial 15 bold', width=24)
input_field.pack(fill=BOTH, padx=3)
output_field.pack(fill=BOTH, padx=3)


upper_limit_label = Label(text="Интегрирование выражений")
upper_limit_label.grid(column=6, row=0, padx=0)

definite_integral_button = tk.Button(text="Вычислить определённый интеграл", command=definite_integral)
definite_integral_button.grid(column=6, row=1)




upper_limit_label = Label(text="Введите верхний предел интегрирования:")
upper_limit_label.grid(column=6, row=2, padx=2)

upper_limit_field = tk.Entry()
upper_limit_field.grid(column=6, row=3, padx=2)

lower_limit_label = Label(text="Введите нижний предел интегрирования:")
lower_limit_label.grid(column=6, row=4, padx=2)

lower_limit_field = tk.Entry()
lower_limit_field.grid(column=6, row=5, padx=2)

integral_button = tk.Button(text="Вычислить неопределённый интеграл", command=integral)
integral_button.grid(column=6, row=6)



buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'),

           )

expression = ''

button = Button(root, text='C', command=lambda: bt_clear())
button.grid(row=+1, padx=3, column=3, sticky='nsew')

button = Button(root, text='Del', command=lambda: bt_clear1())
button.grid(row=+1, padx=2, column=2, sticky='nsew')

button = Button(root, text='`', command=derivative)
button.grid(row=+1, padx=2, column=1, sticky='nsew')





for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 3, column=col,
                                                                                   sticky='nsew', padx=3, pady=1)

button = (("**", "x",'(',')'),
          )

for row in range(1):
    for col in range(len(button) + 3):
        Button(root, width=2, height=3, text=button[row][col],
               command=lambda row=row, col=col: btn_click(button[row][col])).grid \
            (row=row + 2, column=col, sticky='nsew', padx=3, pady=1)

root.mainloop()
