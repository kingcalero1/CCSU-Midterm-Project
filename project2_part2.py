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
root.configure(bg='#A5D6FF')

# -------------------------
# Logo
# -------------------------
try:
    img = Image.open('logo.PNG')
    try:
        img = img.resize((130, 130), Image.Resampling.LANCZOS)
    except AttributeError:
        img = img.resize((130, 130), Image.ANTIALIAS)

    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    white_bg.paste(img, (0, 0), img)

    logo = ImageTk.PhotoImage(white_bg)
    logoLabel = Label(root, image=logo, bg='#A5D6FF')
    logoLabel.place(x=30, y=20)

except:
    Label(root, text="CCSU", font=('Arial', 28, 'bold'), bg='#A5D6FF', fg='#003087').place(x=40, y=40)

# -------------------------
# Load CSV
# -------------------------
data = pd.read_csv("examfile.csv")

# Output Label - Centered
lb = Label(root, justify="left", bg='#A5D6FF', anchor="nw",
           font=('Arial', 10), padx=20, pady=10, fg="black")

label_placed = False

# -------------------------
# Show output function
# -------------------------
def show_output():
    global label_placed
    if not label_placed:
        lb.place(x=175, y=255, width=310, height=270)
        label_placed = True

# -------------------------
# Button functions
# -------------------------
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
# Buttons
# -------------------------

# First row
Button(root, text='Calendar', command=calender,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=10).place(x=95, y=175)

Button(root, text='Buildings', command=building,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=10).place(x=225, y=175)

Button(root, text='Faculty', command=faculty,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=10).place(x=355, y=175)

# Second row
Button(root, text='School of Business', command=school_business,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=16).place(x=95, y=210)

Button(root, text='MIS Department', command=mis_department,
       bg="#004080", fg="white", font=('Arial', 9, 'bold'), width=16).place(x=310, y=210)

# -------------------------
root.mainloop()