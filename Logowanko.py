import tkinter.messagebox
import tkinter as tk
import os

failure_max = 3

passwords = [('DaniWeb', 'best1'), ('newbie', 'help!help!'), ('student', 'student')]


def makeEntry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP, anchor='w', expand=True)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, anchor='w', fill=tk.BOTH)
    return entry


def enter(event):
    check_password()


def check_password(failures=[]):

    print(userEntry.get(), passwordEntry.get())

    if (userEntry.get(), passwordEntry.get()) in passwords:
        root.destroy()
        os.system('python tk_test.py')
        return #otwarcie okienka z apka
    else:
        userEntry.delete(0, 'end')
        passwordEntry.delete(0, 'end')
        failures.append(1)

    if sum(failures) == failure_max:
        for i in range(failure_max):
            failures.remove(1)
        tk.messagebox.showinfo('zle haslo', 'Trzecia nieudana proba wpisania hasla')
        answer = tk.messagebox.askquestion('Wysylanie maila', "Czy wyslac maila z przypomnianiem hasla?")
        if answer == 'yes':
            print('wysylanie maila')




def zapomniales():
    o = tk.Tk()
    o.title('Przypominanie maila')
    mailEntry = makeEntry(o, "Prosze o wpisanie maila", 24)
    sendButton = tk.Button(o, text="Send", command=o.destroy) #Jak bedzie to wysylanie maila z przypomnieniem
    mailEntry.pack()
    sendButton.pack(side=tk.BOTTOM)
    o.mainloop()


def openRejestr():
    root.destroy()
    os.system('python Rejestracja.py')



root = tk.Tk()
root.geometry('300x230')
root.title('Enter your information')
# frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH)
# entry with not shown text
userEntry = makeEntry(parent, "User name", 16)
passwordEntry = makeEntry(parent, "Password", 16, show="*")
# button to attempt to login
loginButton = tk.Button(parent, borderwidth=4, text="Login", width=20, pady=8, command=check_password)
passwordButton = tk.Button(parent, borderwidth=4, text="Nie pamietasz hasla?", width=20, pady=8, command=zapomniales)
rejestrButton = tk.Button(parent, borderwidth=4, text="Rejestracja", width=10, command=openRejestr)
passwordButton.pack(side=tk.BOTTOM)
loginButton.pack(side=tk.BOTTOM)
rejestrButton.pack(side=tk.RIGHT)
# checkbox (logout)
checkbox = tk.Checkbutton(parent, text="Nie wylogowywuj mnie")
checkbox.pack(side=tk.LEFT, pady=5)
passwordEntry.bind('<Return>', enter)
userEntry.focus_set()
parent.mainloop()