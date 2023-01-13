import sqlite3
import base64

def open_db():
    # Create a connection to the database
    global conn
    conn = sqlite3.connect("passwords.db")
    # Create a cursor
    global c
    c = conn.cursor()

def close_db():
    # Close the connection
    c.close()
    conn.close()

def createTable():
    open_db()

    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords(
            application TEXT,
            password TEXT
            )
    ''')

    close_db()

createTable()

def add_password(app, password):
    open_db()

    c.execute('''
        INSERT INTO passwords
        VALUES (?,?)
    ''', (app, password))
    conn.commit()

    close_db

def show_database():
    open_db()

    # Get data from database
    c.execute('''
        SELECT * FROM passwords
    ''')
    # Put data in a variable
    data = c.fetchall()
    print(f"|{'Saved Passwords' :^48}|")
    print("-"*50)
    for row in data:
        print(f"|{row[0] + ':' :<18}|{(row[1].decode('UTF-8')):<29}|")
        print("-"*50)
    
    close_db()

def delete_password(app, password):
    open_db()
    
    c.execute('''
        DELETE FROM passwords
        WHERE application = (?) AND
        password = (?)
    ''', (app, password))
    conn.commit()

    close_db()

# add_password("YouTube", "asdmnbqwhjg823")
# show_database()
# delete_password("YouTube", "asdmnbqwhjg823")
