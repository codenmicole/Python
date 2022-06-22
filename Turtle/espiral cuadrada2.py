import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
rh = turtle.Turtle()
rh.color("blue")
 
def sqrfunc(size):
    for i in range(4):
        rh.fd(size)
        rh.left(90)
        size = size + 5
 
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
