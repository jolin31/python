import turtle
import PySimpleGUI as sg


c1=turtle.Turtle()
c1.shape("turtle")
c1.color("Red")
c1.speed(1)


def stickman():
    c1.circle(40)
    c1.setheading(270)
    c1.forward(100)
    c1.right(30)
    c1.forward(60)
    c1.left(180)
    c1.forward(60)  
    c1.setheading(270)
    c1.left(30)
    c1.forward(60)
    c1.right(180)
    c1.forward(60)
    c1.setheading(90)
    c1.forward(50)
    c1.setheading(0)
    c1.forward(50)
    c1.setheading(180)
    c1.forward(100) 
    c1.setheading(0)
    c1.forward(50)
    c1.setheading(90)
    c1.forward(50)
    c1.color('white')
    c1.forward(40)
    c1.setheading(180)
    c1.forward(20)
    c1.color('red')
    c1.circle(5)
    c1.setheading(0)
    c1.color('white')
    c1.forward(40)
    c1.setheading(270)
    c1.forward(5)
    c1.color('Red')
    c1.circle(5)
    c1.color('White')
    c1.forward(100)
    

stickman()
k=input("press any key to close")



