import random
import time
import turtle
from turtle import *

window=turtle.Screen()
window.title("Turtle Race!")

turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-150,160)
turtle.write("Turtle Race Game!",font=("Arial",25,"bold","underline"))

#Finish Line(White):
turtle.shape("square")
turtle.shapesize(1)
turtle.penup()

xcoordinate=150
ycoordinate=60
turtle.color("white")

while ycoordinate!=-210:
   turtle.setpos(xcoordinate,ycoordinate)
   turtle.stamp()
   ycoordinate-=30

#Red Line
turtle.penup()
xcoordinate2=180
ycoordinate2=30

while ycoordinate2!=-180:
    turtle.color("red")
    turtle.setpos(xcoordinate2,ycoordinate2)
    turtle.stamp()
    ycoordinate2-=30

turtle.hideturtle()

#TURTLES//
#Turtle1
turtle1=Turtle()
turtle1.speed(0)
turtle1.color("Blue")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-200,25)
turtle1.pendown()

#Turtle2
turtle2=Turtle()
turtle2.speed(0)
turtle2.color("DeepPink")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-200,-25)
turtle2.pendown()

#Turtle3
turtle3=Turtle()
turtle3.speed(0)
turtle3.color("Gold")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-200,-75)
turtle3.pendown()

#Turtle4
turtle4=Turtle()
turtle4.speed(0)
turtle4.color("Lavender")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-200,-120)
turtle4.pendown()

time.sleep(2) #Pause game before starting!

#Making turtles move!
random_int=random.randint(1,7)
for i in range(1,120):
    turtle1.forward(random.randint(1,random_int))
    turtle2.forward(random.randint(1,random_int))
    turtle3.forward(random.randint(1,random_int))
    turtle4.forward(random.randint(1,random_int))












turtle.mainloop()
