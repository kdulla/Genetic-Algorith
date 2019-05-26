#!/usr/bin/env python3

from tkinter import *
from car import Car
from track import *

HEIGHT = 1200
WIDTH = 1200
FPS = 1000 // 60

root = Tk()
root.title("Genetic Algos")

cv = Canvas(root, width = WIDTH, height = HEIGHT)
cv.configure(background = 'white')
cv.pack()

last_key = None

def start():
    path = [(250, 250), (250, 450), (450, 650), (650, 450), (650, 250), (450, 50)]
    track = Track.path_to_track(path)
    return track

def key(event):
    global last_key

    if event.char == 'w':
        last_key = "w"
    elif event.char == 'a':
        last_key = "a"
    elif event.char == 's':
        last_key = None
    elif event.char == 'd':
        last_key = "d"

def key_release(event):
    global last_key

    if event.char == 'w' and last_key == "w":
        last_key = None
    elif event.char == 'a' and last_key == "a":
        last_key = None
    elif event.char == 's' and last_key == "s":
        last_key = None
    elif event.char == 'd' and last_key == "d":
        last_key = None

root.bind("<Key>", key)
root.bind("<KeyRelease>", key_release)

c = Car(WIDTH / 2, HEIGHT / 2)
t = start()

def tick():
    if last_key == "w":
        c.accel()
    elif last_key == "a":
        c.turn_left()
    elif last_key == "d":
        c.turn_right()

    c.update()
    cv.delete("all")
    c.draw(cv)
    t.draw(cv)
    root.after(FPS, tick)

root.after(FPS, tick)

root.mainloop()
