# Day 66: Calculator with simple GUI
from tkinter import Tk, ttk

# main window
window = Tk()
window.title('Calculator')
window.geometry('300x200')

answer = 0
last_number = 0
operator = None


def enter_number(value):
    global answer
    answer = f'{answer}{value}'
    answer = int(answer)
    label['text'] = answer


def set_last_number(op):
    global answer, last_number, operator
    last_number = answer
    answer = 0
    if op == '+':
        operator = '+'
    elif op == '-':
        operator = '-'
    elif op == '*':
        operator = '*'
    elif op == '/':
        operator = '/'
    label['text'] = answer


def calculate():
    global answer, last_number, operator
    total = 0
    if operator == '+':
        total = last_number + answer
    elif operator == '-':
        total = last_number - answer
    elif operator == '*':
        total = last_number * answer
    elif operator == '/':
        total = last_number / answer
    answer = total
    label['text'] = answer


# frame
frm = ttk.Frame(window, padding=10)
frm.grid()

# label
label = ttk.Label(frm, text=answer, width=15)
label.grid(column=4, row=0)

# buttons
one = ttk.Button(frm, text='1', width=3, command=lambda: enter_number(1))
one.grid(column=1, row=1)

two = ttk.Button(frm, text='2', width=3, command=lambda: enter_number(2))
two.grid(column=2, row=1)

three = ttk.Button(frm, text='3', width=3, command=lambda: enter_number(3))
three.grid(column=3, row=1)

four = ttk.Button(frm, text='4', width=3, command=lambda: enter_number(4))
four.grid(column=1, row=2)

five = ttk.Button(frm, text='5', width=3, command=lambda: enter_number(5))
five.grid(column=2, row=2)

six = ttk.Button(frm, text='6', width=3, command=lambda: enter_number(6))
six.grid(column=3, row=2)

seven = ttk.Button(frm, text='7', width=3, command=lambda: enter_number(7))
seven.grid(column=1, row=3)

eight = ttk.Button(frm, text='8', width=3, command=lambda: enter_number(8))
eight.grid(column=2, row=3)

nine = ttk.Button(frm, text='9', width=3, command=lambda: enter_number(9))
nine.grid(column=3, row=3)

zero = ttk.Button(frm, text='0', width=3, command=lambda: enter_number(0))
zero.grid(column=2, row=4)


add = ttk.Button(frm, text='+', width=3,
                 command=lambda: set_last_number('+'))
add.grid(column=5, row=1)

subtract = ttk.Button(frm, text='-', width=3,
                      command=lambda: set_last_number('-'))
subtract.grid(column=5, row=2)

multiply = ttk.Button(frm, text='*', width=3,
                      command=lambda: set_last_number('*'))
multiply.grid(column=6, row=1)

divide = ttk.Button(frm, text='/', width=3,
                    command=lambda: set_last_number('/'))
divide.grid(column=6, row=2)

equals = ttk.Button(frm, text='=', width=3, command=calculate)
equals.grid(column=5, row=4)

# run loop
window.mainloop()
