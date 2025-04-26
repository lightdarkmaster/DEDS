import tkinter as tk
from tkinter import filedialog, messagebox
import os

from encryption import encrypt_file
from decryption import decrypt_file

def save_key(key: bytes, path: str):
    with open(path, 'wb') as f:
        f.write(key)

def load_key(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()

def encrypt_ui():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    output_path = filepath + ".enc"
    key_path = filepath + ".key"

    try:
        key = encrypt_file(filepath, output_path)
        save_key(key, key_path)
        messagebox.showinfo("Success", f"File encrypted!\nEncrypted: {output_path}\nKey: {key_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_ui():
    enc_path = filedialog.askopenfilename(title="Select encrypted file")
    if not enc_path:
        return

    key_path = filedialog.askopenfilename(title="Select key file")
    if not key_path:
        return

    try:
        key = load_key(key_path)
        output_path = filedialog.asksaveasfilename(defaultextension="", title="Save decrypted file as")

        if not output_path:
            return

        decrypt_file(enc_path, output_path, key)
        messagebox.showinfo("Success", f"File decrypted!\nSaved to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# User Interface
app = tk.Tk()
app.title("File Encryptor & Decryptor")
app.geometry("500x300")  # Bigger window

title = tk.Label(app, text="DEDS", font=("Arial", 20, "bold"))
title.pack(pady=20)

encrypt_btn = tk.Button(app, text="🔒 Encrypt File", command=encrypt_ui, width=35, height=2, font=("Arial", 14))
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(app, text="🔓 Decrypt File", command=decrypt_ui, width=35, height=2, font=("Arial", 14))
decrypt_btn.pack(pady=10)

app.mainloop()
