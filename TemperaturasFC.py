#EJERCICIO 5.2.6
 #BUCLE WHILE
 
min=input('Temperatura minima?: ') #temperatura minima
#si queremos fijarla en algun valor en particular min=...
max=input('Temperatura maxima?: ') #temperatura maxima
#si queremos fijarla en algun valor en particular max=...

A=[] #creamos la lista A vacia
C=[]

while min<=max: #bucle con iteracion de 5 en 5
   far=min*9./5 + 32 #calculamos el valor en farhenheit
   C.append(min) #aniadimos los valores a la lista C
   A.append(far) #aniadimos los valores a la lista A
   min+=5

print('')
print("Los valores en Celsius son: ")
print (C)
print("Los valores en Farenheit son: ")
print (A)
print('')
print("| Celsius | Farenheit |")
print("|---------|-----------|")

for i in range(len(A)):
  print("|  %4d   |    %4.1f   |"%(C[i],A[i]))


# # # # # # # # # # # # # # # # # # #

 #BUCLE FOR
 
print('')
tmin=input('Temperatura minima?: ') #introducimos temp min
tmax=input('Temperatura maxima?: ') #introducimos temp max

B=[] #creamos lista B vacia
D=[]

for x in range(tmin,tmax+1,5): #bucle desde la minima a la maxima cada 5
   t=x*9./5 + 32 #calculamos el valor en farhenheit
   D.append(x) #aniadimos los valores a la lista D
   B.append(t) #aniadimos los valores a la lista B
   
#mostramos los resultados obtenidos
print('')
print("Los valores en Celsius son: ")
print (D)
print("Los valores en Farenheit son: ")   
print (B) #mostramos los valores de la lista B
print('')
print("| Celsius | Farenheit |")
print("|---------|-----------|")
for i in range(len(D)):
  print("|  %4d   |    %4.1f   |"%(D[i],B[i]))
