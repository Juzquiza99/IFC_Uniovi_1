#TAREA 5.3. - JAVIER UZQUIZA LOPEZ   

#SUCESION DE FIBONACCI

n=input('Orden de la sucesion de Fibonacci: ') #pedimos al usuario que indique el orden
#hasta el que quiere llevar la sucesion

num=1 #prefijamos el valor de la suma de la tercera posicion de la serie
a=0 #primer valor de la serie
b=0 #segundo valor de la serie

print('0') #mostramos por pantalla los dos primeros valores de la serie
print('1')

for x in range(0,n): #bucle que se repite las veces que el usuario establezca
#mediante el orden de la sucesion
  a=b #la primera posicion toma el valor de la segunda en la anterior repeticion del bucle
  b=num #la segunda posicion toma el valor de la tercera en la anterior repeticion del bucle
  num=a+b #la tercera posicion es el resultado de la suma de las dos anteriores
  
  print(num) #mostramos cada vez el valor de la tercera posicion (suma de las dos anteriores)


#De esta manera, tras una repeticion del bucle, el valor de a es 0, el valor de b es el de num
#inicial, por tanto 1, y num, que es la suma de a y b es 1. La siguiente repeticion, a sera la
#antigua b(1), y b sera el antiguo valor de num(1); así pues, num sera en este caso 2. Y asi
#sucesivamente, el numero de repeticiones qu el usuario desee.
