import tkinter as tk                                                                    #Importing libraries
import pygame as pg
from statemachine import StateMachine, State


root = tk.Tk()                                                                          #Defines root window and its properties
root.title("EDM Player")
root.geometry("400x500")
pg.init()                                                                               #initialising pygame libraries
pg.mixer.init()



class edmPlayer(StateMachine):                                                          #defining state machine
    stop = State('stop', initial=True)
    pause = State('pause')
    playing = State('play')

    starting = stop.to(playing)
    unpause = pause.to(playing)
    pauseing = playing.to(pause)
    stoping = playing.to(stop)
    stopping2 = pause.to(stop)



m1 = edmPlayer()                                                                        #createing instance of state machine
m2 = edmPlayer()
m3 = edmPlayer()
m4 = edmPlayer()
m5 = edmPlayer()
m6 = edmPlayer()
m7 = edmPlayer()
m8 = edmPlayer()
m9 = edmPlayer()
m10 = edmPlayer()
m11 = edmPlayer()
m12 = edmPlayer()
m13 = edmPlayer()
m14 = edmPlayer()
m15 = edmPlayer()
m16 = edmPlayer()

s1 = pg.mixer.Sound('G 128 G.wav')                                                      #storing and reading audio files
s2 = pg.mixer.Sound('G 140 D.wav')
s3 = pg.mixer.Sound('G128 F.wav')
s4 = pg.mixer.Sound('G160 D#m.wav')
s5 = pg.mixer.Sound('Brass 140BPM.wav')
s6 = pg.mixer.Sound('brass 150BPM.wav')
s7 = pg.mixer.Sound('brass 150BPM1.wav')
s8 = pg.mixer.Sound('brass 180BPM.wav')
s9 = pg.mixer.Sound('string 110 G#m.wav')
s10 = pg.mixer.Sound('string 128 F#m.wav')
s11 = pg.mixer.Sound('string 140 C#m.wav')
s12 = pg.mixer.Sound('string 140 E.wav')
s13 = pg.mixer.Sound('dc 150.wav')
s14 = pg.mixer.Sound('sc128.wav')
s15 = pg.mixer.Sound('trap 128.wav')
s16 = pg.mixer.Sound('trap 150.wav')

x1 = 0                                                                                  #creating global variables for each button
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
x11 = 0
x12 = 0
x13 = 0
x14 = 0
x15 = 0
x16 = 0

def but1():                                                                             #function contaning functionalities of button
    global x1                                                                           #taking global variable
    if x1 == 0:
        if m1.is_stop or m1.is_pause:                                                   #checking condition
            s1.play(-1)                                                                 #playing audio file in loop 
            if m1.is_stop:
                m1.starting()                                                           #changing state
            if m1.is_pause:
                m1.unpause()

    if x1 == 1:
        if m1.is_playing:
            s1.stop()                                                                   #pauseing looped sound
            m1.pauseing()
            x1 -=1
    if m1.is_playing:
        x1 += 1

def but2():
    global x2
    if x2 == 0:
        if m2.is_stop or m2.is_pause:
            s2.play(-1)
            if m2.is_stop:
                m2.starting()
            if m2.is_pause:
                m2.unpause()

    if x2 == 1:
        if m2.is_playing:
            s2.stop()
            m2.pauseing()
            x2 -=1
    if m2.is_playing:
        x2 += 1
        
def but3():
    global x3
    if x3 == 0:
        if m3.is_stop or m3.is_pause:
            s3.play(-1)
            if m3.is_stop:
                m3.starting()
            if m3.is_pause:
                m3.unpause()

    if x3 == 1:
        if m3.is_playing:
            s3.stop()
            m3.pauseing()
            x3 -=1
    if m3.is_playing:
        x3 += 1
        
def but4():
    global x4
    if x4 == 0:
        if m4.is_stop or m4.is_pause:
            s4.play(-1)
            if m4.is_stop:
                m4.starting()
            if m4.is_pause:
                m4.unpause()

    if x4 == 1:
        if m4.is_playing:
            s4.stop()
            m4.pauseing()
            x4 -=1
    if m4.is_playing:
        x4 += 1
        
def but5():
    global x5
    if x5 == 0:
        if m5.is_stop or m5.is_pause:
            s5.play(-1)
            if m5.is_stop:
                m5.starting()
            if m5.is_pause:
                m5.unpause()

    if x5 == 1:
        if m5.is_playing:
            s5.stop()
            m5.pauseing()
            x5 -=1
    if m5.is_playing:
        x5 += 1

def but6():
    global x6
    if x6 == 0:
        if m6.is_stop or m6.is_pause:
            s6.play(-1)
            if m6.is_stop:
                m6.starting()
            if m6.is_pause:
                m6.unpause()

    if x6 == 1:
        if m6.is_playing:
            s6.stop()
            m6.pauseing()
            x6 -=1
    if m6.is_playing:
        x6 += 1

def but7():
    global x7
    if x7 == 0:
        if m7.is_stop or m7.is_pause:
            s7.play(-1)
            if m7.is_stop:
                m7.starting()
            if m7.is_pause:
                m7.unpause()

    if x7 == 1:
        if m7.is_playing:
            s7.stop()
            m7.pauseing()
            x7 -=1
    if m7.is_playing:
        x7 += 1

def but8():
    global x8
    if x8 == 0:
        if m8.is_stop or m8.is_pause:
            s8.play(-1)
            if m8.is_stop:
                m8.starting()
            if m8.is_pause:
                m8.unpause()

    if x8 == 1:
        if m8.is_playing:
            s8.stop()
            m8.pauseing()
            x8 -=1
    if m8.is_playing:
        x8 += 1

def but9():
    global x9
    if x9 == 0:
        if m9.is_stop or m9.is_pause:
            s9.play(-1)
            if m9.is_stop:
                m9.starting()
            if m9.is_pause:
                m9.unpause()

    if x9 == 1:
        if m9.is_playing:
            s9.stop()
            m9.pauseing()
            x9 -=1
    if m9.is_playing:
        x9 += 1
        
def but10():
    global x10
    if x10 == 0:
        if m10.is_stop or m10.is_pause:
            s10.play(-1)
            if m10.is_stop:
                m10.starting()
            if m10.is_pause:
                m10.unpause()

    if x10 == 1:
        if m10.is_playing:
            s10.stop()
            m10.pauseing()
            x10 -=1
    if m10.is_playing:
        x10 += 1
        
def but11():
    global x11
    if x11 == 0:
        if m11.is_stop or m11.is_pause:
            s11.play(-1)
            if m11.is_stop:
                m11.starting()
            if m11.is_pause:
                m11.unpause()

    if x11 == 1:
        if m11.is_playing:
            s11.stop()
            m11.pauseing()
            x11 -=1
    if m11.is_playing:
        x11 += 1
        
def but12():
    global x12
    if x12 == 0:
        if m12.is_stop or m12.is_pause:
            s12.play(-1)
            if m12.is_stop:
                m12.starting()
            if m12.is_pause:
                m12.unpause()

    if x12 == 1:
        if m12.is_playing:
            s12.stop()
            m12.pauseing()
            x12 -=1
    if m12.is_playing:
        x12 += 1
        
def but13():
    global x13
    if x13 == 0:
        if m13.is_stop or m13.is_pause:
            s13.play(-1)
            if m13.is_stop:
                m13.starting()
            if m13.is_pause:
                m13.unpause()

    if x13 == 1:
        if m13.is_playing:
            s13.stop()
            m13.pauseing()
            x13 -=1
    if m13.is_playing:
        x13 += 1
        
def but14():
    global x14
    if x14 == 0:
        if m14.is_stop or m14.is_pause:
            s14.play(-1)
            if m14.is_stop:
                m14.starting()
            if m14.is_pause:
                m14.unpause()

    if x14 == 1:
        if m14.is_playing:
            s14.stop()
            m14.pauseing()
            x14 -=1
    if m14.is_playing:
        x14 += 1
        
def but15():
    global x15
    if x15 == 0:
        if m15.is_stop or m15.is_pause:
            s15.play(-1)
            if m15.is_stop:
                m15.starting()
            if m15.is_pause:
                m15.unpause()

    if x15 == 1:
        if m15.is_playing:
            s15.stop()
            m15.pauseing()
            x15 -=1
    if m15.is_playing:
        x15 += 1
        
def but16():
    global x16
    if x16 == 0:
        if m16.is_stop or m16.is_pause:
            s16.play(-1)
            if m16.is_stop:
                m16.starting()
            if m16.is_pause:
                m16.unpause()

    if x16 == 1:
        if m16.is_playing:
            s16.stop()
            m16.pauseing()
            x16 -=1
    if m16.is_playing:
        x16 += 1
        
def stop():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16

    if m1.is_playing:
        m1.stoping()
        s1.stop()
        x1 -=1
    elif m1.is_pause:
        m1.stopping2()

    if m2.is_playing:
        m2.stoping()
        s2.stop()
        x2 -=1
    elif m2.is_pause:
        m2.stopping2()
    
    if m3.is_playing:
        m3.stoping()
        s3.stop()
        x3 -=1
    elif m3.is_pause:
        m3.stopping2()
    
    if m4.is_playing:
        m4.stoping()
        s4.stop()
        x4 -=1
    elif m4.is_pause:
        m4.stopping2()
        
    if m5.is_playing:
        m5.stoping()
        s5.stop()
        x5 -=1
    elif m5.is_pause:
        m5.stopping2()
        
    if m6.is_playing:
        m6.stoping()
        s6.stop()
        x6 -=1
    elif m6.is_pause:
        m6.stopping2()
        
    if m7.is_playing:
        m7.stoping()
        s7.stop()
        x7 -=1
    elif m7.is_pause:
        m7.stopping2()
        
    if m8.is_playing:
        m8.stoping()
        s8.stop()
        x8 -=1
    elif m8.is_pause:
        m8.stopping2()
        
    if m9.is_playing:
        m9.stoping()
        s9.stop()
        x9 -=1
    elif m9.is_pause:
        m9.stopping2()
        
    if m10.is_playing:
        m10.stoping()
        s10.stop()
        x10 -=1
    elif m10.is_pause:
        m10.stopping2()
        
    if m11.is_playing:
        m11.stoping()
        s11.stop()
        x11 -=1
    elif m11.is_pause:
        m11.stopping2()
        
    if m12.is_playing:
        m12.stoping()
        s12.stop()
        x12 -=1
    elif m12.is_pause:
        m12.stopping2()

    if m13.is_playing:
        m13.stoping()
        s13.stop()
        x13 -=1
    elif m13.is_pause:
        m13.stopping2()

    if m14.is_playing:
        m14.stoping()
        s14.stop()
        x14 -=1
    elif m14.is_pause:
        m14.stopping2()

    if m15.is_playing:
        m15.stoping()
        s15.stop()
        x15 -=1
    elif m15.is_pause:
        m15.stopping2()  

    if m16.is_playing:
        m16.stoping()
        s16.stop()
        x16 -=1
    elif m16.is_pause:
        m16.stopping2()           


canvas1 = tk.Canvas(root, width = 400, height = 600)                                    #creating canvas to place widgets.
canvas1.pack()


b1 = tk.Button(root, text = 'G 128 G', width=10, height=5, command = but1)              #defineing and placeing widget buttons.
b1.pack()

b2 = tk.Button(root, text = 'G 140 D', width=10, height=5, command = but2)
b2.pack()

b3 = tk.Button(root, text = 'G128 F', width=10, height=5, command = but3)
b3.pack()

b4 = tk.Button(root, text = 'G160 D#m', width=10, height=5, command = but4)
b4.pack()

b5 = tk.Button(root, text = 'Brass 140BPM', width=10, height=5, command = but5)
b5.pack()

b6 = tk.Button(root, text = 'brass 150BPM', width=10, height=5, command = but6)
b6.pack()

b7 = tk.Button(root, text = 'brass 150BPM', width=10, height=5, command = but7)
b7.pack()

b8 = tk.Button(root, text = 'brass 180BPM', width=10, height=5, command = but8)
b8.pack()

b9 = tk.Button(root, text = 'string 110 G#m', width=10, height=5, command = but9)
b9.pack()

b10 = tk.Button(root, text = 'string 128 F#m', width=10, height=5, command = but10)
b10.pack()

b11 = tk.Button(root, text = 'string 140 C#m', width=10, height=5, command = but11)
b11.pack()

b12 = tk.Button(root, text = 'string 140 E', width=10, height=5, command = but12)
b12.pack()

b13 = tk.Button(root, text = 'dc 150', width=10, height=5, command = but13)
b13.pack()

b14 = tk.Button(root, text = 'sc128', width=10, height=5, command = but14)
b14.pack()

b15 = tk.Button(root, text = 'trap 128', width=10, height=5, command = but15)
b15.pack()

b16 = tk.Button(root, text = 'trap 150', width=10, height=5, command = but16)
b16.pack()

bs = tk.Button(root, text = 'stop', width=10, height=5, command = stop)
bs.pack()

canvas1.create_window(50, 45, window=b1)                                                #placing buttons at specific location
canvas1.create_window(150, 45, window=b2)
canvas1.create_window(250, 45, window=b3)
canvas1.create_window(350, 45, window=b4)
canvas1.create_window(50, 145, window=b5)
canvas1.create_window(150, 145, window=b6)
canvas1.create_window(250, 145, window=b7)
canvas1.create_window(350, 145, window=b8)
canvas1.create_window(50, 245, window=b9)
canvas1.create_window(150, 245, window=b10)
canvas1.create_window(250, 245, window=b11)
canvas1.create_window(350, 245, window=b12)
canvas1.create_window(50, 345, window=b13)
canvas1.create_window(150, 345, window=b14)
canvas1.create_window(250, 345, window=b15)
canvas1.create_window(350, 345, window=b16)
canvas1.create_window(210, 445, window=bs)


root.mainloop()                                                                         #looping root window
