import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sample Button")
        self.configure(bg="#d37468")
        self.geometry("500x500")
        self.ui()

    def clicked(self):
        self.label.config(text="Button Clicked...", fg="white", bg="#d37468")

    def ui(self):
        self.label = tk.Label(self,text="Button is waiting....",font=("Times New Roman", 12),fg="white",bg="#d37468")
        self.label.pack()

        self.button = tk.Button(self,text="Click Here",fg="white",bg="#d37468",command=self.clicked)
        self.button.pack(pady=20)

app = MyApp()
app.mainloop()