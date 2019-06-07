import tkinter as tk
import keyboard
import time
from StopWatch import StopWatch

'''
TODO no of errors
'''

def check_key(key, name, symbol):
    global pattern
    global counter
    if pattern[counter] == symbol:
        if key == name:
            tmp.append(pattern[counter])
            text.set(''.join(tmp))
            text_label.config(bg = 'green')
            counter += 1
            return True
        else:
            return False
def typing(key):
    global counter
    global pattern
    global errors
    if pattern[counter] == key.name:
        tmp.append(pattern[counter])
        text.set(''.join(tmp))
        text_label.config(bg="green")
        counter += 1
    elif check_key(key.name, 'space', ' '):
        pass
    elif check_key(key.name, 'enter', '\n'):
        pass
    elif check_key(key.name, 'tab', '\t'):
        pass
    else:
        errors += 1
        text_label.config(bg="red")
    if counter >= len(pattern):
        unhook()
        return

def hook():
    sw.Reset()
    sw.Start()                                          #kontrola stopwatcha
    global counter
    global pattern
    counter = 0
    pattern = box.get('1.0', 'end-1c')                  #zaciągnięcie tekstu z pola
    box.config(state=tk.DISABLED)
    keyboard.on_press(typing)
    text.set("GO!")

def unhook():
    sw.Stop()
    words = len(pattern.split())
    words_var.set("Words per minute: {}".format(len(pattern.split())*60/sw._elapsedtime))
    keyboard.unhook_all()
    text.set("")
    box.config(state=tk.NORMAL)
    tmp.clear()

root = tk.Tk()
root.geometry('800x600')
sw = StopWatch(root)
sw.pack(side="top")
tmp = []
errors = 0
counter = 0
pattern = ""
text = tk.StringVar()
text_label = tk.Label(root, textvariable=text, bg="green")
text_label.pack()
start = tk.Button(root, text="Start", command=hook)
stop = tk.Button(root, text="Stop", command=unhook)
start.pack()
stop.pack()
box = tk.Text(root, width=80, height=13)
box.pack()
words_var = tk.StringVar()
wpm = tk.Label(root, textvariable=words_var)
wpm.pack(side='bottom')

root.mainloop()
