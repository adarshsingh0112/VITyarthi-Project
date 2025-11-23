Problem Statement
The current manual method of managing a library system is inefficient, prone to errors, and lacks real-time tracking of book availability, issuance, and returns. Managing records of issued books, students, due dates, and fines becomes harder as the library grows. A simple automated system is needed to streamline operations and reduce manual workload.

Scope of the Project

* Develop a lightweight command-line based library management system.
* Maintain a structured database of books and student transactions using SQLite.
* Provide essential features such as viewing available books, issuing books, and returning them.
* Automate fine calculation based on late returns.
* Ensure data persistence across multiple sessions.

Target Users

* School and college librarians who need a simple system to manage book records.
* Students who interact with the book issuance and return process.
* Small libraries that require a basic digital system without complex interfaces.

High-Level Features

* **Book Availability Check:** Displays all books currently available for issue.
* **Issue Book:** Allows entry of student details, issue date, and due date while updating the book status.
* **Return Book:** Records actual return date, calculates late fines, and updates book status.
* **SQLite Database Integration:** Ensures persistent storage for books and student transaction records.
* **Interactive Menu:** Provides a simple user-friendly menu-driven interface for smooth operation.
