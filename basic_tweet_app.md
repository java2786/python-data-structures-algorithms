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

## Implementation Guidelines
- Use console inputs and outputs
- Each menu should loop until user exits or logs out
- Use maps/dictionaries to track user data and state
- Include input validation and user-friendly messages
- Separate logic into functions or methods for better modularity

---