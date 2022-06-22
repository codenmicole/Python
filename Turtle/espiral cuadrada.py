import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Espiral cuadrada")
rh = turtle.Turtle()
rh.color("pink")
 
def sqrfunc(size):
    for i in range(4):
        rh.fd(size)
        rh.left(90)
        size = size-5
 
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
