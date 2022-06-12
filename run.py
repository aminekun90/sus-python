from asyncio.log import logger
import turtle
import time

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title("SUS")
    wn.bgcolor('skyblue')
    wn.setup(width=100, height=100)
for i in range(10000000):
    turtle.penup()
    turtle.setpos(-30, 0)
    turtle.pendown()
    turtle.color("red")
    turtle.write("SUS", move=True, align="left", font=("serif", 18))
    time.sleep(0.5)
    turtle.penup()
    turtle.setpos(-30, 0)
    turtle.pendown()
    turtle.color("green")
    turtle.write("SUS", move=True, align="left", font=("serif", 18))
    time.sleep(0.5)
    turtle.penup()
    turtle.setpos(-30, 0)
    turtle.pendown()
    turtle.color("blue")
    turtle.write("SUS", move=True, align="left", font=("serif", 18))
    time.sleep(0.5)
while True:
    try:
        wn.update()
    except turtle.Terminator:
        logger.log("App Terminated")
