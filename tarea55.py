#tarea 5.5 JAVIER UZQUIZA LOPEZ (colaboracion con ALEX PANERA ALVAREZ)

from math import *

f=open('cuerpos.txt', 'r') #abrimos y leemos el fichero donde se encuentran los datos
lectura=f.read().splitlines() #lo separamos en las distintas lineas de texto
#y lo metemos dentro de la lista lectura
f.close() #cerramos el fichero

del lectura[:3] #eliminamos las tres primeras lineas de datos

#Creamos todas listas vacias que vamos a usar a lo largo del programa
esfera=[]
cilindro=[]
parale=[]
densesfera=[]
diaesfera=[]
denscilindro=[]
radiocilindro=[]
alturacilindro=[]
densparale=[]
aparale=[]
bparale=[]
cparale=[]
volesflist=[]
volcilist=[]
volparalelist=[]

#recorremos la lista para ir separandola mediante comas
for i in range(len(lectura)):
	lectura[i]=lectura[i].split(',')
	for e in range(len(lectura[i])):
		lectura[i][e]=float(lectura[i][e])
		
	#en funcion del numero de datos de cada fila de datos lo clasificamos
	#para las distintas figuras
	if len(lectura[i])==2:
		esfera.append(lectura[i])			
			
	elif len(lectura[i])==3:
		cilindro.append(lectura[i])
					
	elif len(lectura[i])==4:
		parale.append(lectura[i])		

#Creamos las listas donde separamos cada uno de los datos que se nos ofrecen de cada figura

for i in range (len(esfera)): #metemos en distintas listas los datos de la esfera
	densesfera.append(esfera[i][0])
	diaesfera.append(esfera[i][1])
	
for i in range (len(cilindro)): #metemos en distintas listas los datos del cilindro
	denscilindro.append(cilindro[i][0])
	radiocilindro.append(cilindro[i][1])
	alturacilindro.append(cilindro[i][2])
	
for i in range (len(parale)): #metemos en distintas listas los datos del paralelepipedo
	densparale.append(parale[i][0])
	aparale.append(parale[i][1])
	bparale.append(parale[i][2])
	cparale.append(parale[i][3])
	
	

#             ESFERA

#calculo de los volumenes de la esfera

for i in range(len(esfera)): #recorremos la lista de esfera
	volesf=(4./3)*pi*(diaesfera[i]/2)**3 #calculamos el volumen de cada esfera
	volesflist.append(volesf) #se lo aniadimos a la lista volesf

totdensesfera=sum(densesfera) #sumamos todos los valores de la densidad
findensesfera=totdensesfera/len(esfera) #hacemos la media de densidades
totvolesfera=sum(volesflist) #sumamos todos los valores de volumen
masaesfera=findensesfera*totvolesfera #calculamos el valor de la masa total de las esferas

#Lo mostramos por pantalla
print('             ESFERA\n')
print('Densidad media: %1.6f kg*m**-3'%(findensesfera))
print('Volumen total: %5.4f m**3'%(totvolesfera))
print('Masa total: %6.4f kg\n\n'%(masaesfera))


#            CILINDRO

#calculo de los volumenes del cilindro (de igual forma que en la esfera)

for i in range(len(cilindro)):
	volcilindro=pi*radiocilindro[i]**2*alturacilindro[i]
	volcilist.append(volcilindro)

totdenscilindro=sum(denscilindro) #sumamos la densidad total
findenscilindro=totdenscilindro/len(cilindro) #hallamos la media de la densidad
totvolcilindro=sum(volcilist) #sumamos los valores del volumen
masacilindro=findenscilindro*totvolcilindro #calculamos la masa total de los cilindros

#Lo mostramos por pantalla
print('             CILINDRO\n')
print('Densidad media: %1.6f kg*m**-3'%(findenscilindro))
print('Volumen total: %5.4f m**3'%(totvolcilindro))
print('Masa total: %6.4f kg\n\n'%(masacilindro))


#           PARALELEPIPEDO

#calculo de los volumenes de los paralelepipedos (de igual forma que los dos anteriores)

for i in range(len(parale)):
	volparale=aparale[i]*bparale[i]*cparale[i]
	volparalelist.append(volparale)
	
totdensparale=sum(densparale) #sumamos la densidad total
findensparale=totdensparale/len(parale) #hallamos la media de la densidad
totvolparale=sum(volparalelist) #sumamos los valores del volumen
masaparale=findensparale*totvolparale #calculamos la masa total de los paralelepipedos

#Lo mostramos por pantalla
print('            PARALELEPIPEDO\n')
print('Densidad media: %1.6f kg*m**-3'%(findensparale))
print('Volumen total: %5.4f m**3'%(totvolparale))
print('Masa total: %6.4f kg\n\n'%(masaparale))
