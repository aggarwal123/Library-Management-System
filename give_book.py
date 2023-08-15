from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3


con = sqlite3.connect("Library.db")
cur = con.cursor()


class LendBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x260+70+50")
        self.title("Give Book")
        books = cur.execute("SELECT * FROM books WHERE book_available>0").fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + " - " + book[1])
        
        members = cur.execute("SELECT * FROM members").fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + " - " + member[1])
        
        
        ##############################    FRAMES    ###############################
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=480, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        # HEADING AND IMAGE (IN TOP FRAME)
        self.top_image = PhotoImage(file="Images/give_book_image.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=75, y=10)
        heading = Label(self.top_frame, text="  Give Book", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=150, y=12)
        
        #############################    ENTRIES AND LABELS    ############################
        
        # BOOK NAME
        self.book_name = StringVar()
        self.label_name = Label(self.bottom_frame, text="Book Name", font="Times 15 bold", background="#E9FFF8")
        self.label_name.place(x=110, y=20)
        self.combo_name = ttk.Combobox(self.bottom_frame, textvariable=self.book_name)
        self.combo_name["values"] = book_list
        self.combo_name.place(x=250, y=25)
        
        # MEMBER NAME
        self.member_name = StringVar()
        self.label_age = Label(self.bottom_frame, text="Member Name", font="Times 15 bold", background="#E9FFF8")
        self.label_age.place(x=110, y=65)
        self.combo_member = ttk.Combobox(self.bottom_frame, textvariable=self.member_name)
        self.combo_member["values"] = member_list
        self.combo_member.place(x=250, y=70)

        self.submit_button = Button(self.bottom_frame, text="S U B M I T", background="lightblue", command=self.Lend_Book)
        self.submit_button.place(x=230, y=120)
    
    def Lend_Book(self):
        book_name = self.book_name.get().split()
        member_name = self.member_name.get().split()
        book = cur.execute("SELECT * FROM books WHERE book_id = ?", (int(book_name[0]),)).fetchall()
        member = cur.execute("SELECT * FROM members WHERE member_id = ?", (int(member_name[0]),)).fetchall()
        if (book_name and member_name):
            try:
                if book[0][7]>0:
                    query = "INSERT INTO 'borrow' (borrow_book_id, borrow_member_id, borrow_book_name, borrow_member_name) VALUES (?,?,?,?)"
                    cur.execute(query, (book[0][0], member_name[0][0], book[0][1], member[0][1]))
                    con.commit()
                    messagebox.showinfo("Success", "Book has been Given", icon="info")
                    cur.execute("UPDATE books SET book_available = ? WHERE book_id = ?", (book[0][7]-1, book[0][0]))
                    con.commit()
                    self.destroy()
                else:
                    messagebox.showinfo("Failed", "No Book Available", icon="warning")
            except:
                messagebox.showerror("Error", "Failed to Give Book", icon="warning")
        else:
            messagebox.showerror("Error", "Enter All Fields", icon="warning")
