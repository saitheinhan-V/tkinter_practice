import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student ID Card")
        self.geometry("500x300")
        self.setup_ui()

    def setup_ui(self):
        name_label = tk.Label(self, text="ၸၢႆးတဵင်းႁၢၼ်ႇ", font=("NamKhoneUnicode", 16),fg="#98BE25",bg="#3E6DF9")
        name_label.pack(ipadx=20,ipady=20,anchor="center", expand=True)


app = MyApp()
app.mainloop()