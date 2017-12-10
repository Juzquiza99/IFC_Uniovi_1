#Este programa se encarga de resolver ecuaciones de segundo grado
#Tanto con discriminantes positivos y negativos (mediante complejos)

#En primer lugar definimos las variables que nos van a pedir por teclado
#introducir los distintos valores que forman la ecuacion
a=input("Introduce el valor de a (x^2): ")
b=input("Introduce el valor de b(x): ")
c=input("Introduce el valor de c: ")

#Con el condicional diferenciamos quien quiera resolver la ecuacion de
#primer o segundo grado
if a!=0: #en este caso es de segundo grado
  d=b**2-4*a*c #calculamos el discriminante
  print("El valor del discriminante es: "+str(d))
  #mostramos el valor del discriminante (NO NECESARIO)

  print("Las raices de la ecuacion son: ")

  if d==0: #En el caso de que el discriminante sea 0
	  d_0=(-b/2*a) #Calculamos asi el resultado unico de la ecuacion
	  print("x=" +str(d_0)) #y lo mostramos
     	
  elif d > 0: #En el caso de que el discriminante sea positivo
		d_pos=(-b+(d**0.5)/2*a) #Calculamos la raiz con discriminante 
		#positivo
		d_neg=(-b-(d**0.5)/2*a) #Calculamos la raiz con discriminante
		#negativo
		print("x=" +str(d_pos)) #y los mostramos
		print("x=" +str(d_neg))
	
  else: #En el caso de que el discriminante sea negativo (complejos)
		comp_pos=((-b/2*a)+1j*((-d)**0.5)/2*a) #Calculamos para el complejo positivo
		print("x=" +str(comp_pos)) #y lo mostramos
		comp_neg=((-b/2*a)-1j*((-d)**0.5)/2*a) ##Calculamos para el complejo negativo
		print("x=" +str(comp_neg)) #y lo mostramos

else: #En el caso de que se quiera resolver una ecuacion de primer grado (a=0)
  e=(c/b) #Calculamos el valor de x
  print("Este programa calcula ecuaciones de segundo grado, sin embargo,\
  el resultado de esta ecuacion de primer grado es: ")
  print("x= "+str(e)) #y lo mostramos
