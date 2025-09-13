import tkinter as tk

def convert_units():
    try:
        input_value = float(entry_value.get())
        conversion_type = unit_conversion_type.get()

        if conversion_type == "Meters to Feet":
            result = input_value * 3.28084
            result_label.config(text=f"{input_value} meters is equal to {result:.2f} feet")
        elif conversion_type == "Feet to Meters":
            result = input_value / 3.28084
            result_label.config(text=f"{input_value} feet is equal to {result:.2f} meters")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Unit Conversion")

# Create entry fields and labels
label_value = tk.Label(window, text="Enter Value:")
label_conversion = tk.Label(window, text="Select Conversion:")

entry_value = tk.Entry(window)

unit_conversion_type = tk.StringVar()
unit_conversion_type.set("Meters to Feet")

conversion_dropdown = tk.OptionMenu(window, unit_conversion_type, "Meters to Feet", "Feet to Meters")

label_value.grid(row=0, column=0)
label_conversion.grid(row=1, column=0)
entry_value.grid(row=0, column=1)
conversion_dropdown.grid(row=1, column=1)

# Create a button to perform the unit conversion
convert_button = tk.Button(window, text="Convert", command=convert_units)
convert_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(window, text="", padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Start the main loop
window.mainloop()
