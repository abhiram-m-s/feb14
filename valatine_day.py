import tkinter as tk
root = tk.Tk()
root.title("Valentine Proposal ❤️")
root.geometry("500x400")

yes_font_size = 14

def say_yes():
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="Yayyyyy ❤️🥰", font=("Arial", 24))
    label.pack(expand=True)

def grow_yes():
    global yes_font_size
    yes_font_size += 4
    yes_button.config(font=("Arial", yes_font_size))

label = tk.Label(root, text="abcdefghijk? 💖", font=("Arial", 18))
label.pack(pady=40)
yes_button = tk.Button(root, text="Yes ❤️", font=("Arial", yes_font_size), command=say_yes)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No 😢", font=("Arial", 14), command=grow_yes)
no_button.pack(pady=10)
root.mainloop()