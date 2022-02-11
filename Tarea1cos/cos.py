import math
#Se abre un loop while para que se repita el proceso las veces que se desee.
while True:

#Ingresar el angulo a calcular
    vlr=int(input('Ingrese el valor de coseno que desea calcular... '))
#Ingrasar el numero de sucesiones
    n=int(input('Ingrese el número de sucesiones que desea (Máximo 80 sucesiones)... '))

#Convertimos el valor del angulo a radianes e inicializamos variables
    vlr=(vlr*math.pi)/180
    coseno=0
    pot=0

#Se realiza la sucesión y se pasa el resultado a negativo para que haya una sucesion de sumas y restas
    for i in range (0,n):
        coseno+=((vlr**pot)/(math.factorial(pot)))
        coseno=coseno*(-1)
        pot=pot+2

#Se calcula el valor exacto del coseno
    vlrexacto=math.cos(vlr)

#Se hacen condicionales porque cuando el numero de sucesiones es impar, el resultado da con signo contrario
#entonces se realiza la multiplicacion por -1 para que quede correctamente y se calcula el error porcentual
    if (n%2!=0):
        coseno=coseno*(-1)
        errorporcentual=((vlrexacto-coseno)/vlrexacto)*100
        
    #Condicional por si el error porcentual es negativo
        if(errorporcentual>=0):
            print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')
        else:
            errorporcentual=errorporcentual*(-1)
            print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')
    
    else:
        errorporcentual=((vlrexacto-coseno)/vlrexacto)*100
        print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')
    
#Se cierra el loop while
    if (n>=80):
        break


