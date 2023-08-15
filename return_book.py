from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3


con = sqlite3.connect("Library.db")
cur = con.cursor()


class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x260+70+50")
        self.title("Return Book")
        books = cur.execute("SELECT * FROM books WHERE book_available<book_total_number").fetchall()
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
        self.top_image = PhotoImage(file="Images/return_book_image.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=75, y=10)
        heading = Label(self.top_frame, text="  Return Book", font="Times 40 bold", bg="#E9FFF8")
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

        self.submit_button = Button(self.bottom_frame, text="S U B M I T", background="lightblue", command=self.Return_Book)
        self.submit_button.place(x=230, y=120)
    
    def Return_Book(self):
        book_name = self.book_name.get().split()
        member_name = self.member_name.get().split()
        if book_name and member_name:
            book = cur.execute("SELECT * FROM books WHERE book_id = ?", (int(book_name[0]),)).fetchone()
            member = cur.execute("SELECT * FROM members WHERE member_id = ?", (int(member_name[0]),)).fetchone()
            print(book)
            print(member)
            if book and member:
                try:
                    borrowed = cur.execute("SELECT * FROM borrow WHERE borrow_book_id = ? AND borrow_member_id = ?", (book[0], member[0])).fetchall()
                    if borrowed:
                        cur.execute("DELETE FROM borrow WHERE borrow_book_id = ? AND borrow_member_id = ?", (book[0], member[0]))
                        con.commit()
                        messagebox.showinfo("Success", "Book has been Returned", icon="info")
                        cur.execute("UPDATE books SET book_available = ? WHERE book_id = ?", (book[7]+1, book[0]))
                        con.commit()
                    else:
                        messagebox.showinfo("Failed", "Book or Member Not Found", icon="warning")
                    self.destroy()
                except:
                    messagebox.showerror("Error", "Failed to Return Book", icon="warning")
        else:
            messagebox.showerror("Error", "Enter All Fields", icon="warning")
