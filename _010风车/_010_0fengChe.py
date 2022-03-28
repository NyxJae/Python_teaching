import turtle as t

t.bgcolor("lightBlue")

t.color("gray")
t.pensize(20)
t.right(90)
t.forward(150)
t.backward(150)

t.color("black")
t.pensize(1)
t.fillcolor("pink")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
    t.circle(50, 180)
t.end_fill()
t.dot(20)
t.hideturtle()

t.done()
