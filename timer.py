import time
from tkinter import *

class timer:
    def __init__(self, frame, r, c):
        self.frame = frame
        self.r = r
        self.c = c

        self.run = False
        self.times = []
        self.last = time.time()

        self.timer = Label(frame)
        self.timer.grid(row=r, column=c)
    
    def update(self):
        if self.run == False:
            self.last = time.time()
            self.timer.config(text="0.000", font=("Helvetica", 40))
        else:
            self.curtime = round(time.time() - self.last, 3)
            self.timer.config(text=self.curtime)
        self.frame.after(10, lambda: self.update())
    
    def stop(self):
        self.run = False
        self.times.append(self.curtime)
