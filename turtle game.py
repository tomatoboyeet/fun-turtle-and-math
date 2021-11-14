from turtle import *#imports are essential for this to work
from os import system
try:from keyboard import is_pressed#we try importing it.
except:
    system('pip install keyboard')#if it wont work, it will install it.
    from keyboard import is_pressed#now we import it.
"""note: no one has keyboard unless they downloaded it, which is what we did now"""
shape('circle')#we set the shape to circle
#add here another turtle by stating x=Turtle(), and than make it draw a shape in the spot that makes you lose.
penup()#we tell it not to draw
def check():#check if we reach specific position (add here whatever you want)
    if xcor()>1000000000 and xcor()<1000000000000:bye()#if its between 1000000000 and 1000000000000 x, close turtle.
def rightt():#move right
    forward(2)#the movement
    check()#perform check for location
def backwardd():#go back
    goto(xcor(),ycor()-2)#go -2 in the y, and stay x same.
    check()#check location
def leftt():#move left
    backward(2)#move
    check()#check location
def forwardd():#forward
    goto(xcor(),ycor()+2)#move 2 more y, and same x.
    check()#check for location
while True:#infinite loop
    if is_pressed('w'):forwardd()#if you press w, move up.
    if is_pressed('s'):backwardd()#if you press s, move down.
    if is_pressed('d'):rightt()#if you press d, move right.
    if is_pressed('a'):leftt()#if you press a, move left.
