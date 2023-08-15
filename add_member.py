from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("Library.db")
cur = conn.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x435+450+70")
        self.title("Add Member")
        self.resizable(False, False)
        
        ##############################    FRAMES    ###############################
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=480, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        # HEADING AND IMAGE (IN TOP FRAME)
        self.top_image = PhotoImage(file="Images/add_member_image.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=55, y=10)
        heading = Label(self.top_frame, text="  ADD MEMBER", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=125, y=12)
        
        #############################    ENTRIES AND LABELS    ############################
        
        # NAME
        self.label_name = Label(self.bottom_frame, text="Name", font="Times 15 bold", background="#E9FFF8")
        self.label_name.place(x=110, y=20)
        self.entry_name = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_name.insert(0, "Enter Member Name")
        self.entry_name.place(x=225, y=25)
        # AGE
        self.label_age = Label(self.bottom_frame, text="Age", font="Times 15 bold", background="#E9FFF8")
        self.label_age.place(x=110, y=65)
        self.entry_age = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_age.insert(0, "Enter Age")
        self.entry_age.place(x=225, y=70)
        # gender
        self.label_gender = Label(self.bottom_frame, text="Gender", font="Times 15 bold", background="#E9FFF8")
        self.label_gender.place(x=110, y=110)
        self.entry_gender = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_gender.insert(0, "Enter Gender")
        self.entry_gender.place(x=225, y=115)
        # PHONE
        self.label_phone = Label(self.bottom_frame, text="Phone", font="Times 15 bold", background="#E9FFF8")
        self.label_phone.place(x=110, y=155)
        self.entry_phone = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_phone.insert(0, "Enter Phone Number")
        self.entry_phone.place(x=225, y=160)
        # EMAIL
        self.label_email = Label(self.bottom_frame, text="Email Id", font="Times 15 bold", background="#E9FFF8")
        self.label_email.place(x=110, y=200)
        self.entry_email = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_email.insert(0, "Enter Email Id")
        self.entry_email.place(x=225, y=205)
        # ADDRESS
        self.label_address = Label(self.bottom_frame, text="Address", font="Times 15 bold", background="#E9FFF8")
        self.label_address.place(x=110, y=245)
        self.entry_address = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_address.insert(0, "Enter Address")
        self.entry_address.place(x=225, y=250)
        # SUBMIT BUTTON
        self.submit_button = Button(self.bottom_frame, text="S U B M I T", background="lightblue", command=self.Add_Member_To_Database)
        self.submit_button.place(x=265, y=295)
    
    def Add_Member_To_Database(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if (name and age and gender and phone):
            try:
                cur.execute("INSERT INTO Members (member_name, member_age, member_gender, member_phone, member_email, member_address) VALUES (?, ?, ?, ?, ?, ?)",
                            (name, age, gender, phone, email, address))
                conn.commit()
                messagebox.showinfo("SUCCESS","Member Successfully Added in Database", icon="info")
                self.destroy()
            except:
                messagebox.showerror("ERROR","Cannot Add Member in Database", icon="warning")
        else:
            messagebox.showerror("ERROR","Enter All the Fields", icon="warning")