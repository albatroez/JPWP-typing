import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Zadanie 1
def make_register_window():
    # miejsce na kod
                                                                  #sciaga:
                                                                  #tk.Entry()
                                                                  #tk.Label()
                                                                  #tk.Text()


kmiot = tk.Tk()
entry1 = make_register_window()
entry1.pack()
kmiot.mainloop()


# Zadanie 2
def send_email():
    try:
         msg = MIMEMultipart()
         message = "Tu wpisz wiadomosc mailowa"
         msg['From'] =
         msg['To'] =
         msg['Subject'] =
         email_password =
         msg.attach(MIMEText(message, 'plain'))
         server = smtplib.SMTP('smtp. wpisz server z którego wysyłasz maila i port')
         server.starttls()
         server.login("TU ZALOGUJ SIE DO MAILA Z KTOREGO WYSYLASZ")
         server.sendmail("OD , DO")
         server.quit()
    except:
        tk.messagebox.showinfo('BLAD', 'Niepoprawny mail lub hasło')