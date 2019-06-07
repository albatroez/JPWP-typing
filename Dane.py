import tkinter as tk
import tkinter.messagebox
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

failure_max = 3
passwords = [('student', 'student')]
email_password = "123QWEqwe"
email_address = "fast_typing@op.pl"


def send_email():
    try:
         msg = MIMEMultipart()
         message = """WITAJ
         Założyłeś konto w aplikacji fast typing. Dzieki temu możesz zapisywac swoje wyniki i korzystac z aplikacji kiedy chcesz.
         Twój login i hasło to:
         """ + str(username.get()) + " " + str(password.get())
         msg['From'] = "fast_typing@op.pl"
         msg['To'] = email.get()
         msg['Subject'] = "REJESTRACJA MORDO"
         msg.attach(MIMEText(message, 'plain'))
         server = smtplib.SMTP('smtp.op.pl: 587')
         server.starttls()
         server.login(msg['From'], email_password)
         server.sendmail(msg['From'], msg['To'], msg.as_string())
         server.quit()
    except:
        tk.messagebox.showinfo('BLAD', 'Niepoprawny mail lub hasło')


def makeEntry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP, anchor='w', expand=True)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, anchor='w', fill=tk.BOTH)
    return entry