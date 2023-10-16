#import all necessary libraries
import sqlite3
from cryptography.fernet import Fernet
import pandas as pd


#open file that contains the encryption and decryption key
with open("fernet_key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)


#connect to SQL database
conn = sqlite3.connect('tank_database')
c = conn.cursor()


#creates a new table, if one doe not already exist, that has #parameters user id, username, password, first name, and last name
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tank_database 
    ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
    [username] TEXT,
    [password] TEXT,
    [firstname] TEXT,
    [lastname] TEXT)''')


#creates an account, if the username is not already taken, stores #all the parameters in the database, and notifies the user of the #successful account creation
def create_acc(username, password, firstname, lastname):
    c.execute('''SELECT username FROM tank_database WHERE username = ?''', (username,))
    existing_user = c.fetchone()
    if existing_user:

        print('This account already exists, choose a different username')
        return False
    else:
        enc_password = fernet.encrypt(password.encode())
        #print("Encrypted Password:", enc_password)
        c.execute('''
        INSERT INTO tank_database (username, password, firstname, lastname)
        VALUES
        (?, ?, ?, ?)
        ''', (username, enc_password, firstname, lastname))
        conn.commit()
        print('You have created an account')
        return True


#logs the user into the Tank GUI if the username and password #entered match an acount in the database
def login(username, password):
    c.execute('''SELECT password FROM tank_database WHERE username = ?''', (username,))
    existing_user = c.fetchone()
    if existing_user is None:
        print('This account does not exist, please create one')
        return False, 'nope'
    else:
        password_database = existing_user[0]
        try:
            decrypted_data_password = fernet.decrypt(password_database).decode()
            if password == decrypted_data_password:
                print('You are now logged in')
                c.execute('''SELECT firstname FROM tank_database WHERE username = ?''', (username,))
                use = c.fetchone()
                name = use[0]
                return True, name
            else:
                print('Incorrect password, please try again')
                return False, 'nope'
        except Exception as e:
            print(f'The error was: {e}')



