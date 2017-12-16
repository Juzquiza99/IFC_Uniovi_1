#Tarea 6.1 JAVIER UZQUIZA LOPEZ
#no muestra el error correcto segun el ejemplo

from math import *

eps=1.0e-6 #determinamos el valor por defecto hasta el que se producen las iteraciones

def raizcub(y,x): #definimos la funcion que aplica la formula y nos devuelve su resultado
	ra3 = 1./3*((2*x)+float(y/(x*x)))
	return ra3	

for y in range(1,101): #iniciamos un bucle para calcular las raices hasta el 100
	x=1.0
	while True: #bucle que tiene lugar mientras un valor absoluto sea menor de un numero fijado
		ra3=raizcub(y,x)	
			
		if abs(ra3-x)<eps:		
			error=abs(y**(1./3)-ra3)	
			print ('%3d  %9.8f %9.8e'%(y,ra3,error)) #y lo vamos mostrando por pantalla			
			break
		x=ra3
