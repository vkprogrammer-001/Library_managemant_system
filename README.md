# Library Management System

The **Library Management System** is a Python project that demonstrates the integration of MySQL with Python. It allows users to manage a library's book collection by performing various operations. Here's how you can set it up and run it:

## Features

- **Add Book**: Add new books to the library.
- **Issue Book**: Issue a book to a user.
- **Submit Book**: Return a book to the library.
- **Display Books**: View the list of available books.
- **Delete Book**: Remove a book from the system.

## Prerequisites

Before running the project, ensure you have the following software installed:

- **Python**: Make sure you have Python installed on your system.
- **MySQL**: Set up a MySQL database with a username and password.

## Installation

1. **Clone the Repository**:
   - Clone the project repository using the following command:
     ```
     git clone https://github.com/<user_name>/Library_management_system.git
     ```
   - Replace `<user_name>` with your actual GitHub username.

2. **Navigate to the Project Directory**:
   ```
   cd Library_management_system
   ```

3. **Install Dependencies**:
   - Install the MySQL connector for Python:
     ```
     pip install mysql-connector-python
     ```

4. **Database Setup**:
   - Create a MySQL account with a username and password.
   - Create a database using the following SQL command:
     ```
     CREATE DATABASE databasename;
     ```
   - Switch to the newly created database:
     ```
     USE databasename;
     ```
   - Ensure that MySQL is running in the background.

5. **Run the Python File**:
   - Execute the Python script to start the Library Management System:
     ```
     python library_management.py
     ```

## Usage

- Upon running the script, a menu will be displayed with the available operations.
- Follow the prompts to add, issue, submit, display, or delete books.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to create pull requests.
