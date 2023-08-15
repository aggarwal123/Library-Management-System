from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3
import add_book, add_member, about_us, contact_us, book_reviews, user_guide, give_book, return_book


con = sqlite3.connect("Library.db")
cur = con.cursor()



class Main(object):
    def __init__(self, master):
        self.master = master
        
        def Display_Statistics(event):
            count_books = cur.execute("SELECT count(book_id) FROM books").fetchall()
            books_in_library = cur.execute("SELECT count(book_id) FROM books WHERE book_available>0").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM members").fetchall()
            taken_books = cur.execute("SELECT count(book_total_number) FROM books WHERE book_total_number>book_available").fetchall()
            self.label_book_count.config(text="Total Books : " + str(count_books[0][0]))
            self.label_books_in_library.config(text="Total Books in Library : " + str(books_in_library[0][0]))
            self.label_member_count.config(text="Total Members : " + str(count_members[0][0]))
            self.label_taken_count.config(text="Taken Books : " + str(taken_books[0][0]))
            Display_Books(self)
        
        def Display_Books(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count=0
            self.list_books.delete(0,END)
            for book in books:
                # print(book)
                self.list_books.insert(count, "  " + str(book[0]) + " - " + book[1])
                count+=1
            
            def Book_Info(event):
                select = self.list_books.curselection()
                if select:
                    value=str(self.list_books.get(select))
                    id = value.split("-")[0]
                    book = cur.execute("SELECT * FROM books WHERE book_id=?",(id,))
                    book_info = book.fetchall()
                    
                    self.list_details.delete(0,END)
                    self.list_details.insert(0, "  Book Name : " + book_info[0][1])
                    self.list_details.insert(1, "  Book Author : " + book_info[0][2])
                    self.list_details.insert(2, "  Total No. of Pages : " + book_info[0][4])
                    self.list_details.insert(3, "  Language of Book : " + book_info[0][5])
                    self.list_details.insert(4, "  No. of Books Borrowed : " + str(book_info[0][6]-book_info[0][7]))
                    self.list_details.insert(5, "  No. of Books Available : " + str(book_info[0][7]))
                    self.list_details.insert(6, "  No. of Books : " + str(book_info[0][6]))
                    
                    review_count = 1
                    if book_info[0][3]:
                        self.list_details.insert(7, "")
                        self.list_details.insert(8, "  Book Reviews :")
                        reviews = book_info[0][3].split("\n")
                        for review in reviews:
                            self.list_details.insert(END, f"          {review_count}.  {review}")
                            review_count += 1
                    else:
                        self.list_details.insert(7, "  Book Reviews : None")

            def Double_Click(event):
                global given_id
                value = str(self.list_books.get(self.list_books.curselection()))
                given_id = value.split()[0]
                give_book = GiveBook()

            self.list_books.bind("<<ListboxSelect>>", Book_Info)
            self.tabs.bind("<<NotebookTabChanged>>", Display_Statistics)
            self.list_books.bind("<Double-Button-1>", Double_Click)
            
        
        ################################    FRAMES    ###############################
        main_frame = Frame(self.master)
        main_frame.pack(fill=BOTH, expand=True)
        
        #############################    TOP FRAME    ################################
        top_frame = Frame(main_frame, width=1050, height=70, bg="#E0F0F0", padx=10, relief=SUNKEN, borderwidth=2)
        top_frame.pack(side=TOP, fill=X)
        
        #############################    CENTER FRAME    ################################
        center_frame = Frame(main_frame, width=1050, height=515, relief=RIDGE, bg="#E0F0F0")
        center_frame.pack(side=TOP, fill=BOTH, expand=True)

        
        #############################   CENTER LEFT FRAME   #################################
        center_left_frame = Frame(center_frame, width=650, height=540, relief=SUNKEN, borderwidth=2, background="#DEF9FF")
        center_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        #############################   CENTER RIGHT FRAME   ##################################
        center_right_frame = Frame(center_frame, width=400, height=540, relief=SUNKEN, borderwidth=2, background="#DEF9FF")
        center_right_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        
        #############################   SEARCH BAR (CENTER RIGHT FRAME)   ############################
        search_bar = LabelFrame(center_right_frame, width=400, height=45, text="Search Box",
                                background="#85E0FC")
        search_bar.pack(fill=BOTH)
        # CREATING A SEARCH BAR
        self.label_search = Label(search_bar, text="Search : ", font="Arial 12 bold", background="#85E0FC",
                                  fg="black")
        self.label_search.grid(row=0, column=0, padx=10, pady=10)
        self.entry_search = Entry(search_bar, width=30, bd=3)
        self.entry_search.grid(row=0, column=1, columnspan=3, pady=10)
        # ADDING A BUTTON FOR SEARCH
        self.BookSearch = PhotoImage(file="Images/search.png")
        self.BookSearchButton = Button(search_bar, image=self.BookSearch, command=self.SearchBook)
        self.BookSearchButton.grid(row=0, column=4, pady=10, padx=10)
        
        
        ############################    LIST BAR (CENTER RIGHT FRAME)   ###############################
        list_bar = LabelFrame(center_right_frame, width=400, height=485, text="List Box", background="#85E0FC")
        list_bar.pack(fill=BOTH)
        label_list = Label(list_bar, text="Sort By", font="times 16 bold", fg="black", bg="#85E0FC")
        label_list.grid(row=0, column=1, columnspan=2)
        # CREATING RADIO BUTTONS
        self.ListChoice = IntVar()
        radio_button1 = Radiobutton(list_bar, text="All Books", var=self.ListChoice, value=1,
                                    bg="#85E0FC").grid(row=1, column=0)
        radio_button2 = Radiobutton(list_bar, text="In Library", var=self.ListChoice, value=2,
                                    bg="#85E0FC").grid(row=1, column=1)
        radio_button3 = Radiobutton(list_bar, text="Borrowed Books", var=self.ListChoice, value=3,
                                    bg="#85E0FC").grid(row=1, column=2)
        button_list = Button(list_bar, text="Books List", bg="#E9FFF8", font="arial 12", command=self.Books_List)
        button_list.grid(row=1, column=3, padx=10, pady=10)
        
        
        #########################   TITLE AND IMAGE (CENTER RIGHT FRAME)    ###########################
        image_bar = Frame(center_right_frame, width=400, height=80, background="pink")
        image_bar.pack(fill=BOTH)
        self.TitleRight = Label(image_bar, text="WELCOME TO THE LIBRARY", font="arial 12 bold",
                                pady=5,  background="pink")
        self.TitleRight.grid(row=0)
        self.LibraryImage = PhotoImage(file="Images/library.png")
        self.LabelImage = Label(image_bar, image=self.LibraryImage)
        self.LabelImage.grid(row=1, padx=30, pady=7)
        
        
        ################################   TOOL BAR (TOP FRAME)    ####################################
        
        # ADD BOOK BUTTON (TOP FRAME)
        self.IconBook = PhotoImage(file="Images/add_book.png")
        self.ButtonBook = Button(top_frame, text="   Add Book  ", image=self.IconBook, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.Add_Book)
        self.ButtonBook.pack(side=LEFT, padx=5, pady=5)
        
        # ADD MEMBER BUTTON (TOP FRAME)
        self.IconMember = PhotoImage(file="Images/add_member.png")
        self.ButtonMember = Button(top_frame, text="   Add Member  ", image=self.IconMember, compound=LEFT,
                                   font="Arial 9 bold", background="#E9FFF8", command=self.Add_Member)
        self.ButtonMember.pack(side=LEFT, padx=5, pady=5)
        
        # GIVE BOOK (TOP FRAME)
        self.IconGive = PhotoImage(file="Images/give_book.png")
        self.ButtonGive = Button(top_frame, text="   Give Book  ", image=self.IconGive, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.Give_Book)
        self.ButtonGive.pack(side=LEFT, padx=5, pady=5)
        
        # RETURN BOOK (TOP FRAME)
        self.IconReturn = PhotoImage(file="Images/return_book.png")
        self.ButtonReturn = Button(top_frame, text="   Return Book  ", image=self.IconReturn, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.Return_Book)
        self.ButtonReturn.pack(side=LEFT, padx=5, pady=5)
        
        # BOOK REVIEWS (TOP FRAME)
        self.IconReview = PhotoImage(file="Images/review_book.png")
        self.ButtonReview = Button(top_frame, text="   Book Review  ", image=self.IconReview, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.Book_Reviews)
        self.ButtonReview.pack(side=LEFT, padx=5, pady=5)
        
        # ABOUT US (TOP FRAME)
        self.IconAbout = PhotoImage(file="Images/about.png")
        self.ButtonAbout = Button(top_frame, text="   About Us  ", image=self.IconAbout, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.About_Us)
        self.ButtonAbout.pack(side=LEFT, padx=5, pady=5)
        
        # CONTACT (TOP FRAME)
        self.IconContact = PhotoImage(file="Images/contact.png")
        self.ButtonContact = Button(top_frame, text="   Contact Us  ", image=self.IconContact, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.Contact_Us)
        self.ButtonContact.pack(side=LEFT, padx=5, pady=5)
        
        # USER GUIDE (TOP FRAME)
        self.IconUserGuide = PhotoImage(file="Images/user_guide.png")
        self.ButtonUserGuide = Button(top_frame, text="  User Guide  ", image=self.IconUserGuide, compound=LEFT,
                                 font="Arial 9 bold", background="#E9FFF8", command=self.User_Guide)
        self.ButtonUserGuide.pack(side=LEFT, padx=5, pady=5)
        
        
        ##############################   TABS (CENTER LEFT FRAME)   ############################
        self.tabs = ttk.Notebook(center_left_frame, width=650, height=550)
        self.tabs.pack()
        self.icon1 = PhotoImage(file="Images/library_management.png")
        self.icon2 = PhotoImage(file="Images/statistics.png")
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text=" Library Management       ", image=self.icon1, compound=LEFT)
        self.tabs.add(self.tab2, text=" Statistics       ", image=self.icon2, compound=LEFT)
        
        ##########################    TAB1 (LIBRARY MANAGEMENT)   ###########################
        # BOOKS LIST
        self.list_books = Listbox(self.tab1, width=30, height=23, bd=5, font="times 12 bold")
        self.scroll_bar = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(5,0), pady=5, sticky=N)
        self.scroll_bar.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.grid(row=0, column=0, sticky=N+S+E)
        # LIST DETAILS
        self.list_details = Listbox(self.tab1, width=47, height=23, bd=5, font="times 12 bold")
        self.list_details.grid(row=0, column=1, padx=(3,0), pady=5, sticky=N)
        
        ##############################    TAB2 (STATISTICS)    ###############################
        self.label_book_count = Label(self.tab2, text="label_book_count", pady=20, font="times 12 bold")
        self.label_book_count.grid(row=0, sticky=W)
        self.label_books_in_library = Label(self.tab2, text="label_books_in_library", pady=20, font="times 12 bold")
        self.label_books_in_library.grid(row=1, sticky=W)
        self.label_member_count = Label(self.tab2, text="label_member_count", pady=20, font="times 12 bold")
        self.label_member_count.grid(row=2, sticky=W)
        self.label_taken_count = Label(self.tab2, text="label_taken_count", pady=20, font="times 12 bold")
        self.label_taken_count.grid(row=3, sticky=W)
        
        Display_Books(self)
        Display_Statistics(self)
    
    
    def Add_Book(self):
        add_book.AddBook()
    
    def Add_Member(self):
        add_member.AddMember()
    
    def About_Us(self):
        about_us.AboutUs()
    
    def User_Guide(self):
        user_guide.UserGuide()
    
    def Contact_Us(self):
        contact_us.ContactUs()
    
    def Book_Reviews(self):
        book_reviews.BookReviews()
    
    def Give_Book(self):
        give_book.LendBook()
    
    def Return_Book(self):
        return_book.ReturnBook()

    def SearchBook(self):
        value = self.entry_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ("%"+value+"%",)).fetchall()
        self.list_books.delete(0,END)
        count = 0
        for book in search:
            self.list_books.insert(count, "  " + str(book[0]) + " - " + book[1])
            count+=1
    
    def Books_List(self):
        value = self.ListChoice.get()
        if value == 1:
            all_books = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in all_books:
                self.list_books.insert(count, "  " + str(book[0]) + " - " + book[1])
                count+=1
        
        elif value ==2:
            books_in_library = cur.execute("SELECT * FROM BOOKS WHERE book_available > 0").fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in books_in_library:
                self.list_books.insert(count,"  " + str(book[0]) + " - " + book[1])
                count+=1
        
        else:
            borrowed_books = cur.execute("SELECT * FROM BOOKS WHERE book_available < book_total_number").fetchall()
            self.list_books.delete(0,END)
            count = 0
            for book in borrowed_books:
                self.list_books.insert(count, "  " + str(book[0]) + " - " + book[1])
                count+=1


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x260+70+50")
        self.title("Give Book")
        global given_id
        self.book_id = int(given_id)
        books = cur.execute("SELECT * FROM books").fetchall()
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
        self.combo_name.current(self.book_id - 1)
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
                    messagebox.showinfo("Success", "Successfully Added to Database", icon="info")
                    cur.execute("UPDATE books SET book_available = ? WHERE book_id = ?", (book[0][7]-1, book[0][0]))
                    con.commit()
                    self.destroy()
                else:
                    messagebox.showinfo("Failed", "No Book Available", icon="warning")
            except:
                messagebox.showerror("Error", "Cannot Enter into Database", icon="warning")
        else:
            messagebox.showerror("Error", "Enter All Fields", icon="warning")


def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1050x585+150+85")
    image_icon = PhotoImage(file = "Images/icon.png")
    root.iconphoto(False, image_icon)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()