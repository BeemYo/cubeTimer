import scramble, timer, threading, time
from tkinter import filedialog
from tkinter import *

def space(event):
    if event.char != " ":
        return
    if timer.run == False:
        timer.run = True
        time.sleep(0)
    else:
        timer.stop()
        s.Gen()

def saveTimes():
    
    saves = open("saves.save", "w")
    for tim in timer.times:
        print(tim)
        saves.write(str(tim) + "\n")
        #timer.times.remove(tim)
    saves.close()

root = Tk()
root.title("Cube Timer")

root.bind("<KeyRelease>", space)

save = Button(root)
save.grid(row=0, column=0)
save.config(text="Save", command=saveTimes)

timer = timer.timer(root, 2, 0)

s = scramble.scramble(root, 1, 0)
s.Gen()

timer.update()

root.mainloop()
