from tkinter import *
from tkinter import font

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x635+150+20")
        self.title("About Us")
        self.resizable(False, False)
        
        ##############################    FRAMES    ###############################
        
        # TOP FRAME
        self.top_frame = Frame(self, height=90, background="#E9FFF8")
        self.top_frame.pack(fill=X)
        
        # BOTTOM FRAME
        self.bottom_frame = Frame(self, height=705, background="#E9FFF8")
        self.bottom_frame.pack(fill=X)
        
        ######################     HEADING AND IMAGE (IN TOP FRAME)     #########################
        self.top_image = PhotoImage(file="Images/about_image.png")
        top_image_label = Label(self.top_frame, image=self.top_image, bg="#E9FFF8")
        top_image_label.place(x=195, y=10)
        heading = Label(self.top_frame, text="  ABOUT US", font="Times 40 bold", bg="#E9FFF8")
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
        welcome_text = "WELCOME TO LIBRARY MANAGEMENT SYSTEM!"
        welcome_label = Label(canvas, text=welcome_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(55, 10, anchor=NW, window=welcome_label)
        
        # ABOUT 1 TEXT
        about1_text = '''Our platform is designed to provide seamless and efficient management of your library's resources, helping you organize, track, and facilitate the borrowing and return of books. Whether you're a librarian or a library enthusiast, our user-friendly interface and comprehensive features make library management a breeze.
        '''
        about1_label = Label(canvas, text=about1_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 50, anchor=NW, window=about1_label)
        
        # OUR VISION TEXT
        vision_text = "Our Vision :"
        vision_label = Label(canvas, text=vision_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 170, anchor=NW, window=vision_label)
        
        # OUR VISION DETAILS TEXT
        vision_details_text = '''At the heart of our project lies a commitment to promoting knowledge, learning, and exploration. We aim to empower libraries of all sizes and types, from public and school libraries to private collections, to streamline their operations and enhance the user experience. Our vision is to create a digital ecosystem that fosters a love for reading and makes access to books easier and more engaging.
        '''
        vision_details_label = Label(canvas, text=vision_details_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 210, anchor=NW, window=vision_details_label)
        
        # KEY FEATURES TEXT
        key_feature_text = "Key Features :"
        vision_label = Label(canvas, text=key_feature_text, font="Times 20 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(275, 350, anchor=NW, window=vision_label)
        
        # 1. KEY FEATURES TEXT
        key_feature_text = "1. User-Friendly Interface: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 390, anchor=NW, window=vision_label)
        # 1. KEY FEATURES DETAILS TEXT
        key_feature_text = "We understand that efficient management requires a simple and intuitive interface. Our design focuses on providing easy navigation and quick access to essential library functions."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=550,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(242, 390, anchor=NW, window=vision_label)
        
        # 2. KEY FEATURES TEXT
        key_feature_text = "2. Member Management : "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 470, anchor=NW, window=vision_label)
        # 2. KEY FEATURES DETAILS TEXT
        key_feature_text = "Managing library members is essential. You can easily add new members, maintain their profiles, and keep track of thethey have borrowed."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=550,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 470, anchor=NW, window=vision_label)
        
        # 3. KEY FEATURES TEXT
        key_feature_text = "3. Borrow / Return Books: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 550, anchor=NW, window=vision_label)
        # 3. KEY FEATURES DETAILS TEXT
        key_feature_text = "Facilitate the borrowing and return of books with just a few clicks. Members can check out books, and the system will keep track of book availability."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=550,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 550, anchor=NW, window=vision_label)
        
        # 4. KEY FEATURES TEXT
        key_feature_text = "4. Search and Sorting: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 630, anchor=NW, window=vision_label)
        # 4. KEY FEATURES DETAILS TEXT
        key_feature_text = "Our search and sorting functionalities help users find books quickly. Whether they're looking for borrowed books, books that are available, and list of all books, the system makes the search process efficient."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=550,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 630, anchor=NW, window=vision_label)
        
        # 5. KEY FEATURES TEXT
        key_feature_text = "5. Statistics and Insights: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 733, anchor=NW, window=vision_label)
        # 5. KEY FEATURES DETAILS TEXT
        key_feature_text = "Gain valuable insights into your library's performance through our comprehensive statistics. Track the number of books available, borrowed books, and the number of active members."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=550,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 733, anchor=NW, window=vision_label)
        
        # 6. KEY FEATURES TEXT
        key_feature_text = "6. User Engagement: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 815, anchor=NW, window=vision_label)
        # 6. KEY FEATURES DETAILS TEXT
        key_feature_text = "Encourage reader engagement by allowing members to provide feedback of books they've read. These reviews can help other members discover new and exciting titles."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=540,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 815, anchor=NW, window=vision_label)
        
        # 7. KEY FEATURES TEXT
        key_feature_text = "7. Dedicated Support: "
        vision_label = Label(canvas, text=key_feature_text, font="Times 15 bold", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 895, anchor=NW, window=vision_label)
        # 7. KEY FEATURES DETAILS TEXT
        key_feature_text = "We're dedicated to ensuring your experience with our platform is smooth and hassle-free. Our support team is ready to assist you with any questions or concerns you may have."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=540,
                        bg="#E9FFF8", justify="left")
        canvas.create_window(240, 895, anchor=NW, window=vision_label)
        
        # CONCLUSION TEXT
        key_feature_text = "Whether you're a modern digital library or a traditional brick-and-mortar institution, our Library Management System adapts to your needs. Join us on this journey to enhance the way libraries are managed, and together, we'll create a world where knowledge knows no bounds."
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 985, anchor=NW, window=vision_label)
        
        # THANK YOU TEXT
        key_feature_text = "Thank you for choosing the Library Management System!"
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1075, anchor=NW, window=vision_label)
        
        # SINCERELY TEXT
        key_feature_text = "Sincerely,"
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1105, anchor=NW, window=vision_label)
        
        # REGARDS
        key_feature_text = "The Library Management System Team"
        vision_label = Label(canvas, text=key_feature_text, font="Times 15", wraplength=775,
                        bg="#E9FFF8", justify="left", padx=10)
        canvas.create_window(0, 1135, anchor=NW, window=vision_label)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=self.scrollbar.set)