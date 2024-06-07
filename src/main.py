import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt, decrypt
from key_management import generate_key, save_key, load_key

def encrypt_message():
    key = load_key()
    result = encrypt(entry.get(), key)
    text_var.set(result)

def decrypt_message():
    key = load_key()
    result = decrypt(entry.get(), key)
    text_var.set(result.decode())

app = tk.Tk()
app.title('AES Encryptor/Decryptor')

entry = tk.Entry(app, width=50)
entry.pack(pady=20)

text_var = tk.StringVar()
result_label = tk.Label(app, textvariable=text_var, width=50)
result_label.pack(pady=20)

encrypt_button = tk.Button(app, text='Encrypt', command=encrypt_message)
encrypt_button.pack(side=tk.LEFT, padx=(20, 10))

decrypt_button = tk.Button(app, text='Decrypt', command=decrypt_message)
decrypt_button.pack(side=tk.RIGHT, padx=(10, 20))

app.mainloop()
