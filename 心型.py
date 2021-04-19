import turtle

t = turtle.Turtle()

def curvemove():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.color('red', 'pink')
t.begin_fill()
t.left(140)
t.forward(111.65)
curvemove()
t.left(120)
curvemove()
t.forward(111.65)
t.end_fill()
turtle.done()
