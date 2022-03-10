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

# Solución de una ecuación f(x)=0 utilizando el método de bisección. Al
# finalizar la ejecución del código se imprimen los extremos del intervalo, la aproximación de la raiz,
# el error aproximado porcentual y el número de iteraciones.

# ======================================================================

#Se importa la libreria math, numpy y matplotlib para utilizar algunas funciones matemáticas que no trae
#el python base
import math
import matplotlib.pyplot as plt
import numpy as np

#Definimos la función metodoBiseccion que recibe como parametros la funcion, los extremos izquierdo y derecho del intervalo y la tolerancia maxima

def metodoBiseccion(fun, xa, xb, tolerancia):
    print('\n\n---SE USA EL MÉTODO DE BISECCIÓN PARA RESOLVER LA FUNCION : ',fun) #Se especifica el metodo usado
    
    #Definimos una función f que nos retorna el valor que tiene al ser evaluada con un valor x
    def f(x):
        return eval(fun)
    i = 0 #i representará el número de iteraciones
    errorcal = 999999 #representa la función evaluada en el punto medio (c). Se debe inicializar con un número alto para que entre en el ciclo while
    vectorIteraciones=list() #Vector para guardar las iteraciones para la gráfica
    vectorErrores=list()#Vector para guardar el valor de los errores para la gráfica
    vectorGlobal=list() #Vector global que contendrá los vectores de las iteraciones y los errores

    if(f(xa)*f(xb)<=0): #Este condicional global nos sirve para determinar si la función tiene solución en el intervalo ingresado

        while abs(errorcal)>= tolerancia: #Nuestro ciclo se seguirá ejecutando hasta que el error porcentual sea menor que la tolerancia
    
            puntoMedio= (xa + xb)/2 #Calculamos el punto medio
            f_a = f(xa) #Evaluamos en el extremo izquierdo de la raiz
            f_b = f(xb) #Evaluamos en el extremo derecho de la raiz
            fc = f(puntoMedio) #Evaluamos en el punto medio
            
            
            i+=1 #Sumamos 1 iteración cada vez que se repita el proceso

            #==============SALIDA DE DATOS=================

            print('Inicio del intervalo: ', xa, ' Final del intervalo: ', xb, ' Raíz aproximada: ', puntoMedio, ' Error porcentual: ', errorcal,'%',' # Iteraciones: ', i)
            
            #Hacemos los condicionales para determinar si el siguiente punto va a ser del punto medio a la izquierda o del punto medio a la derecha
            if(f_a * fc)<0: #Si el producto de f(a)*f(c) es negativo, entonces nuestro nuevo intervalo sera [a,c]
                if(xb==0):#Condicional para que si existen intervalos iguales inversos, la división por cero se omita
                    errorcal=100
                else:#Se calcula el error porcentual cuando la solución está dada por el extremo xb
                    errorcal=float(abs(((puntoMedio-xb)/xb)*100))
                xb=puntoMedio
            elif (f_b * fc)<0:#Si el producto de f(b)*f(c) es negativo, entonces nuestro nuevo intervalo sera [b,c]
                if(xa==0):#Condicional para que si existen intervalos iguales inversos, la división por cero se omita
                    errorcal=100
                else:#Se calcula el error porcentual cuando la solución está dada por el extremo xa
                    errorcal=float(abs(((puntoMedio-xa)/xa)*100))
                xa = puntoMedio
            vectorErrores.append(errorcal)#Luego de terminar el proceso se acumula el valor del error en un vector
            vectorIteraciones.append(i)#Luego de terminar el proceso se acumula la iteracion en un vector
            if i >= 1000: #Hacemos otra condición para que se cierre el ciclo en caso de que en 1000 iteraciones no encuentre la raiz
                break

        #  Se imprime la raiz aproximada que encontramos
        print('La raiz buscada es: ', puntoMedio)
        vectorGlobal=vectorIteraciones+vectorErrores#Se crea un vector general que contiene el vector con el número de iteraciones y los valores de los errores
        return np.array(vectorGlobal)#Se devuelve el vector general
    else:
        print('No existe solución en este intervalo')
