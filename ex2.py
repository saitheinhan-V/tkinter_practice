import numpy as np
import tkinter as tk

class MyFirstApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ႁႃတူဝ်လိူၵ်ႈ")
        self.geometry("300x200")

        self.label = tk.Label(self, text="မႂ်ႇသုင်ၶႃႈ", font=("NamKhoneUnicode", 14))
        self.label.pack(pady=20)

        self.random_btn = tk.Button(self, text="Generate Random Number", command=self.generate_random_number)
        self.random_btn.pack()

    def generate_random_number(self):
        random_number = np.random.randint(1, 100)
        self.label.config(text=f"Random Number: {random_number}")

app = MyFirstApp()
app.mainloop()