from turtle import *
from time import sleep
from keyboard import *
shape('circle')
penup()
speed('fastest')
def check():
    pass
def rightt():
    forward(2)
def backwardd():
    goto(xcor(),ycor()-2)
def leftt():
    backward(2)
def forwardd():
    goto(xcor(),ycor()+2)
while True:
    if is_pressed('w'):forwardd()
    if is_pressed('s'):backwardd()
    if is_pressed('d'):rightt()
    if is_pressed('a'):leftt()
