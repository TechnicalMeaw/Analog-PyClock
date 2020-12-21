import turtle
import time

# setting up the screen
root = turtle.Screen()
root.title("Analog Clock")
root.bgcolor("black")
root.setup(width= 550, height= 550)
root.tracer(0)

#setting up the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

# drawing the clock
def draw_clock(pen):
    pen.up()
    pen.pensize(4)
    pen.goto(0, 250)
    pen.setheading(180)
    pen.color("cyan")
    pen.down()
    pen.circle(250)
    pen.up()
    pen.setheading(90)

    # drawing the digit bars
    pen.goto(0,0)
    for _ in range(12):
        pen.pensize(4)
        pen.color("red")
        pen.fd(230)
        pen.down()
        pen.fd(17)
        pen.up()
        pen.goto(0,0)
        pen.color("#648a1d")
        pen.pensize(3)
        for i in range(4):
            pen.rt(6)
            pen.fd(238)
            pen.down()
            pen.fd(9)
            pen.up()
            pen.goto(0,0)
        pen.rt(6)

    # current time
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    # drawing the H bar
    pen.up()
    pen.color("#d18e08")
    pen.pensize(5)
    pen.goto(0,0)
    pen.setheading(90)
    pen.rt((h /12 * 360) + (m/60 *30))
    pen.bk(20)
    pen.down()
    pen.fd(200)
    


    # drawing the M bar
    pen.up()
    pen.color("green")
    pen.pensize(3)
    pen.goto(0,0)
    pen.setheading(90)
    pen.rt((m /60 * 360) + (s/60 *6))
    pen.bk(35)
    pen.down()
    pen.fd(265)

    # drawing the s bar
    pen.up()
    pen.color("white")
    pen.pensize(1)
    pen.goto(0,0)
    pen.setheading(90)
    pen.rt((s/60) *360)
    pen.bk(60)
    pen.down()
    pen.fd(230)


    # mid circle
    pen.up()
    pen.pensize(8)
    pen.color("gray")
    pen.setheading(180)
    pen.goto(0,4)
    pen.down()
    pen.circle(4)
    pen.up()





while True:
    draw_clock(pen)
    root.update()
    time.sleep(0.25)
    pen.clear()


root.mainloop()