# Console Application Practice – Project-Level Problems

These problems are designed for beginner-to-intermediate students with basic understanding of variables, conditionals, loops, lists/maps, and functions or classes. Each problem simulates a real-world use case and should be implemented as a **menu-driven console application** with state management and user interaction.

---

## 1. Tweet App 
**Description**: Registered users can post tweets and view their own tweets. Guests cannot view tweets.
**Modules**:
- Register/Login
- Post tweet
- View own tweets
- Forgot/reset password

**Menu**:
- Guest Menu: Register, Login, Forgot Password
- User Menu: Post Tweet, View My Tweets, Reset Password, Logout

---

## 2. Library Management Console App
**Description**: A simple library system where users (students) can borrow and return books.
**Modules**:
- Register/Login
- View Available Books
- Borrow Book
- Return Book
- Forgot Password

**Menu**:
- Guest Menu: Register, Login, Forgot Password
- User Menu: View Books, Borrow Book, Return Book, Reset Password, Logout

**State Tracking**:
- Maintain list of borrowed books per user using a map
- Update availability when book is borrowed or returned

---

## 3. College Voting System
**Description**: Registered users can vote for their department representative. Each user can vote only once.
**Modules**:
- Register/Login
- Vote for candidate
- View Voting Stats
- Forgot Password

**Menu**:
- Guest Menu: Register, Login, Forgot Password
- User Menu: Vote, View Voting Results, Reset Password, Logout

**State Tracking**:
- Track who has voted using a map
- Store votes in a candidate → count map

---

## 4. Digital Expense Tracker
**Description**: Track daily expenses per user. Users can add, delete, and view their expenses.
**Modules**:
- Register/Login
- Add Expense (description, amount, date)
- View Expense History
- Forgot Password

**Menu**:
- Guest Menu: Register, Login, Forgot Password
- User Menu: Add Expense, View History, Reset Password, Logout

**State Tracking**:
- Store expenses per user in a map
- Display monthly and daily totals (optional for extra credit)

---

## 5. Student Report Card Generator
**Description**: A console app to manage student marks and generate reports. Admin can add students and marks, students can view their own reports.
**Modules**:
- Admin: Add Student, Enter Marks, View All Reports
- Student: Register/Login, View Own Report, Forgot Password

**Menu**:
- Guest Menu: Register, Login, Forgot Password
- Admin Menu: Add Student, Enter Marks, View Reports, Logout
- Student Menu: View Report, Reset Password, Logout

**State Tracking**:
- Maintain two roles (admin, student)
- Use maps to store student ID → marks and reports

---

## Implementation Guidelines
- Use console inputs and outputs
- Each menu should loop until user exits or logs out
- Use maps/dictionaries to track user data and state
- Include input validation and user-friendly messages
- Separate logic into functions or methods for better modularity

---

## Evaluation Criteria
- Correct and complete menu functionality
- Proper state tracking using data structures
- Functional separation and clean code structure
- Input validation and error handling
- Reusable and maintainable logic

---

