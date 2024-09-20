import tkinter as tk
import subprocess


def save_input():
    site_value = site.get()  # Retrieve text from the Entry widget
    username_value = username.get()
    subprocess.run(["passgen1", site_value, username_value])


root = tk.Tk()
root.title("Hello world")
root.geometry("400x400")

site = tk.Entry(root, width=30)
site.pack(pady=10)
site.insert(0, "Enter Site name")

username = tk.Entry(root, width=30)
username.pack(pady=10)
username.insert(0, "Enter Username")

button = tk.Button(root, text="Generate Password", command=save_input)
button.pack(pady=10)




root.mainloop()
