import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        character_pool = ""
        if letters_var.get():
            character_pool += string.ascii_letters
        if numbers_var.get():
            character_pool += string.digits
        if symbols_var.get():
            character_pool += string.punctuation

        if not character_pool:
            raise ValueError("No character types selected")

        password = ''.join(random.choice(character_pool) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid length and select at least one character type.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setting up the GUI
root = tk.Tk()
root.title("Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, pady=5)

# Checkboxes for character types
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w")

# Generate password button
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

# Display generated password
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, pady=5)


root.mainloop()
