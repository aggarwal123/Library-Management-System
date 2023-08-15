from tkinter import *
from tkinter import font

class UserGuide(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x635+150+20")
        self.title("User Guide")
        self.resizable(False, False)
        
        ##############################    FRAMES    ###############################
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=705, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        ######################     HEADING AND IMAGE (IN TOP FRAME)     #########################
        self.top_image = PhotoImage(file="Images/manual.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=195, y=10)
        heading = Label(self.top_frame, text="  USER GUIDE", font="Times 40 bold", bg="#E9FFF8")
        heading.place(x=265, y=12)
        
        #########################     VERTICLE SCROLL BAR     #######################
        self.scrollbar = Scrollbar(self.bottom_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        ###########################     CANVAS     #########################
        canvas = Canvas(self.bottom_frame, background="#E9FFF8", height=535)
        canvas.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=canvas.yview)
        self.content_frame = Frame(canvas, background="#E9FFF8")
        
        # WELCOME TEXT
        welcome_text = "LIBRARY MANAGEMENT SYSTEM USER GUIDE"
        welcome_label = Label(canvas, text=welcome_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(70, 10, anchor=NW, window=welcome_label)
        
        # ABOUT 1 TEXT
        about1_text = "Welcome to the Library Management System! This user guide will help you understand and navigate through the various features of the system."
        about1_label = Label(canvas, text=about1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(22, 50, anchor=NW, window=about1_label)
        
        # CONTENT TEXT
        content_text = "CONTENT"
        content_label = Label(canvas, text=content_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 130, anchor=NW, window=content_label)
        
        # 1st POINT OF CONTENT
        content1_text = "1.  Getting Started - "
        content1_label = Label(canvas, text=content1_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 180, anchor=NW, window=content1_label)
        
        content11_text = "~  Installation"
        content11_label = Label(canvas, text=content11_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 210, anchor=NW, window=content11_label)
        
        content12_text = "~  Launching the Application"
        content12_label = Label(canvas, text=content12_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 240, anchor=NW, window=content12_label)
        
        # 2nd POINT OF CONTENT
        content2_text = "2.  Main Interface - "
        content2_label = Label(canvas, text=content2_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 280, anchor=NW, window=content2_label)
        
        content21_text = "~  Top Frame"
        content21_label = Label(canvas, text=content21_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 310, anchor=NW, window=content21_label)
        
        content22_text = "~  Center Left Frame"
        content22_label = Label(canvas, text=content22_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 340, anchor=NW, window=content22_label)
        
        content23_text = "~  Center Right Frame"
        content23_label = Label(canvas, text=content23_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 370, anchor=NW, window=content23_label)
        
        # 3rd POINT OF CONTENT
        content3_text = "3.  Library Management - "
        content3_label = Label(canvas, text=content3_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 410, anchor=NW, window=content3_label)
        
        content31_text = "~  Adding a Book"
        content31_label = Label(canvas, text=content31_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 440, anchor=NW, window=content31_label)
        
        content32_text = "~  Adding a Member"
        content32_label = Label(canvas, text=content32_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 470, anchor=NW, window=content32_label)
        
        content33_text = "~  Borrowing and Returning Books"
        content33_label = Label(canvas, text=content33_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 500, anchor=NW, window=content33_label)
        
        # 4th POINT OF CONTENT
        content2_text = "4.  About Us - "
        content2_label = Label(canvas, text=content2_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 540, anchor=NW, window=content2_label)
        
        content21_text = "~  Learn about the Library Management System team"
        content21_label = Label(canvas, text=content21_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 570, anchor=NW, window=content21_label)
        
        
        
        # GETTING STARTED
        getting_started1_text = "1.  Getting Started"
        getting_started1_label = Label(canvas, text=getting_started1_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 640, anchor=NW, window=getting_started1_label)
        
        # GETTING STARTED CONTENT (INSTALLATION)
        getting_started_1a_text = "a.  Installation - "
        getting_started_1a_label = Label(canvas, text=getting_started_1a_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 680, anchor=NW, window=getting_started_1a_label)
        
        getting_started_1a1_text = "~  Ensure you have Python installed on your system."
        getting_started_1a1_label = Label(canvas, text=getting_started_1a1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 710, anchor=NW, window=getting_started_1a1_label)
        
        getting_started_1a2_text = '~  Download the "Library.db" database file.'
        getting_started_1a2_label = Label(canvas, text=getting_started_1a2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 740, anchor=NW, window=getting_started_1a2_label)
        
        getting_started_1a3_text = '~  Download the required image files (e.g., "search.png", etc.).'
        getting_started_1a3_label = Label(canvas, text=getting_started_1a3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 770, anchor=NW, window=getting_started_1a3_label)
        
        getting_started_1a3_text = '~  Install the necessary packages using the command: "pip install tk".'
        getting_started_1a3_label = Label(canvas, text=getting_started_1a3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 800, anchor=NW, window=getting_started_1a3_label)
        
        # GETTING STARTED CONTENT (LAUNCHING THE APPLICATION)
        getting_started_1b_text = "b.  Launching the Application - "
        getting_started_1b_label = Label(canvas, text=getting_started_1b_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 840, anchor=NW, window=getting_started_1b_label)
        
        getting_started_1b1_text = "~  Open a terminal or command prompt."
        getting_started_1b1_label = Label(canvas, text=getting_started_1b1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 870, anchor=NW, window=getting_started_1b1_label)
        
        getting_started_1b2_text = '~  Navigate to the directory containing the code files and the database file.'
        getting_started_1b2_label = Label(canvas, text=getting_started_1b2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 900, anchor=NW, window=getting_started_1b2_label)
        
        getting_started_1b3_text = '~  Run the command: "python main.py".'
        getting_started_1b3_label = Label(canvas, text=getting_started_1b3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 930, anchor=NW, window=getting_started_1b3_label)
        
        getting_started_1b4_text = '~  The Library Management System application window will appear.'
        getting_started_1b4_label = Label(canvas, text=getting_started_1b4_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 960, anchor=NW, window=getting_started_1b4_label)
        
        
        # MAIN INTERFACE
        main_interface2_text = "2.  Main Interface"
        main_interface2_label = Label(canvas, text=main_interface2_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1030, anchor=NW, window=main_interface2_label)
        
        # MAIN INTERFACE (TOP FRAME)
        main_interface_2a_text = "a.  Top Frame - "
        main_interface_2a_label = Label(canvas, text=main_interface_2a_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1070, anchor=NW, window=main_interface_2a_label)
        
        main_interface_2a1_text = '~  "Add Book": Add a new book to the library.'
        main_interface_2a1_label = Label(canvas, text=main_interface_2a1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1100, anchor=NW, window=main_interface_2a1_label)
        
        main_interface_2a2_text = '~  "Add Member": Add a new member to the library.'
        main_interface_2a2_label = Label(canvas, text=main_interface_2a2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1130, anchor=NW, window=main_interface_2a2_label)
        
        main_interface_2a3_text = '~  "About Us": Learn more about the Library Management System.'
        main_interface_2a3_label = Label(canvas, text=main_interface_2a3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1160, anchor=NW, window=main_interface_2a3_label)
        
        main_interface_2a4_text = '~  Other buttons for functions like giving books, returning books, etc.'
        main_interface_2a4_label = Label(canvas, text=main_interface_2a4_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1190, anchor=NW, window=main_interface_2a4_label)
        
        # MAIN INTERFACE (CENTER LEFT FRAME)
        getting_started_2b_text = "b.  Center Left Frame - "
        getting_started_2b_label = Label(canvas, text=getting_started_2b_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1230, anchor=NW, window=getting_started_2b_label)
        
        getting_started_2b1_text = '~  "Library Management": Manage the book collection and member info.'
        getting_started_2b1_label = Label(canvas, text=getting_started_2b1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1260, anchor=NW, window=getting_started_2b1_label)
        
        getting_started_2b2_text = '~  "Statistics": View statistics related to the library books and members.'
        getting_started_2b2_label = Label(canvas, text=getting_started_2b2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1290, anchor=NW, window=getting_started_2b2_label)
        
        # MAIN INTERFACE (CENTER RIGHT FRAME)
        main_interface_2a_text = "c.  Center Right Frame - "
        main_interface_2a_label = Label(canvas, text=main_interface_2a_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1330, anchor=NW, window=main_interface_2a_label)
        
        main_interface_2a1_text = '~  The right side displays a search bar to search for books.'
        main_interface_2a1_label = Label(canvas, text=main_interface_2a1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1360, anchor=NW, window=main_interface_2a1_label)
        
        main_interface_2a2_text = '~  The list box displays books based on the selected filter.'
        main_interface_2a2_label = Label(canvas, text=main_interface_2a2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1390, anchor=NW, window=main_interface_2a2_label)
        
        main_interface_2a3_text = '~  Book details and information are displayed on the list details box.'
        main_interface_2a3_label = Label(canvas, text=main_interface_2a3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1420, anchor=NW, window=main_interface_2a3_label)
        
        main_interface_2a4_text = '~  The title and image section welcome users to the library.'
        main_interface_2a4_label = Label(canvas, text=main_interface_2a4_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1450, anchor=NW, window=main_interface_2a4_label)
        
        
        
        
        
        # LIBRARY MANAGEMENT
        library_management3_text = "3.  Library Management"
        library_management3_label = Label(canvas, text=library_management3_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1520, anchor=NW, window=library_management3_label)
        
        # LIBRARY MANAGEMENT (Adding a Book)
        library_management_3a_text = "a.  Adding a Book - "
        library_management_3a_label = Label(canvas, text=library_management_3a_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1560, anchor=NW, window=library_management_3a_label)
        
        library_management_3a1_text = '~  Click the "Add Book" button in the top frame.'
        library_management_3a1_label = Label(canvas, text=library_management_3a1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1590, anchor=NW, window=library_management_3a1_label)
        
        library_management_3a2_text = '~  A new window will appear for adding book details.'
        library_management_3a2_label = Label(canvas, text=library_management_3a2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1620, anchor=NW, window=library_management_3a2_label)
        
        library_management_3a3_text = '~  Fill in all the required book information such as title, author, etc.'
        library_management_3a3_label = Label(canvas, text=library_management_3a3_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1650, anchor=NW, window=library_management_3a3_label)
        
        library_management_3a4_text = '~  Click the "Add Book" button to add the book to the library.'
        library_management_3a4_label = Label(canvas, text=library_management_3a4_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1680, anchor=NW, window=library_management_3a4_label)
        
        # LIBRARY MANAGEMENT (Adding a Member)
        library_management_3b_text = "b.  Adding a Member - "
        library_management_3b_label = Label(canvas, text=library_management_3b_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1720, anchor=NW, window=library_management_3b_label)
        
        library_management_3b1_text = '~  Click the "Add Member" button in the top frame.'
        library_management_3b1_label = Label(canvas, text=library_management_3b1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1750, anchor=NW, window=library_management_3b1_label)
        
        library_management_3b2_text = '~  Enter the member details, including name, age, etc.'
        library_management_3b2_label = Label(canvas, text=library_management_3b2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1780, anchor=NW, window=library_management_3b2_label)
        
        library_management_3b2_text = '~  Click the "Add Member" button to add the member to the library.'
        library_management_3b2_label = Label(canvas, text=library_management_3b2_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1810, anchor=NW, window=library_management_3b2_label)
        
        # LIBRARY MANAGEMENT (Borrowing and Returning Books)
        library_management_3a_text = "c.  Borrowing and Returning Books - "
        library_management_3a_label = Label(canvas, text=library_management_3a_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1850, anchor=NW, window=library_management_3a_label)
        
        library_management_3a1_text = '~  These functions allow library staff to facilitate the borrowing and returning of books by members. These functions are not covered in this guide.'
        library_management_3a1_label = Label(canvas, text=library_management_3a1_text, font="Times 15", wraplength=620,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(150, 1880, anchor=NW, window=library_management_3a1_label)
        
        
        # ABOUT US
        about_us_text = "4.  About Us"
        about_us_label = Label(canvas, text=about_us_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1950, anchor=NW, window=about_us_label)
        
        about_us_text_text = '~  Click the "About Us" button in the top frame to learn more about the Library Management System team and project.'
        about_us_text_label = Label(canvas, text=about_us_text_text, font="Times 15", wraplength=750,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1990, anchor=NW, window=about_us_text_label)
        

        # CONCLUSION
        conclusion_text = '''Congratulations! You've successfully navigated through the Library Management System user guide. Feel free to explore the different features and functionalities to efficiently manage your library's resources. If you have any questions or need assistance, please refer to the "Contact Us" section or reach out to our dedicated support team.'''
        conclusion_label = Label(canvas, text=conclusion_text, font="Times 15", wraplength=750,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 2080, anchor=NW, window=conclusion_label)
        
        # THANK YOU TEXT
        key_feature_text = "Thank you for choosing the Library Management System!"
        content_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 2200, anchor=NW, window=content_label)
        
        # SINCERELY TEXT
        key_feature_text = "Sincerely,"
        content_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 2240, anchor=NW, window=content_label)
        
        # REGARDS
        key_feature_text = "The Library Management System Team"
        content_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 2265, anchor=NW, window=content_label)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=self.scrollbar.set)