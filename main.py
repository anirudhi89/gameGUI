# idea: have main be a gui where i can select a variety of projects
#WIP, last updated 6.23
#Shoutout pythonguides.com, realpython.com
import tkinter as tk
import rps

window = tk.Tk()
window.title('Game Library')
window.geometry('500x450+500+200')
window.config(bg="#223441")

greeting = tk.Label(
                    text="Game Library",
                    foreground = "white", #text color
                    background = "#34A2FE", #label bg color
                    width = 80,
                    height = 2
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




rp.pack()
window.mainloop()

