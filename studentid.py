import tkinter as tk
from PIL import Image, ImageTk
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student ID Card")
        self.geometry("500x400")
        self.configure(bg="#0032C9")
        self.resizable(False, False)
        self.ui()

    def ui(self):
        #title
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title_label = tk.Label(self, text="ႁူင်းႁဵၼ်း သၢႆလႅင်းမႂ်ႇ", font=("NamKhoneUnicode", 20),bg="#0032C9",fg="#FFFFFF")
        self.title_label.grid(row=0,column=0,pady=5)

        #profile image
        profile_image = Image.open("images/profile.png")
        resized_image = profile_image.resize((120, 120),Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)

        image_label = tk.Label(self, image=self.photo,relief="groove")
        image_label.grid(row=1,column=0,pady=10)

        #name
        self.name_label = tk.Label(self, text="Name: ၸၢႆးတဵင်းႁၢၼ်", font=("NamKhoneUnicode", 14),bg="#0032C9",fg="#FFFFFF")
        self.name_label.grid(row=3,column=0,columnspan=3,pady=20,padx=20,sticky="w")

        #course
        self.course_label = tk.Label(self, text="Course: Basic Computer", font=("NamKhoneUnicode", 14),bg="#0032C9",fg="#FFFFFF")
        self.course_label.grid(row=4,column=0,columnspan=3,padx=20,sticky="w")

        #footer
        self.footer_label = tk.Label(self,text="www.newlightedu.com", font=("NamKhoneUnicode", 12),bg="#ECA100",fg="#FFFFFF")
        self.footer_label.grid(row=5,column=0,columnspan=3,ipady=5,sticky="we")

app = MainApp()
app.mainloop()