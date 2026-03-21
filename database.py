# All SQL stuff here
import pymysql

# settings to connect to MYSQL SEVER without selecting a database
# used only to create the database if it doesn't exist
DATABASE_CREATE_SETTINGS = {
    "host" : "localhost",       # mysql sever is running on computer
    "user" : "root",            # mysql username
    "password" : "Bharath@",    # password
    "port" : 3306               # default mysql port
}

# settings to connect to MySQL server with the expense_tracker database selected
# used for all normal operations (fetch, add, delete)
DATABASE_SETTINGS = {
    "host" : "localhost",
    "user" : "root",
    "password" : "Bharath@",
    "database" : "expense_tracker",     # which databese to use
    "port" : 3306
}

# returns a new connection to expense_tracker database
# called by fetch, add, delete functions
def get_connection():
    return pymysql.connect(**DATABASE_SETTINGS)

def init_db():
    try:
        # connect without database and create it if not exists
        connection = pymysql.connect(**DATABASE_CREATE_SETTINGS)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker")
        connection.commit()
        connection.close()
        
        # connect with database and create table if not exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                date        DATE,
                category    VARCHAR(50),
                amount      DECIMAL(10,2),
                description VARCHAR(50)
            )
        """)
        connection.commit()
        connection.close()
        return True
    
    except Exception as error:
        print("Database init error:", error)
        return False    # failed to connect or create
  
        
def fetch_expenses():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # fetch all rows ordered by newest date first
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        all_expenses = cursor.fetchall()
        connection.close()
        return all_expenses
    except Exception as error:
        print("Fetch error:", error)
        return []   # return empty list if failed


def add_expenses(date, category, amount, description):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # %s are placeholders, values passed as tuple to prevent SQL injection
        cursor.execute("""
            INSERT INTO expenses (date, category, amount, description)
            VALUES (%s, %s, %s, %s)
        """, (date, category, float(amount), description))
        connection.commit()
        connection.close()
        return True
    except Exception as error:
        print("Add error:", error)
        return False

def delete_expenses(expense_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # delete only the row matching the given id
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        connection.commit()
        connection.close()
        return True
    except Exception as error:
        print("Delete error:", error)
        return False

def reset_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE expenses")  # deletes all rows and resets ID to 1
        connection.commit()
        connection.close()
        return True
    except Exception as error:
        print("Reset error:", error)
        return False