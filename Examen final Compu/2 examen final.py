import math

# Función a evaluar con el método numérico
def f(x,y):
   
    f = 1+(y**2)
    
    return f

 #Condiciones de k1 hasta k3 y k general del sistema, fórmula iterativa ("y") del método de Runge Kutta.
def rk(x, y, h):    
    k1 = h*f(x, y)
    k2 = h*f(x+(h/2), y+(k1/2))
    k3 = h*f(x+(h/2), y+(k2/2))
    k4 = h*f(x+h, y+k3)

    k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    y = y+k
    return y

#Condiciones iniciales, paso de interación y punto en cual evaluar la función.
def main():
    x0 = float(input("Introduzca condicion inicial x0:  "))
    y0 = float(input("Introduzca condicion inicial y0:  "))
    xf = float(input("Introduzca punto de evaluación x: "))
    h =  float(input("Introduzca paso de iteración h:   "))
    while x0 <= xf:
        
    
        print("x:\t\t", "%.2f" % x0)
        print("y("+"%.2f" % x0+"):\t", "%.5f" % y0)
        y0 = rk(x0, y0, h)
        x0 = x0+h
    print("x:\t\t", "%.2f" % x0)
    print("y("+"%.2f" % x0+"):\t", "%.9f" % y0)

main()



