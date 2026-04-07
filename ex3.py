import tkinter as tk
import numpy as np

class MyFirstApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student ID Card")
        self.geometry("500x300")
        self.configure(bg="#d37f25")
        self.resizable(False, False)

        self.label = tk.Label(self, text="မႂ်ႇသုင်ၶႃႈ", font=("NamKhoneUnicode", 14))
        self.label.pack(pady=20)

        self.setup_ui()

    def setup_ui(self):
        label = tk.Label(self, text="ၼႃႈတႃ Software ႁဝ်း တင်ႈၵႃႈဝႆႉယဝ်ႉၶႃႈ!", bg="#f0f0f0")
        label.pack(pady=100)

if __name__ == "__main__":
    app = MyFirstApp()
    app.mainloop()