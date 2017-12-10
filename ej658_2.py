def f(x,y):
   x=x+3
   y.append(23)
   print('dentro de f', x, y)

x=22
y=[22]
f(x,y)
print('fuera de f', x, y)



def y_max(v0):
   '''
   Esta funcion calcula la altura maxima alcanzada en un \
   lanzamiento vertical hacia arriba
   '''
   return v0**2/(2*9.81)

velocidad = input('velocidad inicial? ')
print('Para una velocidad inicial de \t %5.2fm/s' % velocidad)
print('la altura maxima alcanzada es \t: %5.2fm ' % y_max(velocidad))
