import tkinter as tk


class MyFirstApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grid Layout Example")
        self.geometry("400x300")
        self.configure(bg="#d37f25")
        self.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        self.label1 = tk.Label(self, text="Label 1", bg="#f0f0f0") 
        # self.label1.pack(pady=10)
        self.label1.grid(row=0,column=0,padx=10,pady=10)

        label2 = tk.Label(self, text="Label 2", bg="#f0f0f0")
        label2.grid(row=0,column=1,padx=10,pady=10)

        label3 = tk.Label(self,text="label 3",bg="#f0f0f0")
        label3.grid(row=1,column=0,padx=10,pady=10)

        label4 = tk.Label(self, text="label 4",bg="#f0f0f0")
        #sticky = n -north / s -south / w - west / e - east
        label4.grid(row=2,column=0,columnspan=2,sticky="we",padx=10,pady=10)

        footer = tk.Label(self,text="လိၵ်ႈတႆး", bg="#d37f25",font=("NamKhoneUnicode", 12))
        footer.grid(row=3,column=0,padx=10,pady=10)

app = MyFirstApp()
app.mainloop()