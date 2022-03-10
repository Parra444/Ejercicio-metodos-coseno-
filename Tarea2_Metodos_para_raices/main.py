import math
import biseccion
import falsaposicion
import newton

while True:
    fun=input('Ingrese la funcion a evaluar: ')#Se ingresa la funcion a evaluar
    derf=input('Ingrese su derivada: ')#Se ingresa la derivada de la funcion a evaluar
    x_i=float(input('Ingrese la aproximacion inicial: '))#Acá se ingresa la aproximación inicial para el metodo abierto
    xa= float(input('Ingrese el valor inicial del intervalo: ')) #Acá se ingresa el extremo izquierdo del intervalo
    xb= float(input('Ingrese el valor final del intervalo: '))#Acá se ingresa el extremo derecho del intervalo
    tolerancia = float(input('Ingrese la tolerancia: '))#Acá se ingresa la tolerancia

    newton.MetodoNewtonRaphson(fun,derf,x_i,tolerancia)
    biseccion.metodoBiseccion(fun,xa,xb,tolerancia)
    falsaposicion.metodoFalsaPosicion(fun,xa,xb,tolerancia)
    if(x_i==99999999):
        break

