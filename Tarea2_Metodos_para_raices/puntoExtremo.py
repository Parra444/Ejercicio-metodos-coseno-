# Febrero 25/2022

# ======================================================================
# Jesus Jair Parra Jimenez
# CC 1.232.589.523
# Métodos Numéricos (506)
# ======================================================================
# ======================================================================
# DESCRIPCIÓN DE LA TAREA
# =======================

# TAREA NÚMERO 2: Búsqueda de raíces de una ecuación

# Se usa el método de Newton-Raphson para encontrar la raiz de la derivada de una funcion
# y de esta manera poder determinar el punto maximo global de la misma

# ======================================================================

#Se importa la libreria math, matplotlib,numpy para utilizar algunas funciones matemáticas que no trae
#el python base
import matplotlib.pyplot as plt
import math
import numpy as np

#Definimos la funcion para hallar el punto maximo que recibe como parametros la funcion y su derivada
def hallarPuntoMaximo(fex, derf):
    def f(x):#Creamos una funcion para evaluar los puntos en la funcion a la que le queremos encontrar el punto max
            return eval(fex)
    def MetodoNewtonRaphson(dv): #Método de Newton, usa la función a la cual se le quiere buscar la raiz, que en este caso es la derivada
        #Definimos una función f que nos retorna el valor que tiene al ser evaluada con un valor x
        def f(x):
            return eval(dv)#La funcion eval, me permite pasar la ecuación ingresada por el usuario (que es un string) y evaluarla como una función entendible para el lenguaje

        #Esta función retornará el valor de la derivada al ser evaluada en x
        def df(x):
            return -(60*(x**4))-(6*(x**2))#La funcion eval, me permite pasar la ecuación ingresada por el usuario (que es un string) y evaluarla como una función entendible para el lenguaje
        
        
        errorcal= 99999 #representa el error calculado. Se debe inicializar con un número alto para que entre en el ciclo while
        i=0 #i es una variable para el numero de iteraciones
        x_i=1#Se define la aproximacion lineal en 1
        while abs(errorcal)>=0.001: #Nuestro ciclo se seguirá ejecutando hasta que el error porcentual sea menor que la tolerancia
            if df(x_i)==0: #Condición para comprobar si la derivada de la función inicial es igual 0, en caso tal de ser cierto, retornará nada, pues la división por 0 es indefinida y se saldrá de la ejecución del código.
                print("No es posible dividir por 0, solución no encontrada")
                return None
            x_r= x_i -(f(x_i))/(df(x_i)) #Fórmula del método de Newton para encontrar la aproximación de la raíz
            errorcal= abs(((x_r-x_i)/x_i)*100) #Fórmula para encontrar el error relativo porcentual con valor absoluto.
            i+= 1 #Se suma una iteración

            
            x_i = x_r #El punto inicial tomará el valor del punto inicial+1 y el contador sumará 1 por cada paso que se haga.
            

        return x_r
    
    raiz=MetodoNewtonRaphson(derf)
    print('El punto máximo global es, aproximadamente el punto: P(',raiz,',',f(raiz),')')