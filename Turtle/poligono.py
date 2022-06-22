import turtle
poligono = turtle.Turtle()
 
num_lados = 9
largo_lado = 80
angulo = 360.0 / num_lados
 
for i in range(num_lados):
    poligono.forward(largo_lado)
    poligono.right(angulo)
     
turtle.done()
