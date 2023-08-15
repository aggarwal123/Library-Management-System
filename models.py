import sqlite3

# CREATING/CONNECTING TO DATABASE
conn = sqlite3.connect("Library.db")
cur = conn.cursor()

#####################   TABLE - BOOKS   ####################
cur.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT NOT NULL,
        book_author TEXT NOT NULL,
        book_reviews TEXT,
        book_page TEXT NOT NULL,
        book_language TEXT NOT NULL,
        book_total_number INTEGER,
        book_available INTEGER
    )
''')

##########################    TABLE - MEMBERS    ########################
cur.execute('''
    CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_name TEXT NOT NULL,
        member_age INTEGER,
        member_gender TEXT NOT NULL,
        member_phone TEXT NOT NULL,
        member_email TEXT NOT NULL,
        member_books_issued TEXT,
        member_address TEXT NOT NULL
    )
''')


##########################    TABLE - BORROW    ########################
cur.execute('''
    CREATE TABLE IF NOT EXISTS borrow (
        borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        borrow_book_id INTEGER,
        borrow_member_id INTEGER,
        borrow_book_name TEXT NOT NULL,
        borrow_member_name TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
