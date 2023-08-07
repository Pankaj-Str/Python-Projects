# Creating a calculator with a graphical user interface (GUI)

We'll use the `tkinter` library, which comes with Python by default, to create the GUI. Here's a step-by-step guide:

1. **Import `tkinter`:**
   Start by importing the `tkinter` library and creating the main window.

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
```

2. **Create Display:**
   Create a display field where the user inputs and results will be shown.

```python
display = tk.Entry(root, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)
```

3. **Define Button Click Function:**
   Create a function that handles button clicks and updates the display.

```python
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))
```

4. **Create Buttons:**
   Create buttons for numbers (0-9) and basic operations (+, -, *, /).

```python
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
```

5. **Implement Calculation:**
   Create a function to perform calculations when the '=' button is clicked.

```python
def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
```

6. **Run the GUI:**
   Run the GUI loop to start the calculator application.

```python
root.mainloop()
```

The complete code should look like this:

```python
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
```

Save this code to a `.py` file and run it using your Python interpreter. It will open a simple calculator GUI with number buttons and basic arithmetic operations. You can expand upon this by adding more functionality, error handling, and a polished design.
