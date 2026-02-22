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
	#change the color
    root.configure(bg="")
    root.title("Sean Calculator")

    BUTTON_HEIGHT = 1
    BUTTON_WIDTH  = 7

	# setting the display screem
    display = StringVar()
    entry = Entry(root, textvariable=display)	
    entry.grid(columnspan=4, ipadx=70, sticky="nsew")

	# 数字按钮布局：(数字, row行, column列)
	buttons = [
        (1, 2, 0), (2, 2, 1), (3, 2, 2),
        (4, 3, 0), (5, 3, 1), (6, 3, 2),
        (7, 4, 0), (8, 4, 1), (9, 4, 2),
        (0, 5, 0)
    ]

    # 用 for 循环批量创建数字按钮
    for num, row, col in buttons:
        btn = Button(root, text=str(num), fg='black', bg='red',
                     command=lambda n=num: press(n),
                     height = BUTTON_HEIGHT, width = BUTTON_WIDTH)
        btn.grid(row=row, column=col)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='black', bg='red', command=lambda: press('*'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='black', bg='red', command=lambda: press('/'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    div.grid(row=5, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    dot.grid(row=6, column=0)

	# fix the size of the table, make it empty blank so the table will be automatically fit 
    root.update()
    root.geometry("")
    root.mainloop()
