from Tkinter import *
import time

def eventInfo(eventName, ctime):
    # helper function to create a string with the event's info
    # also, prints the string for debug info
    msg = ""
    msg += eventName
    msg += " at " + str(ctime)
    print msg

def leftMousePressed(event):
    canvas = event.widget.canvas  
    eventInfo("leftMousePressed", time.time() - canvas.base)
    canvas.data["lefttime"] = time.time() - canvas.base
    canvas.clicks.append(canvas.data["lefttime"])
    redrawAll(canvas)

def redrawAll(canvas):
    canvas.delete(ALL)
    # Draw the "L"
    font = ("Arial", 24, "bold")
    time = canvas.data["lefttime"]
    canvas.create_text(200, 50, text=str(time), font=font)

def init(canvas):
    canvas.data["lefttime"] = 0
    canvas.base = time.time()
    canvas.clicks = []
    redrawAll(canvas)

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=600, height=300)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", leftMousePressed)
    # root.bind("<Key>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()