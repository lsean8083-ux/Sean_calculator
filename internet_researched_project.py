from tkinter import *
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Simple Calculator")
    root.geometry("270x150")

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=70)

				# 数字按钮布局：(数字, row行, column列)
				buttons = [
        (1, 2, 0), (2, 2, 1), (3, 2, 2),
        (4, 3, 0), (5, 3, 1), (6, 3, 2),
        (7, 4, 0), (8, 4, 1), (9, 4, 2),
        (0, 5, 0)
    ]

    # 用 for 循环批量创建
    for num, row, col in buttons:
        btn = Button(root, text=str(num), fg='black', bg='red',
                     command=lambda n=num: press(n),
                     height=1, width=7)
        btn.grid(row=row, column=col)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='black', bg='red', command=lambda: press('*'), height=1, width=7)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='black', bg='red', command=lambda: press('/'), height=1, width=7)
    div.grid(row=5, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=1, width=7)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
    dot.grid(row=6, column=0)

    root.mainloop()