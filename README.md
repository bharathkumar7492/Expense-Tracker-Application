# Expense Tracker

A simple desktop **Expense Tracker application** built with Python and PyQt6.

I built this project to practice connecting a Python desktop application with a MySQL database and to understand how basic database operations work in a real application.

## Tech Used

* Python
* PyQt6
* MySQL
* PyMySQL

## Features

* Add a new expense
* Select expense date
* Select expense category
* Enter amount and description
* View expenses in a table
* Delete a selected expense
* Input validation for amount and required fields
* Automatically creates the database and expenses table if they don't exist

## Project Structure

```text
Expense-Tracker/
│
├── app.py          # PyQt6 user interface and application logic
├── database.py     # MySQL connection and database operations
├── main.py         # Starts the application
└── README.md
```

## How It Works

The application has three main parts:

**`main.py`**

Starts the PyQt6 application and initializes the MySQL database before opening the expense tracker window.

**`app.py`**

Contains the user interface. It handles the date picker, category dropdown, input fields, buttons, table, validation, and user actions.

**`database.py`**

Handles all MySQL-related operations such as creating the database and table, adding expenses, fetching expenses, and deleting expenses.

## Database

The application uses a MySQL database called:

```text
expense_tracker
```

It creates an `expenses` table with the following columns:

```text
id
date
category
amount
description
```

The database and table are created automatically when the application starts if they do not already exist.

## Setup

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install required packages

Open the terminal in the project folder and run:

```bash
pip install PyQt6 PyMySQL
```

### 3. Configure MySQL

Make sure MySQL Server is running.

Update the MySQL username and password in `database.py` if required:

```python
DATABASE_CREATE_SETTINGS = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "port": 3306
}
```

Also update the password in `DATABASE_SETTINGS`.

### 4. Run the application

```bash
python main.py
```

The application will open after successfully connecting to MySQL.

## What I Learned

Through this project, I practiced:

* Building a desktop GUI using PyQt6
* Connecting Python applications with MySQL
* Performing database operations using PyMySQL
* Working with SQL `INSERT`, `SELECT`, and `DELETE`
* Handling user input and validation
* Connecting buttons and UI elements to Python functions
* Organizing a small Python project into separate files

## Author

**Bharath Kumar Ravi**

GitHub: `bharathkumar7492`
