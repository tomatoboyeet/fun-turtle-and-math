#setting up the map
from turtle import * #we need turtle to draw and make the game
from time import sleep #adds one cool feature
shape('turtle') #defines the shape of the turtle
mappy=Turtle() #i define mappy as turtle (mappy draws the map)
penup()#i tell the main turtle to lift the pen to not draw its path
FONT=("Arial", 30, "bold")#we define the font for the "you have lost"
mappy.penup()#to move the mappy to the place it maps without marks
mappy.hideturtle()#hides mappy so we wont see him
mappy.speed('fastest')#we tell it to be fast
mappy.goto(200,200)#we tell it to go to the place it draws
mappy.pendown()#we allow it to draw
for i in range(0,4):#loops 4 times
    mappy.forward(200)#moves farward, forming the cube lines
    mappy.left(90)#turns left, forming the cube shape
#movement
def forwardd():#if ill name it forward, it will refer to the command forward(x).
    for i in range(0,10):forward(1)#i slow it down using a for loop.
    if xcor()>200 and xcor()<400 and ycor()>200 and ycor()<400:#if its in a specific area, do the next things.
        write('you have lost. try again.', font=FONT)#write "you have lost. try again." on the screen.
        sleep(3)#wait 3 seconds.
        bye()#close the turtle.
def leftt():#again, left(x) is an existing command.
    for i in range(0,10):left(1)#we slow it down again to move left slower
def backwardd():#backward(x) is a command
    for i in range(0,10):backward(1)#slows down the movement
    if xcor()>200 and xcor()<400 and ycor()>200 and ycor()<400:#if in specific area do the next things.
        write('you have lost. try again.',font=FONT)#write "you have lost. try again." on the screen
        sleep(3)#wait 3 seconds.
        bye()#close the turtle.
def rightt():#right(x) is a command.
    for i in range(0,10):right(1)#slows down moving right.
#control
onkey(forwardd,'w')#when w is pressed, perform forwardd.
onkey(backwardd,'s')#when s is pressed, perform backwardd.
onkey(rightt,'d')#when d is pressed, perform rightt.
onkey(leftt,'a')#when a is pressed, perform leftt.
listen()#listen to the keys pressed.
