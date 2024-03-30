import turtle
import random

def screenLeftClick(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)
    
def screenRightClick(x,y):
    turtle.penup()
    turtel.goto(x,y)

def screenmIdClick(x,y):
    global r,g,b
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()

pSize=10
r,g,b=0.0,0.0,0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenLeftClick,2)
turtle.onscreenclick(screenLeftClick,3)


turtle.done()
