import tkinter as tk
from tkinter import Label, Entry, Button

def calculate_emi():
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 12 / 100
    tenure = int(tenure_entry.get()) * 12

    emi = principal * interest_rate * (1 + interest_rate) ** tenure / ((1 + interest_rate) ** tenure - 1)

    result_label.config(text=f'EMI: {emi:.2f}')

# Create the main window
root = tk.Tk()
root.title("EMI Calculator")

# Create labels, entry fields, and a button
principal_label = Label(root, text="Principal Amount")
principal_label.pack()
principal_entry = Entry(root)
principal_entry.pack()

interest_rate_label = Label(root, text="Interest Rate (% p.a.)")
interest_rate_label.pack()
interest_rate_entry = Entry(root)
interest_rate_entry.pack()

tenure_label = Label(root, text="Tenure (months)")
tenure_label.pack()
tenure_entry = Entry(root)
tenure_entry.pack()

calculate_button = Button(root, text="Calculate EMI", command=calculate_emi)
calculate_button.pack()

result_label = Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
