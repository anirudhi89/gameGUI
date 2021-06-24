# idea: have main be a gui where i can select a variety of projects
import tkinter as tk
from tkinter import *
from tkinter import ttk

import rps
from rps import *

window = tk.Tk()

greeting = tk.Label(
                    text="Game Library",
                    foreground = "white", #text color
                    background = "#34A2FE", #label bg color
                    width = 10,
                    height = 7
                    )
greeting.pack()

#click, start Rock Paper Scissors game, to be activated on click
def startRPS():
    print("Starting Rock Paper Scissors")
    rps.playGame()

rp  = tk.Button(
                text = "Rock Paper Scissors (Text-Based)",
                command = startRPS
                )


txtbx = tk.Text()



txtbx.get(1.0)

rp.pack()
txtbx.pack()
window.mainloop()

