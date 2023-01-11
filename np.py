import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text = text_widget.get("1.0", tk.END)
        file.write(text)
        file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if file:
        content = file.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", content)

root = tk.Tk()
root.title("Notepad")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(expand=True, fill=tk.BOTH)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

root.mainloop()
