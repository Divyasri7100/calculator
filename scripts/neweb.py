import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        units = float(entry_units.get())
        if units < 0:
            messagebox.showerror("Error", "Units cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of units.")
        return
    L=[[0],[0,1.5],[0,2,3],[0,3.5,4.6,6.6]]
    if units >= 0 and units<=100 :
        total_cost = units * 0
    elif units <= 200:
        total_cost = (units - 100) * L[1][1]
    elif units <=500:
        total_cost = 100*L[2][1]+(units-200) * L[2][2]
    else:
        total_cost =100*L[3][1]+300*L[3][2]+(units-500)*L[3][3]
    
    total_cost = round(total_cost, 2)
    
    result_label.config(text=f"Total Cost: ₹{total_cost:.2f}")

# Create the main window
root = tk.Tk()
root.title("Electricity Bill Calculator")

# Create and configure input label and entry field
unit_label = tk.Label(root, text="Enter the number of units:")
unit_label.pack()
entry_units = tk.Entry(root)
entry_units.pack()

# Create and configure calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_bill)
calculate_button.pack()

# Create and configure result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
