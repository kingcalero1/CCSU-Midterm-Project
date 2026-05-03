import tkinter as tk
from tkinter import messagebox

# Functions

def calculate_grade():
    try:
        s1 = float(entry1.get())
        s2 = float(entry2.get())
        s3 = float(entry3.get())

        avg = (s1 + s2 + s3) / 3

        # determine letter grade
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        result_label.config(text=f"Average: {avg:.2f} | Grade: {grade}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_label.config(text="")

# -------------------------
# Window
# -------------------------
root = tk.Tk()
root.title("Student Grade App")
root.geometry("350x300")

# -------------------------
# Labels + Entries
# -------------------------
tk.Label(root, text="Test 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Test 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Test 3").pack()
entry3 = tk.Entry(root)
entry3.pack()

# -------------------------
# Buttons
# -------------------------
tk.Button(root, text="Calculate", command=calculate_grade).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack()

# -------------------------
# Output
# -------------------------
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()