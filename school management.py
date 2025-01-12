import tkinter as tk
from tkinter import messagebox
import mysql.connector as x

# Database connection
con = x.connect(host='localhost', user='root', password='Vinu@2004', database='vasavi')
cur = con.cursor()

# Functions
def stuInsert():
    roll = roll_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    clas = class_entry.get()
    
    if roll and name and age and clas:
        try:
            sql = "INSERT INTO stud (roll, name, age, class) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (roll, name, age, clas))
            con.commit()
            messagebox.showinfo("Success", "Record inserted successfully")
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def stuview():
    try:
        cur.execute("SELECT * FROM stud")
        results = cur.fetchall()
        output_text.delete(1.0, tk.END)
        for row in results:
            output_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def searchstu():
    condition = search_entry.get()
    try:
        cur.execute(f"SELECT * FROM stud WHERE {condition}")
        results = cur.fetchall()
        output_text.delete(1.0, tk.END)
        for row in results:
            output_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def removestu():
    roll = roll_entry.get()
    try:
        cur.execute("DELETE FROM stud WHERE roll=%s", (roll,))
        con.commit()
        messagebox.showinfo("Success", "Record deleted successfully")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def updatestu():
    roll = roll_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    clas = class_entry.get()
    
    if roll:
        try:
            # Fetch the record to ensure it exists
            cur.execute("SELECT * FROM stud WHERE roll=%s", (roll,))
            results = cur.fetchall()
            
            if not results:
                messagebox.showwarning("No Record", "No matching details available")
            else:
                # Update the record
                cur.execute("UPDATE stud SET name=%s, age=%s, class=%s WHERE roll=%s", (name, age, clas, roll))
                con.commit()
                messagebox.showinfo("Success", "Record updated successfully")
                clear_entries()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter roll number")

def clear_entries():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Student Management System")

# Entry fields
tk.Label(root, text="Roll:").grid(row=0, column=0)
roll_entry = tk.Entry(root)
roll_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Class:").grid(row=3, column=0)
class_entry = tk.Entry(root)
class_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Student", command=stuInsert).grid(row=4, column=0, pady=10)
tk.Button(root, text="View Students", command=stuview).grid(row=4, column=1, pady=10)
tk.Button(root, text="Update Student", command=updatestu).grid(row=5, column=0, pady=10)
tk.Button(root, text="Delete Student", command=removestu).grid(row=5, column=1, pady=10)

# Search field
tk.Label(root, text="Search condition (SQL):").grid(row=6, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1)
tk.Button(root, text="Search", command=searchstu).grid(row=6, column=2)

# Output text box
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=7, columnspan=3, pady=10)

# Main loop
root.mainloop()
