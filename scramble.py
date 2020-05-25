import random
from tkinter import filedialog
from tkinter import *

moves = ["F", "U", "R", "L", "B", "D"]

class scramble:
    def __init__(self, frame, r, c):
        self.frame = frame
        self.r = r
        self.c = c
        self.scrambles = []

        self.bar = Label(frame)
        self.bar.grid(row=r, column=c)
    
    def Gen(self):
        scramble = ""
        lst = ""
        move = ''
        for i in range(20):
            move = random.choice(moves)
            while move == lst:
                move = random.choice(moves)
            lst = move
            rand = random.randint(0, 3)
            if rand == 0:
                move += "2"
            elif rand == 1:
                move += "'"
            scramble += move + " "
        self.bar.config(text=scramble, font=("Helvetica", 20))
        self.scrambles.append(scramble)
