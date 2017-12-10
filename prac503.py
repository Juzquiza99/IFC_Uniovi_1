h0=1000 #Establecemos la altura inicial en 1000m

print("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
#mostramos el cabecero que se situará en la parte de arriba de la tabla

for ht in range(1000,-100,-100):#utilizamos un bucle for para que recorra
	#cada 100m desde la altura inicial 1000m hasta los 0m
  th=((h0-ht)/4.9)**0.5 #formula para calcular el tiempo en cada altura
  vt=(9.8*th) #formula para calcular la velocidad en cada altura
  
  print("|    %4d    |  %7.3f   |      %4d       | "%(ht,th,vt))
  #vamos mostrando los distintos valores que va tomando en cada momento
  #la tabla
