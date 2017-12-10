h0=input('Altura inicial: ') #pedimos al usuario que introduzca la 
#altura inicial que desee
inter=input('Numero de intervalos en los que desea dividir la altura: ')
#preguntamos al usuario en cuantos intervalos desea dividir la altura

if h0>0: #condicion para permitir solo valores positivos
  print("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
  #mostramos el cabecero que se situará en la parte de arriba de la tabla
  
  for ht in range(h0,0,-(h0/inter)):#utilizamos un bucle for para que
	#recorra en el intervalo fijado por el usuario anteriormente
	
    th=((h0-ht)/4.9)**0.5 #formula para calcular el tiempo en cada altura
    vt=(9.8*th) #formula para calcular la velocidad en cada altura
    
    print("| %7d    |  %7.3f   |    %7.3f      | "%(ht,th,vt))
    #vamos mostrando los distintos valores que va tomando en cada momento
    #la tabla
  
  #para que siempre muestre el valor en el suelo, sin importar el numero
  #de intervalos
  #ni la altura inicial, aniadimos de forma externa el valor para
  #la altura 0 m
  t0=((h0)/4.9)**0.5 #formula para calcular el tiempo a la altura del suelo
  v0=(9.8*th) #formula para calcular la velocidad en cada altura
  print("| %7d    |  %7.3f   |    %7.3f      | "%(0,t0,v0))
  
else:
  print("Has de introducir un valor de altura positivo")
  #recordamos al usuario que en el caso de que haya introducido un valor
  #de altura inicial negativo, o 0, a de ser positivo
