import math

def f(x):
#Función a evaluar con el método: sin (1/x)
    f = math.sin((1/x)) 
    
    return f

def simpson38(a,b):
    # paso de iteración con los límites inferior y superior
    h = (b-a)/3
    #Fórmula de Simpson 3/8
    I = (3*(h/8))*(f(a) + (3*f(a+h)) + (3*f(a+(2*h))) + f(b))
    return I



def main():
    #límite inferior (0.159154)
    a = 1/(2*math.pi)
    #límite superior (2)
    b = float(input("Introduzca límite superior de integración: "))
    #llamado a la fórmula de Simpson 3/8
    I = simpson38(a,b)
    print("Valor de la integración numérica por Simpson 3/8: \t",I)
   

main()

