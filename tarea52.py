#TAREA 5.2 - JAVIER UZQUIZA LOPEZ

#CALCULO DEL MOMENTO DE INERCIA

print("Este programa se encarga de calcular momentos de inercia de distintos \
objetos: \n -> Varilla (varilla, VARILLA) \n -> Esfera (esfera, ESFERA) \n \
-> Disco (disco, DISCO) \n -> Cilindro (cilindro, CILINDRO) \n")
#se ensenia al usuario las distintas figuras que puede calcular

a=raw_input("Figura geometrica: ") #se pide al usuario que introduzca el nombre
#de la que desea

#*********VARILLA*********

if a==("Varilla") or a==("varilla") or a==("VARILLA"): #distintas opciones con
#las que el usuario accedera a calcular el momento de inercia de una varilla

  print('Se va a calcular el momento de inercia de una varilla')
  print('Introduce los valores que la constituyen: ')
  m1=input('masa (kg): ')
  l1=input('longitud (m): ')
  i1=(1./3)*m1*l1**2
  print("\nEl momento de inercia de una varilla de %2d kg y %2d m es de\
  %2.3f kg*m^2"%(m1,l1,i1))
  #calculamos su valor y lo mostramos por pantalla

#*********ESFERA*********
  
elif a==("Esfera") or a==("esfera") or a==("ESFERA"): #distintas opciones con
#las que el usuario accedera a calcular el momento de inercia de una esfera

  print('Se va a calcular el momento de inercia de una esfera')
  print('Introduce los valores que la constituyen: ')
  m2=input('masa (kg): ')
  r2=input('radio (m): ')
  i2=(2./5)*m2*r2**2
  print("\nEl momento de inercia de una esfera de %2d kg y %2d m es de\
  %2.3f kg*m^2"%(m2,r2,i2))
  #calculamos su valor y lo mostramos por pantalla
  
#*********DISCO*********
  
elif a==("Disco") or a==("disco") or a==("DISCO"): #distintas opciones con
#las que el usuario accedera a calcular el momento de inercia de un disco

  print('Se va a calcular el momento de inercia de un disco')
  print('Introduce los valores que la constituyen: ')
  m3=input('masa (kg): ')
  r3=input('radio (m): ')
  i3=(0.5)*m3*r3**2
  print("\nEl momento de inercia de un disco de %2d kg y %2d m es de\
  %2.3f kg*m^2"%(m3,r3,i3))
  #calculamos su valor y lo mostramos por pantalla
  
#*********CILINDRO*********
  
elif a==("Cilindro") or a==("cilindro") or a==("CILINDRO"): #distintas opciones con
#las que el usuario accedera a calcular el momento de inercia de un disco

  print('Se va a calcular el momento de inercia de un cilindro')
  print('Introduce los valores que la constituyen: \n')
  m4=input('masa (kg): ')
  r4=input('radio (m): ')
  i4=(0.5)*m4*r4**2
  print("\nEl momento de inercia de un cilindro de %2d kg y %2d m es de\
  %2.3f kg*m^2"%(m4,r4,i4))
  #calculamos su valor y lo mostramos por pantalla

else: #en caso de que el usuario no introduzca ninguna de las opciones mostradas
#al principio, se le enseniara este mensaje de error
  print('\nVaya, parece que el objeto que intentas calcular no se encuentra \
  disponible en este programa, prueba con alguno de los 4 que disponemos: \n\
  -> Varilla (varilla, VARILLA) \n  -> Esfera (esfera, ESFERA) \n  -> Disco \
  (disco, DISCO) \n  -> Cilindro (cilindro, CILINDRO) \n')
