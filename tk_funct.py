#imports all of the necessary libraries
from tkinter import *
from login import *


#creates the root tkinter window with options to Create Account, #Login, or Quit
def create_root():
    root = Tk()
    root.geometry ("500x500")
    create = Button(root, text = 'Create Account', command = lambda:create_window(root))
    create.grid(row = 0, column = 7)
    log = Button(root, text = 'Login', command = lambda:LoginWindow(root))
    log.grid(row = 1, column = 7)
    out = Button(root, text = 'Quit', command = root.destroy)
    out.grid(row = 3, column = 7)
    root.mainloop()


#returns whatever window is inputted back to the root window
def Return(login_wind, root):
    login_wind.destroy
    root.deiconify()


#if an account is created succesfully, returns to the root window
def check_create_acc(user, pword, fname, lname, create_wind, root):
  if create_acc(user, pword, fname, lname):
    Return(create_wind, root)


#creates a window where users can enter all of the parameters #required to create an account and where users can create the #account
def create_window(root):
    create_wind = Toplevel(root)
    root.withdraw()
    create_wind.title('Create Account')
    create_wind.geometry('500x500')
    user = Label(create_wind, text = 'Enter your username: ')
    user.grid(row = 0, column = 0)
    pword = Label(create_wind, text = 'Enter your password: ')
    pword.grid(row = 1, column = 0)
    fname = Label(create_wind, text = 'Enter your first name: ')
    fname.grid(row = 2, column = 0)
    lname = Label(create_wind, text = 'Enter your last name: ')
    lname.grid(row = 3, column = 0)
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()
    userent = Entry(create_wind, textvariable = e1, bg="light gray", fg="black")
    userent.grid(row = 0, column = 1)
    pwordent = Entry(create_wind, textvariable = e2, bg="light gray", fg="black")
    pwordent.grid(row = 1, column = 1)
    fnament = Entry(create_wind, textvariable = e3, bg="light gray", fg="black")
    fnament.grid(row = 2, column = 1)
    lnament = Entry(create_wind, textvariable = e4, bg="light gray", fg="black")
    lnament.grid(row = 3, column = 1)
    enterbutton = Button(create_wind, text = 'Create', command = lambda:check_create_acc(userent.get(), pwordent.get(), fnament.get(), lnament.get(), create_wind, root))
    enterbutton.grid(row = 7, column = 0)
    backbutton = Button(create_wind, text = 'Back', command = lambda:Return(create_wind, root))
    backbutton.grid(row = 7, column = 1)
    create_wind.mainloop()


#if a user logs in successfully, creates the Tank GUI window with, #at the moment, a welcome statement and logout button
def check_logged_in(user, password, login_wind, root):
  valid, name = login(user, password)
  if valid:
    tank_wind = Toplevel(login_wind)
    login_wind.withdraw()
    tank_wind.title('Tank Interface')
    
    tank_wind.geometry('500x500')
    
    canvas = Canvas(tank_wind, bg = 'white', height = 500, width = 500)
    canvas.pack()
    canvas.create_line(250, 0, 250, 500, fill='black')
    canvas.create_line(0, 175, 500, 175, fill = 'black')
    welcome = Label(tank_wind, text = f'Welcome {name}')
    logout = Button(tank_wind, text = 'Logout', command = lambda:Return(tank_wind, root))
    canvas.create_window(250, 20, window = welcome)
    canvas.create_window(400, 20, window = logout)
    tank_wind.mainloop()


#creates a window where the user can log into the Tank GUI, and #the window notifies the user of successful login, incorrect #password, or account nonexistance
def LoginWindow(root):
    login_wind = Toplevel(root)
    root.withdraw()

    login_wind.title('Login')
    login_wind.geometry('500x500')
    user = Label(login_wind, text = 'Enter your username: ')
    user.grid(row = 0, column = 0)
    pword = Label(login_wind, text = 'Enter your password: ')
    pword.grid(row = 1, column = 0)
    e1 = StringVar()
    e2 = StringVar()
    userent = Entry(login_wind, textvariable = e1, bg="light gray", fg="black")
    userent.grid(row = 0, column = 1)
    pwordent = Entry(login_wind, textvariable = e2, bg="light gray", fg="black")
    pwordent.grid(row = 1, column = 1)
    enterbutton = Button(login_wind, text = 'Login', 
    command = lambda:check_logged_in(userent.get(), pwordent.get(), login_wind, root))
    enterbutton.grid(row = 5, column = 0)
    backbutton = Button(login_wind, text = 'Back', command = lambda:Return(login_wind, root))
    backbutton.grid(row = 5, column = 1)
    login_wind.mainloop()


