import sqlite3
from datetime import datetime

def show_available_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT book_name FROM books WHERE status='available'")
    books = c.fetchall()
    print("\nAvailable Books:")
    for book in books:
        print(book[0])
    conn.close()

def issue_book():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    book_name = input("Enter Book Name to Issue: ")
    date_of_issue = input("Enter Date of Issue (YYYY-MM-DD): ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")

    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT status FROM books WHERE book_name=?",(book_name,))
    result = c.fetchone()
    if result and result[0] == 'available':
        c.execute("INSERT INTO students (student_id, name, book_name, date_of_issue, date_of_return) VALUES (?, ?, ?, ?, ?)",
                  (student_id, name, book_name, date_of_issue, due_date))
        c.execute("UPDATE books SET status='issued' WHERE book_name=?",(book_name,))
        print("Book issued successfully!")
    else:
        print("Book not available!")
    conn.commit()
    conn.close()

def submit_book():
    student_id = int(input("Enter Student ID: "))
    book_name = input("Enter Book Name: ")
    actual_return = input("Enter Actual Return Date (YYYY-MM-DD): ")
    
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT date_of_return FROM students WHERE student_id=? AND book_name=?",(student_id, book_name))
    due_date = c.fetchone()
    if due_date:
        due_dt = datetime.strptime(due_date[0], '%Y-%m-%d')
        actual_dt = datetime.strptime(actual_return, '%Y-%m-%d')
        days_late = (actual_dt - due_dt).days
        fine = 30 * max(0, days_late)
        c.execute("UPDATE students SET date_of_return=? WHERE student_id=? AND book_name=?",(actual_return, student_id, book_name))
        c.execute("UPDATE books SET status='available' WHERE book_name=?",(book_name,))
        print(f"Book returned. Fine: {fine} INR" if fine else "Book returned on time. No fine.")
    else:
        print("No such record found!")
    conn.commit()
    conn.close()

while True:
    print("\nPress 1 for Available Books\nPress 2 for Issue Book\nPress 3 for Submission\nPress 4 to Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        show_available_books()
    elif choice == '2':
        issue_book()
    elif choice == '3':
        submit_book()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid input! Please try again.")
