import tkinter as tk
import keyboard
import time
from StopWatch import StopWatch

def typing(key):
    global counter
    global pattern
    if counter >= len(pattern):
        unhook()
        return
    if pattern[counter] == key.name:
        tmp.append(pattern[counter])
        text.set(''.join(tmp))
        text_label.config(bg="green")
        counter += 1
    elif pattern[counter] == ' ':
        if key.name == 'space':
            tmp.append(' ')
            text.set(''.join(tmp))
            text_label.config(bg='green')
            counter += 1
    elif pattern[counter] == '\n':
        if key.name == 'enter':
            tmp.append('\n')
            text.set(''.join(tmp))
            text_label.config(bg='green')
            counter += 1
    else:
        text_label.config(bg="red")

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
    #keyboard.wait()

def unhook():
    sw.Stop()
    keyboard.unhook_all()
    box.config(state=tk.NORMAL)

def main():
    #root = Tk()
    sw = StopWatch(root)
    sw.pack(side="top")

    #tk.Button(root, text='Start', command=sw.Start).pack(side="left")
    #tk.Button(root, text='Stop', command=sw.Stop).pack(side="left")
    #tk.Button(root, text='Reset', command=sw.Reset).pack(side="left")
    #tk.Button(root, text='Quit', command=root.quit).pack(side="left")

    #root.mainloop()

root = tk.Tk()
root.geometry('800x600')
sw = StopWatch(root)
sw.pack(side="top")
tmp = []
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

root.mainloop()
