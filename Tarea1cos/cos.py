import math

#Ingresar el angulo a calcular
vlr=int(input('Ingrese el valor de coseno que desea calcular... '))
#Ingrasar el numero de sucesiones
n=int(input('Ingrese el número de sucesiones que desea (Máximo 80 sucesiones)... '))

#Convertimos a radianes
vlr=(vlr*math.pi)/180
coseno=0
pot=0

#Se realiza la sucesión
for i in range (0,n):
      coseno+=((vlr**pot)/(math.factorial(pot)))
      coseno=coseno*(-1)
      round(coseno,5)
      pot=pot+2

vlrexacto=math.cos(vlr)

if (n%2!=0):
    coseno=coseno*(-1)
    errorporcentual=((vlrexacto-coseno)/vlrexacto)*100
    if(errorporcentual>=0):
        print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')
    else:
        errorporcentual=errorporcentual*(-1)
        print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')
    
else:
    errorporcentual=((vlrexacto-coseno)/vlrexacto)*100
    print('El resultado es... '+ str(coseno) +'\ncon un error porcentual de... '+str(errorporcentual)+'%')



