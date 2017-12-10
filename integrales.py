#INTEGRALES DEFINIDAS

from math import *


a = input('a: ') #Pedimos por teclado los límites de la integracion
b = input('b: ')

def nombre_operacion(x): #funcion que queremos realizar, en este caso (sin(x))
  return (sin(x)) #determinamos la funcion a realizar
  
def integral(f,a,b):
  '''
  calculamos la integral de forma aproximada
  '''
  
  inte=((b-a)/2)*(f(a)+f(b))
  return inte #nos devuelve el valor calculado
	
inte=integral(nombre_operacion,a,b) #establecemos el valor que han de tomar f, a y b

print("La integral definida entre %4.2f y %4.2f de sin(x) es: %7f"%(a,b,inte)) #Mostramos por pantalla el resultado
