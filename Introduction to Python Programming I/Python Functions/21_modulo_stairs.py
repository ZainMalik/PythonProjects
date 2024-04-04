import turtle

zain = turtle.Turtle()
zain.width(5)
zain.color("green")

for step in range(5):
    zain.forward(100)
    if(step % 2 == 0):
        zain.left(90)
    else:
        zain.right(90)
    
zain.hideturtle
input()