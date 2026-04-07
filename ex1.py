import tkinter as tk
from numpy import random

def say_hello():
    label.config(text="Hello, Sai Thein Han 👋")

def generate_random_number():
    random_number = random.randint(1, 100)
    label.config(text=f"Random Number: {random_number}")

app = tk.Tk()
app.title("My First App")
app.geometry("300x200")

label = tk.Label(app, text="Welcome!", font=("Arial", 14))
label.pack(pady=20)

# btn = tk.Button(app, text="Click Me", command=say_hello)
# btn.pack()

random_btn = tk.Button(app, text="Generate Random Number", command=generate_random_number)
random_btn.pack()

app.mainloop()