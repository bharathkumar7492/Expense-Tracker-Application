# App Design
# pip3 install pyqt6

from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, 
                             QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView)
from PyQt6.QtCore import QDate, Qt
from database import fetch_expenses, add_expenses, delete_expenses


class ExpenseApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.settings()     # set window size and title
        self.initUI()       # create all widgets
        self.load_table_data()  # load existing expenses from database

    
    def settings(self):
        self.setGeometry(100, 100, 550, 450)    # horizontal, vertical, width, height
        self.setWindowTitle("Expense Tracker App")
        
    # Design
    def initUI(self):
        # create all objects
        # date picker - defaults to today's date
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        
        # dropdown for expense category
        self.dropdown = QComboBox()
        # text input for amount & description
        self.amount = QLineEdit()
        self.description = QLineEdit()
        
        self.add_button = QPushButton("Add Expense")
        self.add_button.setObjectName("add_button")
        self.delete_button = QPushButton("Delete Expense")
        self.delete_button.setObjectName("delete_button")
        
        self.table = QTableWidget(0,5)  #table with 5 column
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        # stretch all columns to fill the table width equally
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.populate_dropdown()    
        
        # connect buttons to their functions 
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)
        
        self.apply_styles()     # apply CSS
        self.setup_layout()     # arrange Layout (Row/column)
        
    def setup_layout(self):
        master = QVBoxLayout()  # main vertical layout
        row1 = QHBoxLayout()    # date & category row
        row2 = QHBoxLayout()    # amount & description row
        row3 = QHBoxLayout()    # buttons row
        
        # row 1
        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.dropdown)
        
        # row 2
        row2.addWidget(QLabel("Amount"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)
        
        # row 3
        row3.addWidget(self.add_button)
        row3.addWidget(self.delete_button)
        
        # stack rows vertically then add table below
        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addWidget(self.table)
        
        self.setLayout(master)
    
    
    def apply_styles(self):
        # CSS styling
            self.setStyleSheet("""

        QWidget {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #333333;
        }

        QLabel {
            font-size: 14px;
            font-weight: bold;
            color: #333333;
        }

        QLineEdit, QComboBox, QDateEdit {
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #cccccc;
            border-radius: 6px;
            padding: 6px 10px;
        }

        QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
            border: 1px solid #4a90d9;
        }

        QPushButton {
            background-color: #4a90d9;
            color: #ffffff;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #357abd;
        }

        QPushButton:pressed {
            background-color: #2a6099;
        }

        QTableWidget {
            background-color: #ffffff;
            alternate-background-color: #f0f6ff;
            gridline-color: #dddddd;
            border: 1px solid #cccccc;
            font-size: 13px;
        }

        QHeaderView::section {
            background-color: #4a90d9;
            color: #ffffff;
            font-weight: bold;
            padding: 8px;
            border: none;
        }

        QTableWidget::item:selected {
            background-color: #cce0f5;
            color: #333333;
        }

    """)

    
    def populate_dropdown(self):
        # list of expense categories shown in dropdown
        categories = ["Food", "Rent", "Bills", "Entertainment", "shopping", "Other"]
        self.dropdown.addItems(categories)
        
    def load_table_data(self):
        # fetch all expenses from database and display in table
        expenses = fetch_expenses()
        self.table.setRowCount(0)   # clear existing rows first
        for row_index, expense in enumerate(expenses):
            self.table.insertRow(row_index)
            for column_index, data in enumerate(expense):
                # convert every value to string for display
                self.table.setItem(row_index, column_index, QTableWidgetItem(str(data)))
    
    def clear_inputs(self):
        # reset all input fields after adding an expense
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()
    
    def add_expense(self):
        # get values from all input fields
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()      #QcomboBox
        amount = self.amount.text()     #QLineEdit
        description = self.description.text()

        # validate inputs are not empty
        if not amount or not description:
            QMessageBox.warning(self, "Input Error", "Amount and Description can not be empty")
            return 
        
        # validate amount is a valid number
        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Amount must be a valid number")
            return

        # validate amount is a valid number
        if add_expenses(date, category, amount, description):
            self.load_table_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense")
    
    def delete_expense(self):
        # get currently selected row
        selected_row = self.table.currentRow()
        if selected_row == -1:    # -1 means no row selected
            QMessageBox.warning(self, "uh oh", "You need to choose a row to delete.")
            return
        
        # get the id from column 0 of selected row
        expense_id = int(self.table.item(selected_row, 0).text())
        # ask user to confirm before deleting
        confirm =  QMessageBox.question(self, "Confirm", "Are you sure you want to delete?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expenses(expense_id):
            self.load_table_data()  # refresh table after delete
        else:
            QMessageBox.critical(self, "Error", "Failed to delete expense")