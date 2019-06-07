import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import keyboard

# Zadanie 1
def make_register_window():
    pass# miejsce na kod
                                                                  #sciaga:
                                                                  #tk.Entry()
                                                                  #tk.Label()
                                                                  #tk.Text()


# Zadanie 2
def send_email():
    try:
         msg = MIMEMultipart()
         message = "Tu wpisz wiadomosc mailowa"
         msg['From'] = ''
         msg['To'] = ''
         msg['Subject'] = ''
         email_password = ''
         msg.attach(MIMEText(message, 'plain'))
         server = smtplib.SMTP('smtp. wpisz server z którego wysyłasz maila i port')
         server.starttls()
         server.login("TU ZALOGUJ SIE DO MAILA Z KTOREGO WYSYLASZ")
         server.sendmail("OD , DO")
         server.quit()
    except:
        tk.messagebox.showinfo('BLAD', 'Niepoprawny mail lub hasło')

# Zadanie 3
'''
Napisz funkcję, która wypisywać będzie kolejne znaki wciśnięte na klawiaturze w jednej linii
keyboard.on_press(callback, suppress=False)
Invokes callback for every KEY_DOWN event.

The event passed to the callback is of type keyboard.KeyboardEvent, with the following attributes:

name: an Unicode representation of the character (e.g. "&") or description (e.g. "space"). The name is always lower-case.
scan_code: number representing the physical key, e.g. 55.
time: timestamp of the time the event occurred, with as much precision as given by the OS.
'''

def print_key(key):
    print()

def typing():
    keyboard.on_press(print_key)

# Zadanie 4
'''
Napisz funkcję, która utworzy dwa obiekty tk.Label. Jeden z danym tekstem - wzorcem, a drugi aktualizowany przez
tk.StringVar (użyj argumentu textvariable w tk.Label). Następnie korzystając z keyboarda, podobnie
jak w poprzednim zadaniu wychwytuj wciśnięte klawisze, ale wypisuj tylko te, które zgadzają się ze wzorcem.
Skorzystaj z metody tk.StringVar.set()
'''
def check_pattern():
    pattern = ''
    text = tk.StringVar()



if __name__ == '__main__':
    kmiot = tk.Tk()
    entry1 = make_register_window()
    #entry1.pack()
    #typing()
    kmiot.mainloop()
