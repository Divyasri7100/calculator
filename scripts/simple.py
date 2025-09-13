import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except:
        messagebox.showerror("Error", "Invalid Input")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", width=23, height=2, font=("Arial", 16),
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
