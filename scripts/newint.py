import tkinter as tk

def calculate_simple_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    interest = (principal * rate * time) / 100
    result_label.config(text=f"Simple Interest: {interest}")

def calculate_compound_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    n = int(compound_frequency_entry.get())
    amount = principal * (1 + (rate / (n * 100)))**(n * time)
    interest = amount - principal
    result_label.config(text=f"Compound Interest: {interest}")

# Create a tkinter window
window = tk.Tk()
window.title("Interest Calculator")

# Create and place labels and entry fields
principal_label = tk.Label(window, text="Principal Amount:")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

rate_label = tk.Label(window, text="Annual Interest Rate (%):")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

time_label = tk.Label(window, text="Time (years):")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

compound_frequency_label = tk.Label(window, text="Compound Frequency (per year):")
compound_frequency_label.pack()
compound_frequency_entry = tk.Entry(window)
compound_frequency_entry.pack()

# Create buttons to calculate interest
simple_interest_button = tk.Button(window, text="Calculate Simple Interest", command=calculate_simple_interest)
simple_interest_button.pack()

compound_interest_button = tk.Button(window, text="Calculate Compound Interest", command=calculate_compound_interest)
compound_interest_button.pack()

# Display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
