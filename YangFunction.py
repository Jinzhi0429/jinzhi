import turtle
turtle.colormode(255)
bob=turtle.Turtle()
bob.speed(0)

def tile(c):
    polygon(4,400,c)
    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)
        
        
def triangle(distance):
    sides=3
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(sides)

def square(distance):
    sides=4
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

def pentagon(distance):
    sides=5
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

def polygon(sides,distance,c):
    bob.color( c )
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    for times in range(8):
        bob.left(30)
        bob.penup()
        bob.goto(x,y)
        bob.pendown()

def star(distance,c):
    bob.color( c )
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color( c )
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,size,color):
    bob.begin_fill()
    bob.color(color)
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()

def monster(color):
    bob.color(color)
    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(35)
    bob.left(135)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.end_fill()

def fadingTriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,times*5)
        polygon(3,450-times*4,c)
        
def rowtile(c):
    for times in range(4):
        bob.forward(distance)
        bob.left(90)

def spike(distance):
    for times in range(20):
        c=times*12
        bob.color(c,c,c)
        bob.forward(distance)
        bob.left(10)
        
def spikeFlower(angle,distance,c):
    bob.color( c )
    for times in range(5):
        spike(distance)
        bob.pendown()
        bob.left(angle)
