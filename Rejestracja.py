from Dane import *


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
