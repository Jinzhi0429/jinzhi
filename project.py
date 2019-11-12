from YangFunction import*

turtle.bgcolor("black")

turtle.tracer(False)
bob.width(4)
for times in range(50):
    c=(250-times*5,250-times*5,times*5)
    spikeFlower(4,25-times*2,c)
    bob.left(5)
    bob.forward(5)

turtle.tracer(True)
