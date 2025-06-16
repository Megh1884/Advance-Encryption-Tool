import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_module import encrypt_file, decrypt_file

# Create the main window
root = tk.Tk()
root.title("🔐 Advanced Encryption Tool")
root.geometry("600x300")
root.configure(bg="#f4f4f4")

# File path variable
filepath = tk.StringVar()
show_key = tk.BooleanVar(value=False)

# Fonts and Colors
LABEL_FONT = ("Helvetica", 12, "bold")
ENTRY_FONT = ("Helvetica", 11)
BUTTON_FONT = ("Helvetica", 10, "bold")
BG_COLOR = "#f4f4f4"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "white"

# Functions
def select_file():
    path = filedialog.askopenfilename()
    filepath.set(path)

def encrypt_action():
    if filepath.get() and key_entry.get():
        try:
            if len(key_entry.get()) not in [16, 24, 32]:
                messagebox.showerror("Invalid Key", "Key must be 16, 24, or 32 characters long.")
                return
            encrypt_file(filepath.get(), key_entry.get())
            messagebox.showinfo("Success", "✅ File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Missing Info", "File and key are required.")

def decrypt_action():
    if filepath.get() and key_entry.get():
        try:
            if len(key_entry.get()) not in [16, 24, 32]:
                messagebox.showerror("Invalid Key", "Key must be 16, 24, or 32 characters long.")
                return
            decrypt_file(filepath.get(), key_entry.get())
            messagebox.showinfo("Success", "✅ File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Missing Info", "File and key are required.")

def toggle_key_visibility():
    if show_key.get():
        key_entry.config(show='')
    else:
        key_entry.config(show='*')

# Layout
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=20, padx=20, fill="both", expand=True)

tk.Label(frame, text="Select File:", font=LABEL_FONT, bg=BG_COLOR).grid(row=0, column=0, pady=5, sticky="w")
tk.Entry(frame, textvariable=filepath, font=ENTRY_FONT, width=45).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Browse", command=select_file, font=BUTTON_FONT, bg=BTN_COLOR, fg=BTN_TEXT_COLOR).grid(row=0, column=2)

tk.Label(frame, text="Enter Key:", font=LABEL_FONT, bg=BG_COLOR).grid(row=1, column=0, pady=10, sticky="w")
key_entry = tk.Entry(frame, show='*', font=ENTRY_FONT, width=45)
key_entry.grid(row=1, column=1, padx=10)
tk.Checkbutton(frame, text="Show Key", variable=show_key, command=toggle_key_visibility, bg=BG_COLOR).grid(row=1, column=2, sticky="w")

button_frame = tk.Frame(frame, bg=BG_COLOR)
button_frame.grid(row=2, column=0, columnspan=3, pady=20)

tk.Button(button_frame, text="🔒 Encrypt", command=encrypt_action, font=BUTTON_FONT, bg="#2196F3", fg=BTN_TEXT_COLOR, width=15).pack(side="left", padx=20)
tk.Button(button_frame, text="🔓 Decrypt", command=decrypt_action, font=BUTTON_FONT, bg="#f44336", fg=BTN_TEXT_COLOR, width=15).pack(side="left", padx=20)

# Run the app
root.mainloop()