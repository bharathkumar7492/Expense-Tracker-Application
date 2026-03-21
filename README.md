# Expense Tracker App

A desktop application to track daily expenses built with Python, PyQt6 and MySQL.

## Features
- Add expenses with date, category, amount and description
- Delete expenses
- Data stored in MySQL database
- Clean and simple UI

## Technologies
- Python 3
- PyQt6 — desktop UI
- MySQL — database
- PyMySQL — MySQL connector

## Setup

### 1. Install dependencies
pip install pyqt6 pymysql

### 2. Update MySQL password
Open database.py and change:
password : "your_password"

### 3. Run the app
python main.py

## Project Structure
expense_tracker_app/

│

├── main.py        — app entry point

├── app.py         — UI design and logic

├── database.py    — all database operations

└── README.md

## Author
Bharathkumar Ravi
