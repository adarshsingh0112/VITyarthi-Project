Library management system

Overview

The Library Management System is a Python-based application designed to manage books in a library. It allows users to:

View available books in the library.

Issue books to students.

Accept returned books from students, calculate fines for late returns, and update book availability.

This system uses SQLite as the database to store information about books and student transactions, making it simple to set up and use.

Features

View Available Books: Displays a list of books that are currently available in the library.

Issue Books: Allows students to issue books by entering their details and selecting a book to borrow.

Book Submission: Handles the return of books, checks the due date, and calculates a fine for late returns.

Database Interaction: The system interacts with an SQLite database to store and retrieve data related to books and student transactions.

Fine Calculation: Automatically calculates a fine (30 INR per day) if a book is returned late.


Technologies/Tools Used

Python 3.x: Programming language used for building the system.

SQLite: Database used to store the library's books and student transactions.

Datetime: Python’s datetime module is used to manage and compare dates for book issue and return.

Steps to Install & Run the Project

Install Python:
Ensure you have Python 3.x installed on your machine. If not, you can download it from Python's official website.

2. Clone or Download the Project:
Clone the repository using Git or download the source code as a .zip file.

3. Set Up the SQLite Database:
Create a SQLite database file named library.db if it doesn't already exist. Below are the steps for creating the required tables.

4. Run the Program:
Run the main Python script to start the library management system

python library_system.py


Instructions for Testing

1.	Viewing Available Books:

Run the program and choose option 1 to view the list of books currently available in the library.

Expected Output: A list of available books will be displayed.

2. Issuing a Book:

Choose option 2 to issue a book.

Enter the student’s ID, name, book name, issue date, and due date.

If the book is available, it will be issued, and the status will be updated to issued.

3. Returning a Book:

Choose option 3 to return a book.

Enter the student ID, book name, and actual return date. 

The system will calculate any fine if the return is late (30 INR per day).

4. Exiting the Program:

Choose option 4 to exit the program.



Screenshot
<img width="1044" height="757" alt="Screenshot 2025-11-23 182948" src="https://github.com/user-attachments/assets/307b14ef-eec3-48e1-ab7a-6cbfb29084ae" />


<img width="973" height="267" alt="Screenshot 2025-11-23 183001" src="https://github.com/user-attachments/assets/4c05b23e-750b-4532-8deb-89d412845de2" />
