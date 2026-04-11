import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sample Input")
        self.geometry("500x300")
        self.ui()

    def ui(self):
        self.label = tk.Label(self,text="Enter name here",font=("Arial", 12))
        self.label.pack()

        self.entry = tk.Entry(self,width=40,font=("Arial", 12))
        self.entry.pack()

        #button
        self.button = tk.Button(self,text="Greeting",command=self.greeting)
        self.button.pack(padx=10,pady=10)

        #result
        self.result = tk.Label(self,text="",font=("Arial", 12))
        self.result.pack()

    def greeting(self):
        self.name = self.entry.get().strip()
        if self.name == "":
            self.result.configure(text="Please enter your name")
        else:
            self.result.config(text=f"Hello... {self.name}")
            self.entry.delete(0, tk.END)

app = App()
app.mainloop()