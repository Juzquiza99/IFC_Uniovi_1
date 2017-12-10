from math import *

def nombre_operacion(x): #funcion que queremos realizar, en este caso (cos x)
   return cos(x) #determinamos la funcion a realizar
def finite_diff (f, x, h = 0.0000001):
   '''
   aproxima la primera y segunda derivada
   de f en x; h tiene un valor por defecto 0.0000001
   '''
   fm, f0, fp = f(x-h), f(x), f(x+h)
   df, ddf = (fp-fm)/(2*h), (fp-2*f0+fm)/h**2
   return df, ddf

x = input('Derivada de: ')

df, ddf = finite_diff(nombre_operacion, x)
print('Primera derivada = ', df)
print('Segunda derivada = ', ddf)
                                 
