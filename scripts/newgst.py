import tkinter as tk
from tkinter import messagebox

def calculate_gst():
    try:
        amount = float(entry_amount.get())
        gst_rate = float(entry_gst.get())
        
        gst_amount = amount * (gst_rate / 100)
        total_amount = amount + gst_amount

        label_result.config(text=f"GST: ₹{gst_amount:.2f}\nTotal: ₹{total_amount:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("GST Calculator")

# Labels and entries
tk.Label(root, text="Amount (₹):").pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

tk.Label(root, text="GST Rate (%):").pack(pady=5)
entry_gst = tk.Entry(root)
entry_gst.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate_gst).pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=5)

root.mainloop()
