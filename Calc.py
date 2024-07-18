import tkinter as tk

def bc(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = str(eval(expression))
            display.set(expression)
        except:
            expression = "Error"
            display.set(expression)
    elif text == "C":
        expression = ""
        display.set("")
    else:
        expression += text
        display.set(expression)

root = tk.Tk()
root.title("Calculator")

expression = ""

display = tk.StringVar()
display.set("")

dispframe = tk.Frame(root, width=400, height=50, bg="grey")
dispframe.pack(side=tk.TOP)

displab = tk.Label(dispframe, textvariable=display, font=("Arial", 18), anchor="e", padx=10)
displab.pack(fill=tk.BOTH, expand=True)

butframe = tk.Frame(root)
butframe.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)
]

for button in buttons:
    if len(button) == 3:
        text, row, col = button
        rowspan = columnspan = 1
    elif len(button) == 5:
        text, row, col, rowspan, columnspan = button

    button = tk.Button(butframe, text=text, font=("Arial", 18), padx=20, pady=10)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
    button.bind("<Button-1>", bc)

root.mainloop()
