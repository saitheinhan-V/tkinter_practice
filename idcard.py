import tkinter as tk
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ID Card")
        self.geometry("500x300")
        self.configure(bg="#0090C9")
        self.resizable(False, False)
        self.ui()

    def ui(self):
        #school name
        self.grid_columnconfigure(0, weight=1)
        self.school_label = tk.Label(self,text="ႁူင်းႁဵၼ်း သၢႆလႅင်းမႂ်ႇ", font=("NamKhoneUnicode", 18),bg="#0090C9",fg="#FFFFFF")
        self.school_label.grid(row=0,column=0,pady=10,columnspan=3,sticky="we")

        #frame
        content_frame = tk.Frame(self, bg="#0090C9")
        content_frame.grid(row=1, column=0)

        # Center the frame horizontally
        content_frame.grid_columnconfigure(0, weight=1)
        # content_frame.grid_columnconfigure(1, weight=0)
        # content_frame.grid_columnconfigure(2, weight=0)

        self.grid_rowconfigure(1, weight=1)

        #profile image
        profile_image = Image.open("profile.png")
        resized_image = profile_image.resize((150, 150),Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)

        self.profile_label = tk.Label(content_frame, image=self.photo,relief="groove",bg="#FF0000")
        self.profile_label.grid(row=1,column=0,sticky="we",padx=10,pady=10,rowspan=3)

        #name label
        self.name_label = tk.Label(content_frame,text="ၸိုဝ်ႈ", font=("NamKhoneUnicode", 14),bg="#0090C9",fg="#FFFFFF")
        self.name_label.grid(row=1,column=1,sticky="w")

        #real name
        self.real_name_label = tk.Label(content_frame,text=": ၸၢႆးတဵင်းႁၢၼ်ႇ", font=("NamKhoneUnicode", 14),bg="#0090C9",fg="#FFFFFF")
        self.real_name_label.grid(row=1,column=2,sticky="w")

        # grade label
        self.grade_label = tk.Label(content_frame, text="ၸၼ်ႉလိၵ်ႈ", font=("NamKhoneUnicode", 14), bg="#0090C9",
                                   fg="#FFFFFF")
        self.grade_label.grid(row=2, column=1, sticky="w")

        # real grade
        self.grade_name_label = tk.Label(content_frame, text=": Grade (5)", font=("NamKhoneUnicode", 14),
                                        bg="#0090C9", fg="#FFFFFF")
        self.grade_name_label.grid(row=2, column=2, sticky="w")

        # id label
        self.id_label = tk.Label(content_frame, text="ID", font=("NamKhoneUnicode", 14), bg="#0090C9",
                                    fg="#FFFFFF")
        self.id_label.grid(row=3, column=1, sticky="w")

        # real id no
        self.id_no_label = tk.Label(content_frame, text=": NLEC-2026104", font=("NamKhoneUnicode", 14),
                                         bg="#0090C9", fg="#FFFFFF")
        self.id_no_label.grid(row=3, column=2, sticky="w")

        #footer
        self.footer_label = tk.Label(self,text="www.newlightedu.com", font=("NamKhoneUnicode", 12),bg="#D81D00",fg="#FFFFFF")
        self.footer_label.grid(row=5,column=0,sticky="we")

app = MainApp()
app.mainloop()