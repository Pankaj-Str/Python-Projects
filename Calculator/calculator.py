import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20,
              command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
