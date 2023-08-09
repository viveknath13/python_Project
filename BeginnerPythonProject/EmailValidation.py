import re
import tkinter as tk
from tkinter import messagebox


#Creating a function that returns  a  regular expression

def is_valid_email(email):
    email_format = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    return re.match( email_format,email)


def checking_email():
    email = email_entry.get()
    if is_valid_email(email):
        messagebox.showinfo("Valid email"," Wow Your email is valid")
    else:
            messagebox.showerror("Invalid email","what the hack yar , Your email is not valid enter your valid email address")
            
    
    
    
#creating a disaply to show that the email

app = tk.Tk()
app.title("Email validation")
app.geometry("600x400")
app.configure(bg="Yellow")

#Create a widget for the email
label = tk.Label(app,text="Enter the valid email address:", font="anchor",bg="white",fg="red")
label.pack(pady=40)

email_entry = tk.Entry(app, width=60)
email_entry.pack()

#Creating a button for the email

button = tk.Button(app,text="Click me ",fg= "black", font= "arial",command=checking_email)
button.pack(pady = 40)

app.mainloop()

