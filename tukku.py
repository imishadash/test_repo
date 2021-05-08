#!/usr/bin/python3
import turtle
import sys, tty, termios
s = turtle.getscreen()
t = turtle.Turtle()
t.circle(100)

t.forward(100) # draw base
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# first triangle -- by tukku
t.forward(100) # draw base
t.left(120)
t.forward(100)
 
t.left(120)
t.forward(100)
 
t.penup()
t.right(150)
t.forward(50)
 
# second triangle for star
t.pendown()
t.right(90)
t.forward(100)
 
t.right(120)
t.forward(100)
 
t.right(120)
t.forward(100)

ch = sys.stdin.read(1)
