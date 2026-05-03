from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU Mobile App')
root.geometry("650x560")
root.resizable(0, 0)
root.configure(bg='#A5D6FF')        # Light blue background

# -------------------------
# Logo with clean WHITE background (no blending)
# -------------------------
try:
    img = Image.open('logo.PNG')
    # Resize logo
    try:
        img = img.resize((130, 130), Image.Resampling.LANCZOS)
    except AttributeError:
        img = img.resize((130, 130), Image.ANTIALIAS)

    # Create solid white background behind the logo
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    white_bg.paste(img, (0, 0), img)

    logo = ImageTk.PhotoImage(white_bg)
    logoLabel = Label(root, image=logo, bg='#A5D6FF')
    logoLabel.place(x=30, y=20)

except:
    # Fallback if logo file not found
    Label(root, text="CCSU", font=('Arial', 28, 'bold'), bg='#A5D6FF', fg='#003087').place(x=40, y=40)

# -------------------------
# Load CSV data
# -------------------------
data = pd.read_csv("examfile.csv")

# Output Label - NO visible box (transparent on background)
lb = Label(root, justify="left", bg='#A5D6FF', anchor="nw",
           font=('Arial', 10), padx=20, pady=10, fg="black")

label_placed = False

# -------------------------
# FUNCTIONS (using your exact data logic)
# -------------------------
def show_output():
    global label_placed
    if not label_placed:
        lb.place(x=80, y=255, width=490, height=270)
        label_placed = True

def calender():
    show_output()
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def building():
    show_output()
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def faculty():
    show_output()
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def school_business():
    show_output()
    info = """School of Business Departments:
- Accounting
- Finance
- Management & Organization
- Marketing
- Management Information Systems (MIS)
- Business Analytics"""
    lb.config(text=info)

def mis_department():
    show_output()
    info = """MIS Department Core Courses:
- Intro to MIS
- Database Management
- Systems Analysis & Design
- Business Analytics / Data Visualization
- Network & Information Security
- Project Management
- Python for Business Applications"""
    lb.config(text=info)

# -------------------------
# Buttons - Positioned to match screenshot
# -------------------------

# First row: Calendar, Buildings, Faculty
Button(root, text='Calendar', command=calender,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=12).place(x=85, y=175)

Button(root, text='Buildings', command=building,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=12).place(x=225, y=175)

Button(root, text='Faculty', command=faculty,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=12).place(x=365, y=175)

# Second row: School of Business and MIS Department
Button(root, text='School of Business', command=school_business,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=18).place(x=130, y=210)

Button(root, text='MIS Department', command=mis_department,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=18).place(x=310, y=210)

# -------------------------
root.mainloop()