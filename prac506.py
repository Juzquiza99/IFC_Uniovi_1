h0=input('Altura inicial: ') #pedimos al usuario que introduzca la 
#altura inicial que desee
inter=input('Numero de intervalos en los que desea dividir la altura: ')
#preguntamos al usuario en cuantos intervalos desea dividir la altura

if h0>0: #condicion para permitir solo valores positivos
  print("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
  #mostramos el cabecero que se situara en la parte de arriba de la tabla
  
  for ht in range(h0,-(h0/inter),-(h0/inter)):#utilizamos un bucle for para que recorra
	#en el intervalo fijado por el usuario anteriormente
	
    th=((h0-ht)/4.9)**0.5 #formula para calcular el tiempo en cada altura
    vt=(9.8*th) #formula para calcular la velocidad en cada altura
    
    print("| %7d    |  %7.3f   |    %7.3f      | "%(ht,th,vt))
    #vamos mostrando los distintos valores que va tomando en cada momento
    #la tabla
  
else: #en caso de que la altura inicial sea negativa (calculo para el pozo)
  print("| Profundidad (m) | Tiempo (s) | Velocidad (m/s) |")
   #mostramos el cabecero que se situara en la parte de arriba de la tabla
  for ht in range(0,-h0-(h0/inter),-(h0/inter)): #bucle a recorrer
    th_=(ht/4.9)**0.5 #calculo del tiempo en cada profundidad
    vt_=(9.8*th_) #calculo de la velocidad en cada profundidad
    print("|    %7d      |  %7.3f   |    %7.3f      | "%(-ht,th_,vt_))
    #vamos mostrando los distintos valores que va tomando en cada momento
    #la tabla
  
  
