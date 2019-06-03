import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import tkinter.messagebox


def send_email():
    if "@" and "." in email.get():
        msg = MIMEMultipart()
        message = "ELO"
        # lipa ze haslo jest w kodzie
        email_password = "123QWEqwe"
        msg['From'] = "fast_typing@op.pl"
        msg['To'] = email.get()
        msg['Subject'] = "REJESTRACJA MORDO"
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.op.pl: 587')
        server.starttls()
        server.login(msg['From'], email_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    else:
        tk.messagebox.showinfo('BŁĄD', 'Niepoprawny mail')


def makeEntry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP, anchor='w', expand=True)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, anchor='w', fill=tk.BOTH)
    return entry


def make_title(root, caption, size):
    napis = tk.Label(root, text=caption, font=("Times", size))
    napis.pack(anchor='n', expand=True)
    return napis


root = tk.Tk()
root.title("Rejestracja")
# Text
make_title(root, "Siemanko", 15)
# Entrys
email = makeEntry(root, "Email", 16)
username = makeEntry(root, "Login", 16)
password = makeEntry(root, "Haslo", 16, show="*")
password2 = makeEntry(root, "Powtorz haslo", show="*")
rejestrButton = tk.Button(root, borderwidth=4, text="Rejestracja", width=16, command=send_email)
rejestrButton.pack(side=tk.BOTTOM)
root.mainloop()
