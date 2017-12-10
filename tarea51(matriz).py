#TAREA 5.1 - JAVIER UZQUIZA LOPEZ 

#MATRIZ DE DIMENSION DE N

n=input('Orden de la matriz cuadrada: ') #Pedimos la usuario el orden de la matriz
a=range(n) #Creamos una lista con n posiciones
b=a[:] #Copiamos la lista anterior
pares=[] #Creamos una lista para almacenar los numeros pares
impares=a[:] #Creamos una lista para almacenar los numeros impares
for i in range(n): #Con este bucle establecemos que la lista vaya del 1 al 20
  b[i]+=1
for i in range(n):
  a[i]=b[:] #Introducimos cada lista b en cada una de las posiciones de la lista a
  impares[i]=b[:] #Modificamos los valores de las distintas posiciones de la lista
  #que transformara en 0 los impares
  for g in range(n):
     impares[i][g]+=(n*i)
     a[i][g]+=(n*i) #Segun las columnas vayan aumentando, iran aumentando en "n"
     #unidades, en ambas listas
     if a[i][g]%2==0: #solo se aniadiran aquellas posiciones pares de la matriz
		  pares.append(a[i][g])
print ('\n \nLos numeros pares son: \n \n%s'%pares) #Mostraremos por pantalla
#los numeros pares

for i in range(n): #En este caso, el bucle busca sustituir los numeros impares por 0
	for g in range(n):
	 if impares[i][g]%2!=0: 
	   impares[i][g]=0
    
print ('\n\nConvirtiendo los impares en cero: \n \n%s'%impares)	#Los mostraremos
#por pantalla

#Buscamos mostrar las distintas posiciones con forma de matriz
matriz='' #Utilizamos para ello distintos caracteres
for i in range(n):
   matriz += "|"
   for g in range(n):
      matriz+=(" %3d "%impares[i][g]) #Vamos estableciendo los distintos valores
      #con el formato deseado
   matriz +="|\n"
print ("\n  \nEn forma de matriz: \n")
print matriz #los mostramos por pantalla
