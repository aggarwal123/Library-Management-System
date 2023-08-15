from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("Library.db")
cur = conn.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x400+450+70")
        self.title("Add Book")
        self.resizable(False, False)
        
        ##############################    FRAMES    ###############################
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BUTTON FRAME
        self.bottom_frame = Frame(self, height=480, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        # HEADING AND IMAGE (IN TOP FRAME)
        self.top_image = PhotoImage(file="Images/add_book_image.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=95, y=10)
        heading = Label(self.top_frame, text="  ADD BOOK", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=165, y=12)
        
        #############################    ENTRIES AND LABELS    ############################
        
        # NAME
        self.label_name = Label(self.bottom_frame, text="Name", font="Times 15 bold", background="#E9FFF8")
        self.label_name.place(x=110, y=20)
        self.entry_name = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_name.insert(0, "Enter Book Name")
        self.entry_name.place(x=245, y=25)
        # AUTHOR
        self.label_author = Label(self.bottom_frame, text="Author", font="Times 15 bold", background="#E9FFF8")
        self.label_author.place(x=110, y=65)
        self.entry_author = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_author.insert(0, "Enter Author Name")
        self.entry_author.place(x=245, y=70)
        # PAGE
        self.label_page = Label(self.bottom_frame, text="Page Size", font="Times 15 bold", background="#E9FFF8")
        self.label_page.place(x=110, y=110)
        self.entry_page = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_page.insert(0, "Enter Page Size")
        self.entry_page.place(x=245, y=115)
        # LANGUAGE
        self.label_language = Label(self.bottom_frame, text="Language", font="Times 15 bold", background="#E9FFF8")
        self.label_language.place(x=110, y=155)
        self.entry_language = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_language.insert(0, "Enter Language")
        self.entry_language.place(x=245, y=160)
        # NUMBER OF BOOKS
        self.label_number = Label(self.bottom_frame, text="No. of Books", font="Times 15 bold", background="#E9FFF8")
        self.label_number.place(x=110, y=200)
        self.entry_number = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_number.insert(0, "1")
        self.entry_number.place(x=245, y=205)
        # SUBMIT BUTTON
        self.submit_button = Button(self.bottom_frame, text="S U B M I T", command=self.Add_Book_To_Database, background="lightblue")
        self.submit_button.place(x=265, y=250)
    
    def Add_Book_To_Database(self):
        name = self.entry_name.get()
        author = self.entry_author.get()
        page = self.entry_page.get()
        language = self.entry_language.get()
        number = self.entry_number.get()
        if (name and author and page and language and number):
            try:
                cur.execute("INSERT INTO books (book_name, book_author, book_page, book_language, book_total_number, book_available) VALUES (?, ?, ?, ?, ?, ?)",
                            (name, author, page, language, number, number))
                conn.commit()
                messagebox.showinfo("SUCCESS","Book Successfully Added in Database", icon="info")
                self.destroy()
            except:
                messagebox.showerror("ERROR","Cannot Add Book in Database", icon="warning")
        else:
            messagebox.showerror("ERROR","Enter All the Fields", icon="warning")