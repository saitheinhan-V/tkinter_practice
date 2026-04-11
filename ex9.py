import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sample Dictionary")
        self.geometry("500x300")
        self.ui()

        self.mydict = {
            "fruit" : "မၢၵ်ႇ",
            "apple" : "မၢၵ်ႇၵႅမ်ႈၶွင်ႇ",
            "orange" : "မၢၵ်ႇၸွၵ်း",
            "banana" : "ၵူၺ်ႈ",
        }

    def ui(self):
        self.label = tk.Label(self,text="Enter english text here",font=("NamKhoneUnicode",16))
        self.label.pack()

        self.english_entry = tk.Entry(self,font=("NamKhoneUnicode",14),width=20)
        self.english_entry.pack(pady=20)

        self.button = tk.Button(self,text="Submit",command=self.check_word)
        self.button.pack(pady=20)

        self.result = tk.Label(self,text="",font=("NamKhoneUnicode",14))
        self.result.pack(pady=20)

    def check_word(self):
        text = self.english_entry.get().strip()
        if text == "":
            self.result.configure(text="Please enter a word")
        else:
            if text not in self.mydict.keys():
                self.result.configure(text="No such word")
            else:
                self.result.configure(text=f"{self.mydict[text]}")


app = MyApp()
app.mainloop()