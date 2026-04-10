import tkinter as tk
from PIL import Image, ImageTk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student ID Card")
        # self.resizable(False, False)
        self.geometry("500x300")
        self.setup_ui()

    def setup_ui(self):
        raw_image = Image.open("images/profile.png")
        resized_image = raw_image.resize((200, 200))

        self.photo = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(self, image=self.photo)
        image_label.pack(pady=20)

        name_label = tk.Label(self, text="ၸၢႆးတဵင်းႁၢၼ်ႇ", font=("NamKhoneUnicode", 16))
        name_label.pack(anchor="center", expand=True)

app = MyApp()
app.mainloop()