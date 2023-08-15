from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("Library.db")
cur = conn.cursor()

class BookReviews(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x350+300+150")
        self.title("Book Reviews")
        self.resizable(False, False)
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BUTTON FRAME
        self.bottom_frame = Frame(self, height=480, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        # HEADING AND IMAGE (IN TOP FRAME)
        self.top_image = PhotoImage(file="Images/book_reviews.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=60, y=10)
        heading = Label(self.top_frame, text="  BOOK REVIEWS", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=130, y=12)
        
        # BOOK ID
        self.label_id = Label(self.bottom_frame, text="Book Id", font="Times 15 bold", background="#E9FFF8")
        self.label_id.place(x=110, y=20)
        self.entry_id = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_id.insert(0, "Enter Book Id")
        self.entry_id.place(x=245, y=25)
        
        # REVIEWS
        self.label_reviews = Label(self.bottom_frame, text="Book Review", font="Times 15 bold", background="#E9FFF8")
        self.label_reviews.place(x=110, y=60)
        self.entry_reviews = Entry(self.bottom_frame, width=40, bd=2)
        self.entry_reviews.insert(0, "Enter Book Review")
        self.entry_reviews.place(x=245, y=65)
        
        # SUBMIT BUTTON
        self.submit_button = Button(self.bottom_frame, text="S U B M I T", command=self.Add_Book_To_Database, background="lightblue")
        self.submit_button.place(x=265, y=105)
        
    def Add_Book_To_Database(self):
        id = self.entry_id.get()
        reviews = self.entry_reviews.get()
        if (id and reviews):
            try:
                book_details = cur.execute("SELECT * FROM books WHERE book_id=?", (id,)).fetchone()
                feed = book_details[3]
                if feed == None:
                    feed = reviews
                else:
                    feed += f"\n{reviews}"
                cur.execute("UPDATE books SET book_reviews=? WHERE book_id=?",(feed, id))
                conn.commit()
                messagebox.showinfo("SUCCESS","Reviews Successfully Updated in Database", icon="info")
                self.destroy()
            except:
                messagebox.showerror("ERROR","Cannot Update Review in Database", icon="warning")
        else:
            messagebox.showerror("ERROR","Enter All the Fields", icon="warning")
        