import turtle
t = turtle.Pen()
t.speed(0)
x = 0
if x == 100:
    ptint("ok")
else:
    for i in range(50, 150):
        t.forward(i)
        t.left(90)
    x + 1



turtle.done()
