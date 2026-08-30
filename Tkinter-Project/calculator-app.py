import tkinter as tk

def press(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        answer = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, answer)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


window = tk.Tk()
window.title("Calculator")
window.geometry("320x430")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=15,
    ipady=10
)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2)
]

for text, row, column in buttons:
    button = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda value=text: press(value)
    )
    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

clear_button = tk.Button(
    window,
    text="C",
    font=("Arial", 18),
    width=5,
    height=2,
    command=clear
)
clear_button.grid(row=4, column=3, padx=5, pady=5)

equal_button = tk.Button(
    window,
    text="=",
    font=("Arial", 18),
    width=22,
    height=2,
    command=calculate
)
equal_button.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10
)

window.mainloop()