import turtle

screen = turtle.Screen()

turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(670, 670)

screen.title("Infinite loop")
size = 0

while True:
    for i in range(5):
        turtle.fd(size+1)
        turtle.left(90)
        size -= 5
    size+=1