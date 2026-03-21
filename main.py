# Running the App

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db, reset_db
from app import ExpenseApp

def main():
    # create the PyQt6 application, must be created before any UI
    app = QApplication(sys.argv)
    
    # initialize database and table before showing the window
    # if it fails, show error and exit immediately
    if not init_db():       
        QMessageBox.critical(None, "Error", "Could not load your database...")
        sys.exit(1)     #after 1sec
    
    reset_db()

    # create and show the main window
    window = ExpenseApp()
    window.show()
    
     # start the event loop — keeps app running until window is closed
    sys.exit(app.exec())



if __name__ == "__main__":
    main()  # only runs when this file is executed directly