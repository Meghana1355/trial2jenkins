import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        messagebox.showinfo("Registration", "Registration Successful!")
    else:
        messagebox.showwarning("Error", "Please fill in all fields!")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("250x150")

# Username label and entry
tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

# Password label and entry
tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Register button
tk.Button(root, text="Register", command=register).pack(pady=10)

# Run the application
root.mainloop()
