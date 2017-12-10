#Con este programa buscamos mostrar obtener los multiplos de 3 que
#existen entre un valor minimo y un maximo establecidos por el usuario
#y mostrarlos con signo negativo

n=input("Introduce el valor inicial de la lista: ")
m=input("Introduce el valor final de la lista: ")

orig=range (n,(m+1)) #creamos la primera lista
otro=orig[:] #hacemos una replica de la lista anterior

for a in range(len(orig)):
   if otro[a]%3==0:
      otro[a]=-otro[a]

print('|  orden  | original | modificada |') #mostramos cabecera de tabla

for a, b in enumerate(orig):
	print('| %4d -> |   %4d   |   %5d    |'%(a,b,otro[a]) )
