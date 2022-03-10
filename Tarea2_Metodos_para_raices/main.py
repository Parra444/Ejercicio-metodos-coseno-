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

# Con el siguiente codigo se busca la raiz de una funcion de la forma f(x)=0
# por medio de dos métodos cerrados (Bisección y falsa posición) y un 
# método abierto (Newton Raphson)

# ======================================================================

#Importación de librerias
#Para que funcione el código se debe instalar las librerias de pip y matplot
#introduciendo los siguientes comandos en el cmd:
#python -m pip install -U pip
#python -m pip install -U matplotlib

#También, debe instalar la libreria numpy con el siguiente comando en el cmd:
#pip install numpy

import matplotlib.pyplot as plt
import numpy as np
import math
import biseccion
import falsaposicion
import newton
import puntoExtremo

#OBSERVACIONES:
#Para ingresar funciones se debe usar la sintaxis del lenguaje, por ejemplo
#- Funciones exponenciales: math.exp(), y dentro del paréntesis irá a lo que está elevada la función
#- Funciones trigonométricas: math.sen(), math.cos(), math.tan()
#- Para elevar cualquier variable a un número se usa el doble asterisco, ejemplo x**2

while True: #Ciclo principal para que se sigan pidiendo los datos y no se cierre el ejecutable

    # ----------- INGRESO DE DATOS ---------------------

    ax=plt.subplot() #Se crea el area en la que estará puesta la gráfica final
    fun=input('Ingrese la funcion a evaluar: ')#Se ingresa la funcion a evaluar
    derf=input('Ingrese su derivada: ')#Se ingresa la derivada de la funcion a evaluar
    x_i=float(input('Ingrese la aproximacion inicial: '))#Acá se ingresa la aproximación inicial para el metodo abierto
    xa= float(input('Ingrese el valor inicial del intervalo: ')) #Acá se ingresa el extremo izquierdo del intervalo
    xb= float(input('Ingrese el valor final del intervalo: '))#Acá se ingresa el extremo derecho del intervalo
    tolerancia = float(input('Ingrese la tolerancia: '))#Acá se ingresa la tolerancia

    #----------- INFORMACIÓN DE SALIDA ------------------

    ##Se llaman a los subprogramas de los métodos para encontrar las raíces de las funciones,
    ##llevando como parámetros la función, los extremos de los intervalos y la tolerancia para los metodos cerrados
    ##y la función, su derivada, la aproximación inicial y la tolerancia máxima para el método abierto.
    ##Estos subprogramas guardan los datos de las iteraciones y los errores porcentuales en un vector para luego
    ##graficarlos.
    vectorBiseccion=biseccion.metodoBiseccion(fun,xa,xb,tolerancia) 
    vectorFalsaposicion=falsaposicion.metodoFalsaPosicion(fun,xa,xb,tolerancia)
    vectorNewton=newton.MetodoNewtonRaphson(fun,derf,x_i,tolerancia)

    ##Los vectores que nos devolvieron los subprogramas son divididos en 2, que corresponden a nuestros
    ##ejes X y Y.
    BiseccionEjeX, BiseccionEjeY=np.split(vectorBiseccion,2)
    FalsaPosicionEjeX, FalsaPosicionEjeY=np.split(vectorFalsaposicion,2)
    NewtonEjeX, NewtonEjeY=np.split(vectorNewton,2)

    ##Se grafican los vectores y se les asignan nombres a cada gráfica
    ax.plot(NewtonEjeX,NewtonEjeY, label='Newton-Raphson')
    ax.plot(FalsaPosicionEjeX,FalsaPosicionEjeY,label='Falsa Posición')
    ax.plot(BiseccionEjeX,BiseccionEjeY, label='Bisección')

    ##Se estiliza la gráfica con los titulos de los ejes, el titulo general y la escala
    plt.title('Comparación errores relativos porcentuales')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Error porcentual')
    plt.ylim(10**-5,10**2)
    plt.ticklabel_format(axis='y',style='scientific', scilimits=(0,0), useMathText=True)
    plt.legend()
    plt.show()

    

    #================================================================================
    #================SI SE DESEA CALCULAR EL PUNTO EXTREMO DEL PUNTO 3===============
    #==================QUITELE LOS COMENTARIOS A LAS LINEAS 92,93 Y 94===============
    #=================Y COMENTE DESDE LA LINEA 47 HASTA LA LINEA 84 =================
    #fex=input('Ingrese la funcion a la que le desea encontrar el punto maximo: ')
    #dv=input('Ingrese la derivada: ')
    #puntoExtremo.hallarPuntoMaximo(fex,dv)
    

    #Condicional para cerrar el ciclo while del principio
    if(1==99999999):
        break

