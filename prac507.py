h0=input('Altura inicial: ') #pedimos al usuario que introduzca la 
#altura inicial que desee

a=open('altheight.dat', 'r') #abrimos el fichero externo con las alturas
b=open('result.txt', 'w') #creamos el fichero donde se almacenaran los
#datos obtenidos con este programa

b.write('Altura inicial %4d.1f\n'%h0) #aniadimos al fichero el valor de
#la altura inicial, tal y como pide el enunciado

if h0>0: #condicion para permitir solo valores positivos
	print("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
	#mostramos el cabecero que se situara en la parte de arriba de la tabla
	b.write("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
  
	for i in range(a.readlines()): #obtenemos los datos mediante el fichero
	#referido como a
		i+=1 #iteracion dentro de los datos introducidos (cada 1)
		ht=float(i[0:len(i)+1])	#obtenemos cada valor originario del fichero	
		th=((h0-ht)/4.9)**0.5 #formula para calcular el tiempo en cada altura
		vt=(9.8*th) #formula para calcular la velocidad en cada altura
		
		print("| %7.1f    |  %7.3f   |    %7.3f      | "%(ht,th,vt))
		b.write("| %7.1f    |  %7.3f   |    %7.3f      |\n"%(ht,th,vt))
		#vamos mostrando los distintos valores que va tomando en cada momento
		#la tabla y los añadimos al fichero según van apareciendo
  
else: #en caso de que la altura inicial sea negativa (calculo para el pozo)
	print("| Profundidad (m) | Tiempo (s) | Velocidad (m/s) |")
	b.write("| Altura (m) | Tiempo (s) | Velocidad (m/s) |")
	#mostramos el cabecero que se situara en la parte de arriba de la tabla
	#y se lo aniadimos al nuevo fichero
	
	for i in range(a.readlines()): #bucle a recorrer
		i+=1
		ht=float(i[0:len(i)+1)])
		th_=(ht/4.9)**0.5 #calculo del tiempo en cada profundidad
		vt_=(9.8*th_) #calculo de la velocidad en cada profundidad
		print("|    %7d.1f      |  %7.3f   |    %7.3f      | "%(ht,th_,vt_))
		b.write("|    %7d.1f      |  %7.3f   |    %7.3f      | "%(ht,th_,vt_))
		#vamos mostrando los distintos valores que va tomando en cada momento
		#la tabla
	
	a.close()
	b.close()
	#cerramos ambos ficheros
  
