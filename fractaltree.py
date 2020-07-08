import turtle as tu
wn=tu.Screen()
wn.bgcolor("red")
wn.title("Fractal Tree")

t = tu.Turtle()
t.left(90)
t.speed(0)

def draw(len):
    if len<10:
        return
    else:
        t.forward(len)
        t.left(30)
        draw(3*len/4)
        t.right(60)
        draw(3*len/4)
        t.left(30)
        t.backward(len)

draw(100)

tu.mainloop()
