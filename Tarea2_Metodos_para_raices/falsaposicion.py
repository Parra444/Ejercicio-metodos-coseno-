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

# Solución de una ecuación f(x)=0 utilizando el método de falsa posición. Al
# finalizar la ejecución del código se imprimen los extremos del intervalo, la aproximación de la raiz,
# el error aproximado porcentual y el número de iteraciones.

# ======================================================================

#Se importa la libreria math para utilizar algunas funciones matemáticas que no trae
#el python base

import math

# ======================================================================
# INGRESO DE INFORMACIÓN
# ======================

#Condicional inicial para que el ejecutable haga el proceso todas las veces que se desee y no se cierre antes de mostrar el resultado
def metodoFalsaPosicion(fun,xa,xb,tolerancia):
    print('---SE USA EL MÉTODO DE FALSA POSICIÓN PARA RESOLVER LA FUNCIÓN f(x) = ', fun) #Se especifica el metodo usado

    #Definimos una función f que nos retorna el valor que tiene al ser evaluada con un valor x
    def f(x):
        return eval(fun) #La funcion eval, me permite pasar la ecuación ingresada por el usuario (que es un string) y evaluarla como una función

    i = 0 #i representará el número de iteraciones
    errorcal = 999999 #representa el error calculado. Se debe inicializar con un número alto para que entre en el ciclo while

    if(f(xa)*f(xb)<=0): #Este condicional global nos sirve para determinar si la función tiene solución en el intervalo ingresado

        while abs(errorcal)>= tolerancia: #Nuestro ciclo se seguirá ejecutando hasta que el error porcentual sea menor que la tolerancia
            f_a=f(xa)
            f_b=f(xb)
            sol= xb-((f_b*(xb-xa))/(f_b-f_a)) #Calculamos el punto x o intersección con el eje x (la raiz aproximada)
            
            i+=1 #Sumamos 1 iteración cada vez que se repita el proceso
            print('Inicio del intervalo: ', xa, ' Final del intervalo: ', xb, ' Raíz aproximada: ', sol, ' Error porcentual: ', errorcal,' # Iteraciones: ', i)
    
            #Hacemos los condicionales para determinar si el siguiente punto va a ser del punto encontrado a la izquierda o del punto encontrado a la derecha
            if(f_a * f(sol))>=0: #Si el producto de f(a)*f(x) es positivo, entonces nuestro nuevo intervalo sera [x,b]
                if(xa==0):
                    errorcal=100
                else:
                    errorcal=float(abs(((sol-xa)/xa)*100))
                xa=sol
            else:#Por el contrario si este producto nos da negativo el nuevo intervalo será [a,x]
                if(xb==0):
                    errorcal=100
                else:
                    errorcal=float(abs(((sol-xb)/xb)*100))
                xb = sol

            if i >= 1000: #Hacemos otra condición para que se cierre el ciclo en caso de que en 1000 iteraciones no encuentre la raiz
                break

        #  Se imprime la raiz aproximada que encontramos
        print('La raiz buscada es: ', sol)
    
    else:
        print('No existe solución en este intervalo')
