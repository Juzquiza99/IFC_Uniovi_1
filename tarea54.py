#TAREA 5.4. - JAVIER UZQUIZA LOPEZ   

#LANZAMIENTO VERTICAL

y0=input('Altura inicial: ') #Pedimos la altura y la velocidad inicial
v0=input('Velocidad inicial: ')
y=y0 #Calculamos la altura en cada punto a partir de la inicial
t=0
t0=int(2*v0/9.8)

#Mostramos la tabla hasta la altura del lanzamiento
print('\n-> Calculo hasta la altura del lanzamiento \n')
print('| Tiempo (s) | Altura (m) |')
objeto=open('posiciones.dat','w') #Creamos el fichero
objeto.write('| Tiempo (s) | Altura (m) |\n')

for t in range(0,t0+1): #Iniciamos un bucle desde 0 hasta el momento en el que el cuerpo esta en la inicial
  
  y=y0+v0*t-4.9*t**2 #Calculo de la altura
  print('| %7.2f    |  %7.2f   |'%(t,y)) #Lo mostramos en forma de tabla
  objeto.write('| %7.2f    |  %7.2f   |\n'%(str(t),str(y)))
  
print('| %7.2f    |  %7.2f   |\n'%(t0,y0)) #Mostramos los valores de tiempo y posicion en el momento del choque
objeto.write('| %7.2f    |  %7.2f   |\n'%(str(t0),str(y)))

#Mostramos la tabla hasta el suelo
print('-> Calculo hasta la altura del suelo \n')
print('| Tiempo (s) | Altura (m) |')
objeto.write('| Tiempo (s) | Altura (m) |\n')
t=0 #Volvemos a iniciar el tiempo a 0 para que nos vuelva a mostrar todos los valores

while True: #Bucle para que se lleve a cabo siempre teniendo en cuenta al break
  y=y0+v0*t-4.9*t**2
  if y<=0: #si la altura es menor que la inicial
    t=(-v0-(v0**2+2*y0*9.8)**0.5)/(-9.8)
    y=y0+v0*t-4.9*t**2
    print('| %7.2f    |  %7.2f   |'%(t, y))
    objeto.write('| %7.2f    |  %7.2f   |\n'%(str(t),str(y)))
    break #se para el bucle cuando deja de cumplirse la condicion del if
  
  #Mientras el objeto esta por encima de la inicial
  print('| %7.2f    |  %7.2f   |'%(t, y))
  objeto.write('| %7.2f    |  %7.2f   |\n'%(str(t),str(y)))
  t+=1 
  
objeto.close()
