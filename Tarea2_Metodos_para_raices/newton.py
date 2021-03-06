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

# Solución de una ecuación f(x)=0 utilizando el método de Newton-Raphson. Al
# finalizar la ejecución del código se imprimen la aproximación inicial, la aproximación de la raiz,
# el error aproximado porcentual y el número de iteraciones.

# ======================================================================

#Se importa la libreria math, matplotlib,numpy para utilizar algunas funciones matemáticas que no trae
#el python base
import matplotlib.pyplot as plt
import math
import numpy as np

def MetodoNewtonRaphson(fun, derf,x_i, tol): #Método de Newton, usa la función a la cual se le quiere buscar la raiz, la aproximacion inicial y la tolerancia
    print('\n\n---SE USA EL MÉTODO DE NEWTON-RAPHSON PARA RESOLVER LA FUNCIÓN f(x) = ', fun)
    #Definimos una función f que nos retorna el valor que tiene al ser evaluada con un valor x
    def f(x):
        return eval(fun)#La funcion eval, me permite pasar la ecuación ingresada por el usuario (que es un string) y evaluarla como una función entendible para el lenguaje

    #Esta función retornará el valor de la derivada al ser evaluada en x
    def df(x):
        return eval(derf)#La funcion eval, me permite pasar la ecuación ingresada por el usuario (que es un string) y evaluarla como una función entendible para el lenguaje
    
    
    errorcal= 99999 #representa el error calculado. Se debe inicializar con un número alto para que entre en el ciclo while
    i=0 #i es una variable para el numero de iteraciones
    vectorIteraciones=list() #Vector para guardar las iteraciones para la gráfica
    vectorErrores=list()#Vector para guardar el valor de los errores para la gráfica
    vectorGlobal=list() #Vector global que contendrá los vectores de las iteraciones y los errores

    while abs(errorcal)>=tol: #Nuestro ciclo se seguirá ejecutando hasta que el error porcentual sea menor que la tolerancia
        if df(x_i)==0: #Condición para comprobar si la derivada de la función inicial es igual 0, en caso tal de ser cierto, retornará nada, pues la división por 0 es indefinida y se saldrá de la ejecución del código.
            print("No es posible dividir por 0, solución no encontrada")
            return None
        x_r= x_i -(f(x_i))/(df(x_i)) #Fórmula del método de Newton para encontrar la aproximación de la raíz
        errorcal= abs(((x_r-x_i)/x_i)*100) #Fórmula para encontrar el error relativo porcentual con valor absoluto.
        i+= 1 #Se suma una iteración

        #=================SALIDA DE DATOS================

        print('Aproximación: ', x_i,' Raíz aproximada: ', x_r, ' Error porcentual: ', errorcal,' # Iteraciones: ', i) #Esto imprimirá la cantidad de iteraciones, pasos y errores relativos porcentuales.
        
        x_i = x_r #El punto inicial tomará el valor del punto inicial+1 y el contador sumará 1 por cada paso que se haga.
        
        vectorErrores.append(errorcal) #Luego de terminar el proceso se acumula el valor del error en un vector
        vectorIteraciones.append(i) #Luego de terminar el proceso se acumula la iteracion en un vector

    #Imprime la raiz aproximada encontrada        
    print('La raíz buscada es: ', x_r)
    vectorGlobal=vectorIteraciones+vectorErrores#Se guardan los vectores en el vector global
    return np.array(vectorGlobal)#Se retorna el vector general