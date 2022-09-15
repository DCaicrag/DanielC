import numpy as np

#Se le pide al usuario la dimensión de la matriz, >=3
n = int(input("Introduzca una dimension de matriz mayor o igual a 3:"))
#Se multiplica la dimensión proporcionada por el usuario para hacer la matriz cuadrada,
m = n*n
# M representa la cantidad final de números a los que se va a determinar si son números primos.
M=m*m
# Lista donde se va a guardar los valores de los primeros números primos 
vect = []
#Inicialización del contador para los ciclos for que calcula los números primos
c = 0
# Lista donde se va a guardar los valores de la diagonal superior 
diagsup = []
# El for va desde el 2 hasta un valor final M, que es m al cubo, los suficientes números para llenar la matriz.
#Se realiza el cálculo de los números primos a través del cálculo del módulo (basado en un código de internet) 
for i in range(2,M):
    prim = True
    for j in range(2,i):
        if i == j:
            break
        elif i%j == 0:
            prim = False
        else:
            continue
    if prim == True:
        vect.append(i)
        c += 1 ;
        if c== m:
            break
# Se almacena los datos de los primeros n números primos en el vector
v = np.array(vect)
print(v);

# Se genera una matriz vacia en la cual se va a almacenar los valores del vector
matriz = np.empty((n,n), int)

# Inicialización de contador de posición para el ciclo for que almacena los valores en la matriz 
x = 0
# Ciclo para almacenar los valores en la matriz
for i in range (0,n):
    for j in range (0,n):
        matriz[i][j] = v[x]
        x = x + 1
# Muestra la matriz quitando los corchetes, utilizando str
print(str(matriz).replace(' [', '').replace('[', '').replace(']', ''))

#Lista con los números de la diagonal superior 
for i in range(n):
    for j in range(n):
        if i <= j:
            diagsup.append(matriz[i][j])
#Suma de la diagonal superior 
diagsum = sum(diagsup)
print("Suma de la diagonal superior:", diagsum)

