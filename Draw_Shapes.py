import turtle
import PySimpleGUI as sg

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

def draw(c):
    if c=='Square':
        square()
    elif c=='Circle':
        circle()


def square():
    c1.setheading(0)
    c1.forward(20)
    c1.setheading(90)
    c1.forward(20)
    c1.setheading(180)
    c1.forward(20)
    c1.setheading(270)
    c1.forward(20)
    c1.setheading(0)
    c1.forward(20)

def circle():
    c1.circle(20)

question =input("What you want to draw? (Square,Triangle,Circle)")
c1=turtle.Turtle()
c1.shape("turtle")
c1.color("Red")
c1.speed(1)
draw(question)

""" question =input("What you want to draw? (Square,Triangle,Circle)")
if question.upper()=='SQUARE':
    c1=turtle.Turtle()
    c1.shape("turtle")
    c1.color("Red")
    c1.speed(1)
    square()
elif question.upper()=='CIRCLE':
    c1=turtle.Turtle()
    c1.shape("turtle")
    c1.color("Red")
    c1.speed(1)

    circle()
else:
    print("Chose the right shape") """

k=input("press any key to close.")
