# a = 5
# b = 6
# c = 7

a = float(input('Ingrese el primer lado: '))
b = float(input('Ingrese el segundo lado: '))
c = float(input('Ingrese el tercer lado: '))

# semi perimetro
s = (a + b + c) / 2

# formula de heron
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('El area del triangulo es %0.2f' %area)
