import logging
import turtle
import time
logging.basicConfig(filename='logs/app.log',
                    encoding='utf-8', level=logging.INFO)
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title("SUS")
    wn.bgcolor('skyblue')
    wn.setup(width=200, height=100)
try:
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
        wn.update()
except turtle.Terminator:
    logging.info(msg="App Terminated")
