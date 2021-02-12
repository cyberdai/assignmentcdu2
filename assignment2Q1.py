import turtle
import random
import time
from turtle import Turtle 
from random import randint


#set the background color and window title
wn = turtle.Screen()
wn.title("Project Assignment 2 Q1 Drawing")
wn.bgcolor('skyblue')
wn.bgcolor('green')

#create turtle
trt_l=turtle.Turtle()
trt_l.speed(6)
trt_l.shape("turtle")

# Drawing of Sky
trt_l.penup()
trt_l.goto(-650, -100)
trt_l.pendown()
trt_l.fillcolor("deepskyblue")
trt_l.begin_fill()
for i in range(2):
    trt_l.forward(1279)
    trt_l.left(90)
    trt_l.forward(500)
    trt_l.left(90)
trt_l.end_fill()

# Drawing of Sun
trt_l.penup()
trt_l.goto(-230,180)
trt_l.fillcolor("yellow")
trt_l.pendown()
trt_l.begin_fill()
trt_l.circle(30)
trt_l.end_fill()

# Drawing of sun rays
def Draw_Rays(t, length, radius):
   for i in range(4):
      t.penup()
      t.forward(radius)
      t.pendown()
      t.forward(length)
      t.penup()
      t.backward(length + radius)
      t.left(90)
trt_l.penup()
trt_l.goto(-230, 210)
trt_l.pendown()
Draw_Rays(trt_l, 29, 30)
trt_l.right(45)
Draw_Rays(trt_l, 19, 30)
trt_l.left(45)

# Drawing of Cloud
def Draw_Cloud():
    trt_l.penup()
    trt_l.goto(200, 200)
    trt_l.pendown()
    trt_l.color("white")
    trt_l.begin_fill()
    for i in range(1):
        trt_l.circle(25)
        trt_l.penup()
        trt_l.goto(220,240)
        trt_l.pendown()
        trt_l.circle(25)
        trt_l.penup()
        trt_l.goto(240,225)
        trt_l.pendown()
        trt_l.circle(25)
        trt_l.penup()
        trt_l.goto(180,230)
        trt_l.pendown()
        trt_l.circle(25)
        trt_l.penup()
        trt_l.goto(190,190)
        trt_l.pendown()
        trt_l.circle(25)
        trt_l.penup()
        trt_l.goto(220,196)
        trt_l.pendown()       
    trt_l.end_fill()
Draw_Cloud()


# Drawing of House
def Draw_House():
    trt_l.penup()
    trt_l.goto(-130, -100)
    trt_l.pendown()
    trt_l.pensize(3)
    trt_l.color("chocolate", "orange")
    trt_l.begin_fill()
    for i in range(4):
        trt_l.forward(210)
        trt_l.left(90)
    trt_l.end_fill()
Draw_House()

# Drawing of Chimney
def Draw_Chimney():
    trt_l.penup()
    trt_l.goto(-127, 130)
    trt_l.pendown()
    trt_l.color("brown", "firebrick")
    trt_l.begin_fill()
    for i in range(2):
        trt_l.forward(30)
        trt_l.left(90)
        trt_l.forward(100)
        trt_l.left(90)
    trt_l.end_fill()
Draw_Chimney()

# Drawing of Roof
def Draw_Roof():
    trt_l.penup()
    trt_l.goto(-158, 100)
    trt_l.pendown()
    trt_l.begin_fill()
    for i in range(3):
        trt_l.forward(268)
        trt_l.left(120)
    trt_l.end_fill()
Draw_Roof()

# Drawing of Window 1
def Draw_Window1():
    trt_l.penup()
    trt_l.goto(10, 0)
    trt_l.pendown()
    trt_l.color("black", "white")
    trt_l.begin_fill()
    for i in range(4):
        trt_l.forward(50)
        trt_l.left(90)
    trt_l.end_fill()
Draw_Window1()
# Drawing of Window 1 Cross - Horizontal Line 
trt_l.penup()
trt_l.goto(10, 25)
trt_l.pendown()
trt_l.color("black")
trt_l.forward(50)

# Drawing of Window 1 Cross - Vertical Line 
trt_l.penup()
trt_l.goto(35,0)
trt_l.pendown()
trt_l.left(90)
trt_l.forward(50)

# Drawing of Window 2
def Draw_Window2():
    trt_l.penup()
    trt_l.goto(-110, 0)
    trt_l.pendown()
    trt_l.right(90)
    trt_l.color("black", "white")
    trt_l.begin_fill()
    for i in range(4):
        trt_l.forward(50)
        trt_l.left(90)
    trt_l.end_fill()
Draw_Window2()

# Drawing of Window 2 Cross - Horizontal Line 
trt_l.penup()
trt_l.goto(-110, 25)
trt_l.pendown()
trt_l.color("black")
trt_l.forward(50)

# Drawing of Window 2 Cross - Vertical Line 
trt_l.penup()
trt_l.goto(-85, 0)
trt_l.pendown()
trt_l.left(90)
trt_l.forward(50)

# Drawing of Door
def Draw_Door():
    trt_l.penup()
    trt_l.goto(-50, -97)
    trt_l.pendown()
    trt_l.right(90)
    trt_l.color("red")
    trt_l.begin_fill()
    for i in range(2):
        trt_l.forward(50)
        trt_l.left(90)
        trt_l.forward(80)
        trt_l.left(90)
    trt_l.end_fill()
Draw_Door()

# Drawin of Door Handle
trt_l.penup()
trt_l.goto(-40, -60)
trt_l.pendown()
trt_l.color("black")
trt_l.begin_fill()
trt_l.circle(5)
trt_l.end_fill()

# Drawing of tree
trt_l.penup()
trt_l.goto(-220, -35)
trt_l.pendown()
def Draw_Tree(Len_Branch,trtl):
    ## Move forward, backward, turn left, turn right with length
    if Len_Branch > 5:
        trt_l.forward(Len_Branch)
        trt_l.right(20)
        ## Recursively calling tree function
        Draw_Tree(Len_Branch-15,trt_l)
        trt_l.left(40)
        
        Draw_Tree(Len_Branch-15,trt_l)
        trt_l.right(20)
        trt_l.backward(Len_Branch)

def main():
    trt_l.left(90)
    trt_l.up()
    trt_l.backward(100)
    trt_l.down()
    trt_l.color("green")
    Draw_Tree(75,trt_l)
main()

# Drawing of car
# Drawing of car wheel 1
trt_l.penup()
trt_l.goto(180, -79)
trt_l.color("brown","black")
trt_l.pendown()
trt_l.begin_fill()
trt_l.circle(20)
trt_l.end_fill()

#Drawing of the car wheel 2
trt_l.penup()
trt_l.goto(270, -79)
trt_l.color("brown","black")
trt_l.pendown()
trt_l.begin_fill()
trt_l.circle(20)
trt_l.end_fill()

# Drawing of body part
trt_l.penup()
trt_l.goto(270,-74)
trt_l.pendown()
trt_l.begin_fill()
trt_l.right(90)
trt_l.forward(39)
trt_l.left(90)
trt_l.forward(35)
trt_l.left(90)
trt_l.forward(55)
trt_l.right(60)
trt_l.forward(60)
trt_l.left(60)
trt_l.forward(60)
trt_l.left(60)
trt_l.forward(60)
trt_l.left(120)
trt_l.forward(60)
trt_l.left(90)
trt_l.forward(53)
trt_l.backward(53)
trt_l.right(90)
trt_l.forward(90)
trt_l.backward(195)
trt_l.right(90)
trt_l.forward(35)
trt_l.left(90)
trt_l.forward(215)
trt_l.fillcolor("tan")
trt_l.end_fill()
wn.mainloop()
