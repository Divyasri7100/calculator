import tkinter as tk

def calculate_percentage():
    try:
        number = float(entry_number.get())
        percentage = float(entry_percentage.get())
        result = (number * percentage) / 100
        result_label.config(text=f"{percentage}% of {number} is {result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

# Create the main window
window = tk.Tk()
window.title("Percentage Calculator")

# Create entry fields and labels
label_number = tk.Label(window, text="Number:")
label_percentage = tk.Label(window, text="Percentage (%):")

entry_number = tk.Entry(window)
entry_percentage = tk.Entry(window)

label_number.grid(row=0, column=0)
label_percentage.grid(row=1, column=0)
entry_number.grid(row=0, column=1)
entry_percentage.grid(row=1, column=1)

# Create a button to calculate the percentage
calculate_button = tk.Button(window, text="Calculate Percentage", command=calculate_percentage)
calculate_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(window, text="", padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Start the main loop
window.mainloop()
