from tkinter import *
import webbrowser

class ContactUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x350+300+150")
        self.title("Contact Us")
        self.resizable(False, False)
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=705, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)

        # HEADING AND IMAGE (IN TOP FRAME)
        self.top_image = PhotoImage(file="Images/contact_us.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=90, y=10)
        heading = Label(self.top_frame, text="  CONTACT US", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=170, y=12)

        self.label_name = Label(self.bottom_frame, text="For any inquiries or support, please contact us:", font="Times 20 bold", background="#E9FFF8")
        self.label_name.place(x=45, y=20)

        self.label_name = Label(self.bottom_frame, text="Email Id :", font="Times 15 bold", background="#E9FFF8")
        self.label_name.place(x=30, y=70)
        self.email = Label(self.bottom_frame, text="TheLibraryManagementSystem@gmail.com", font="Times 15 underline", cursor="hand2", background="#E9FFF8")
        self.email.place(x=130, y=70)
        self.email.bind("<Button-1>", self.open_email)

        self.phone_label = Label(self.bottom_frame, text="Phone :", font="Times 15 bold", background="#E9FFF8")
        self.phone_label.place(x=30, y=120)
        self.phone = Label(self.bottom_frame, text="+123-456-7890", font="Times 15 underline", cursor="hand2", background="#E9FFF8")
        self.phone.place(x=130, y=120)
        self.phone.bind("<Button-1>", self.dial_phone1)
        self.phone = Label(self.bottom_frame, text="+91 - 9087654321", font="Times 15 underline", cursor="hand2", background="#E9FFF8")
        self.phone.place(x=130, y=150)
        self.phone.bind("<Button-1>", self.dial_phone2)
        
        self.phone_label = Label(self.bottom_frame, text="Website :", font="Times 15 bold", background="#E9FFF8")
        self.phone_label.place(x=30, y=200)
        self.phone = Label(self.bottom_frame, text="https://github.com/aggarwal123/Library-Management-System", font="Times 15 underline", cursor="hand2", background="#E9FFF8")
        self.phone.place(x=130, y=200)

    def open_email(self, event):
        webbrowser.open("mailto:TheLibraryManagementSystem@gmail.com")

    def dial_phone1(self, event):
        webbrowser.open("tel:+123-456-7890")
    
    def dial_phone2(self, event):
        webbrowser.open("tel:+91-9087654321")
    
    def open_website(self, event):
        webbrowser.open("https://github.com/aggarwal123/Library-Management-System")
