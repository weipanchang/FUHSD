#!/usr/bin/env python
import time
from turtle import *
def square(length):
    for i in range(4):
        fd(length)
        rt(90)

def retangle(x,y):
    fd(x)
    rt(90)
    fd(y)
    rt(90)
    fd(x)
    rt(90)
    fd(y)
    rt(90)

def door(lx, ly, turn, x, y):
    penup()
    goto(lx,ly)
    pendown()
    rt(turn)
    retangle(x,y)
    
        
rt(180)
square(100)
rt(90)
square(100)
rt(180)
square(100)
rt(270)
square(100)

door(-100,50,0,5,25)
#penup()
#goto(-100, 50)
#pendown()
#retangle(5, 25)
door(100,50,0,-5,25)
#penup()
#goto(100, 50)
#pendown()
#rt(180)
#retangle(5, -25)
door(-100,-50,0,5,-25)
#penup()
#goto(-100, -50)
#pendown()
#rt(180)
#retangle(5, -25)
door(100,-50,180,5,25)
#penup()
#goto(100, -50)
#pendown()
#rt(180)
#retangle(5, 25)

time.sleep(10)
