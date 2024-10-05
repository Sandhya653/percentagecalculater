import tkinter as tk
from tkinter import messagebox

# Function to calculate the percentage
def calculate_percentage():
    try:
        total_marks = float(entry_total_marks.get())
        obtained_marks = float(entry_obtained_marks.get())
        percentage = (obtained_marks / total_marks) * 100
        result_label.config(text=f"Percentage: {percentage:.2f}%")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Student Percentage Calculator")

# Create and place the labels and entries for total marks and obtained marks
label_total_marks = tk.Label(root, text="Total Marks:")
label_total_marks.grid(row=0, column=0, padx=10, pady=10)

entry_total_marks = tk.Entry(root)
entry_total_marks.grid(row=0, column=1, padx=10, pady=10)

label_obtained_marks = tk.Label(root, text="Obtained Marks:")
label_obtained_marks.grid(row=1, column=0, padx=10, pady=10)

entry_obtained_marks = tk.Entry(root)
entry_obtained_marks.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_percentage)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Percentage: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()


