h0=1000 #Establecemos la altura inicial en 1000m

for ht in range(1000,-100,-100):#utilizamos un bucle for para que recorra
	#cada 100m desde la altura inicial 1000m hasta los 0m
	
  th=((h0-ht)/4.9)**0.5 #formula para calcular el tiempo en cada altura
  vt=(9.8*th) #formula para calcular la velocidad en cada altura
  
  print("Altura: %4d m"%(ht)) #mostramos por pantalla los distintos
  print("Tiempo: %4.3f s"%(th)) #resultados para cada momento
  print("Velocidad: %4d m/s"%(vt))
  print('')
