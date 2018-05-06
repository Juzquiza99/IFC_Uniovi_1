#TRABAJO ALEX PANERA Y JAVIER UZQUIZA
#coding:utf-8
from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Yp=linspace(1,0,1000) #Creamos un array de mil posiciones que vaya desde 1 a 0

#Definimos la función 'fun' donde se encuentran las ecuaciones diferenciales que integraremos con odeint
def fun(CXNe,Y,k1,k2):#comentar variacion de k1 y k2 respecto de los valores 
	C , X , Ne =CXNe[0], CXNe[1], CXNe[2] 
	dt=-1/((3*Y**2)+k1*Y*C+k2*Y*X)
	dC=-(Y-k1*C)/(3*Y+k1*C+k2*X)
	dX=-(k1*C-k2*X)/(3*Y+k1*C+k2*X)
	dNe=-(k2*X)/(3*Y+k1*C+k2*X)
	return dt, dC, dX, dNe

#Función para pintar las gráficas de la primera figura	
def prin1(n,tit):
	plt.subplot(2,2,n)
	plt.plot(Yp,t[:,1], label='Carbono')
	plt.plot(Yp,t[:,2],label=u'Oxígeno')
	plt.plot(Yp,t[:,3],label=u'Neón')
	plt.title(tit)
	plt.xlabel(u'Concentración de He')
	plt.ylabel(u'Concentración')
	plt.legend()
	


#print (t[-1,1]+t[-1,2]+t[-1,3])
#---------------------Concentraciones del resto vs conc de He
print(u'Gráfica que muestra como varían las concentraciones según la concentración\n de Helio')
t=odeint(fun,[0,0,0,0],Yp,(0.6,0.5))
prin1(1,'K1=0.5 K2=0.6')

t=odeint(fun,[0,0,0,0],Yp,(1.,1.))
prin1(2,'K1=1 K2=1')

t=odeint(fun,[0,0,0,0],Yp,(0.2,0.7))
prin1(3,'K1=0.2 K2=0.7')	

t=odeint(fun,[0,0,0,0],Yp,(1.5,0.8))
prin1(4,'K1=1.5 K2=0.8')	
print t
plt.show()


#-------------------- conc de los elementos vs tiempo

#Función para pintar las gráficas de la segunda figura	
def prin2(n,tit):
	plt.subplot(2,2,n)
	plt.plot(t[:,0],Yp,label='Helio')
	plt.plot(t[:,0],t[:,1], label='Carbono')
	plt.plot(t[:,0],t[:,2],label=u'Oxígeno')
	plt.plot(t[:,0],t[:,3],label=u'Neón')
	plt.title(tit)
	plt.xlabel('Tiempo')
	plt.ylabel(u'Concentración')
	plt.legend()
print(u'Gráficas que muestran como varían las concentraciones según el tiempo')
t=odeint(fun,[0,0,0,0],Yp,(0.6,0.5))
prin2(1,'K1=0.5 K2=0.6')

t=odeint(fun,[0,0,0,0],Yp,(1.,1.))
prin2(2,'K1=1 K2=1')

t=odeint(fun,[0,0,0,0],Yp,(0.2,0.7))
prin2(3,'K1=0.2 K2=0.7')	

t=odeint(fun,[0,0,0,0],Yp,(1.5,0.8))
prin2(4,'K1=1.5 K2=0.8')	
	
plt.show()

#Mostramos la gráfica que representa la disminución del Helio
#------------------------Helio
plt.plot(t[:,0],Yp,label='Helio')
plt.title(u'Concentración de Helio')
plt.xlabel('Tiempo')
plt.ylabel(u'Concentración de He')
plt.legend()
plt.show()

#------------------------------------------------------------

#Función que nos permite pintar gráficas similares de diferentes variables
def prin3(n,c,lab,tit,ylab):
	plt.subplot(2,2,n)
	plt.plot(t[:,0],t[:,c], label=lab)
	plt.title(tit)
	plt.xlabel('Tiempo')
	plt.ylabel(ylab)
	plt.legend()

#------------------------Carbono
t=odeint(fun,[0,0,0,0],Yp,(0.6,0.5))
prin3(1,1,u'Carbono','K1=0.5 K2=0.6', u'Concentración de C')
t=odeint(fun,[0,0,0,0],Yp,(1.,1.))
prin3(2,1,u'Carbono','K1=1 K2=1', u'Concentración de C')
t=odeint(fun,[0,0,0,0],Yp,(0.2,0.7))
prin3(3,1,u'Carbono','K1=0.2 K2=0.7', u'Concentración de C')
t=odeint(fun,[0,0,0,0],Yp,(1.5,0.8))
prin3(4,1,u'Carbono','K1=1.5 K2=0.8', u'Concentración de C')

plt.show()

#--------------------Oxigeno
t=odeint(fun,[0,0,0,0],Yp,(0.6,0.5))
prin3(1,2,u'Oxígeno','K1=0.5 K2=0.6', u'Concentración de O')
t=odeint(fun,[0,0,0,0],Yp,(1.,1.))
prin3(2,2,u'Oxígeno','K1=1 K2=1', u'Concentración de O')
t=odeint(fun,[0,0,0,0],Yp,(0.2,0.7))
prin3(3,2,u'Oxígeno','K1=0.2 K2=0.7', u'Concentración de O')
t=odeint(fun,[0,0,0,0],Yp,(1.5,0.8))
prin3(4,2,u'Oxígeno','K1=1.5 K2=0.8', u'Concentración de O')

plt.show()

#------------------Neon

t=odeint(fun,[0,0,0,0],Yp,(0.6,0.5))
prin3(1,3,u'Neón','K1=0.5 K2=0.6', u'Concentración de Ne')
t=odeint(fun,[0,0,0,0],Yp,(1.,1.))
prin3(2,3,u'Neón','K1=1 K2=1', u'Concentración de Ne')
t=odeint(fun,[0,0,0,0],Yp,(0.2,0.7))
prin3(3,3,u'Neón','K1=0.2 K2=0.7', u'Concentración de Ne')
t=odeint(fun,[0,0,0,0],Yp,(1.5,0.8))
prin3(4,3,u'Neón','K1=1.5 K2=0.8', u'Concentración de Ne')

plt.show()
#----------------------------------------------------------------

#Vamos a probar a continuación añadiendo valores iniciales a las
#concentraciones de los distintos gases
#0,1 de cada gas

t=odeint(fun,[0,0.1,0.1,0.1],Yp,(0.6,0.5))
prin2(1,'K1=0.5 K2=0.6')

t=odeint(fun,[0,0.1,0.1,0.1],Yp,(1.,1.))
prin2(2,'K1=1 K2=1')

t=odeint(fun,[0,0.1,0.1,0.1],Yp,(0.2,0.7))
prin2(3,'K1=0.2 K2=0.7')	

t=odeint(fun,[0,0.1,0.1,0.1],Yp,(1.5,0.8))
prin2(4,'K1=1.5 K2=0.8')	
	
plt.show()

#PARTE DE VISUAL


from visual import *

#Configuramos la pantalla que mostrará nuestra representación
escena=display(title="Concentraciones de los gases al consumirse el Helio",
	width=1000, height=750,center=(20,-5,0), background=(0,1,1))
	
r=0.5 #Radio de las esferas

#Llamamos a la funcionn 'fun' con para aplicar odeint con las concentraciones
#iniciales de gases de valor 0 y k1=1, k2=2
t=odeint(fun,[0,0,0,0],Yp,(1,1))
#Sumamos las concentraciones de los distintos gases, para poder después
#establecer la proporción en la que aparece cada uno de ellos
tot=t[-1,1]+t[-1,2]+t[-1,3]

esferas=[] #Creamos una lista para introducir las bolas

#Utilizamos un bucle for para crear 100 bolas en un cuadrante 10x10
#y añadimos cada bola a una lista a partir de la que modificaremos las
#propiedades de cada bola de la forma deseada
for i in range(10):
	for j in range(10):
		bola=sphere(pos=vector(i,j,0), radius=r)
		esferas.append(bola)

#En función de las proporciones en las que se encuentre cada uno de los gases,
#existirá un número mayor o menor de bolas coloreadas según la leyenda:
#Carbono-verde, Oxígeno-azul y Neon-rojo
for i in range(100):
	if i<= int((t[-1,1]/tot)*100):
		esferas[i].color=color.green#carbono
	elif int((t[-1,1]/tot)*100)<i<=int(((t[-1,1]+t[-1,2])/tot)*100):
		esferas[i].color=color.blue#oxigeno
	elif int(((t[-1,1]+t[-1,2])/tot)*100)<i<=100:
		esferas[i].color=color.red#neon

#Mostramos los títulos y leyendas que acompañan la representación		
label(pos=(3,10,0), text='Oxigeno', color=color.blue)
label(pos=(-2,5,0), text='Carbono', color=color.green) 
label(pos=(10,8,0), text='Neon', color=color.red) 
label(pos=(5,11,0), text='k1=1 ; k2=1')
label(pos=(5,13,0), text='Concentraciones iniciales: C=0, O=0, Ne=0')


#Mismo procedimiento, en este caso con concentraciones de los gases de 0,1 cada uno
#y k1=1, k2=1
esferas_2=[]
t=odeint(fun,[0,0.1,0.1,0.1],Yp,(1,1))
tot=t[-1,1]+t[-1,2]+t[-1,3]
for i in range(10):
	for j in range(10):
		bola=sphere(pos=vector(i+25,j,0), radius=r)
		esferas_2.append(bola)
for i in range(100):
	if i<= int((t[-1,1]/tot)*100):
		esferas_2[i].color=color.green#carbono
	elif int((t[-1,1]/tot)*100)<i<=int(((t[-1,1]+t[-1,2])/tot)*100):
		esferas_2[i].color=color.blue#oxigeno
	elif int(((t[-1,1]+t[-1,2])/tot)*100)<i<=100:
		esferas_2[i].color=color.red#neon		
label(pos=(28,10,0), text='Oxigeno', color=color.blue)
label(pos=(23,5,0), text='Carbono', color=color.green) 
label(pos=(35,8,0), text='Neon', color=color.red) 
label(pos=(30,11,0), text='k1=1 ; k2=1')
label(pos=(30,13,0), text='Concentraciones iniciales: C=0.1, O=0.1, Ne=0.1')


#En este caso sin concentraciones iniciales de los gases y con k1=0.5 y k2=0.6
esferas_3=[]
t=odeint(fun,[0,0,0,0],Yp,(0.5,0.6))
tot=t[-1,1]+t[-1,2]+t[-1,3]
for i in range(10):
	for j in range(10):
		bola=sphere(pos=vector(i,j-20,0), radius=r)
		esferas_3.append(bola)
for i in range(100):
	if i<= int((t[-1,1]/tot)*100):
		esferas_3[i].color=color.green#carbono
	elif int((t[-1,1]/tot)*100)<i<=int(((t[-1,1]+t[-1,2])/tot)*100):
		esferas_3[i].color=color.blue#oxigeno
	elif int(((t[-1,1]+t[-1,2])/tot)*100)<i<=100:
		esferas_3[i].color=color.red#neon		

label(pos=(3,-10,0), text='Oxigeno', color=color.blue)
label(pos=(-2,-15,0), text='Carbono', color=color.green) 
label(pos=(10,-12,0), text='Neon', color=color.red) 
label(pos=(5,-9,0), text='k1=0,5 ; k2=0,6')
label(pos=(5,-7,0), text='Concentraciones iniciales: C=0, O=0, Ne=0')


#Por último con concentraciones iniciales de los gases de 0.1 y valores de 
#k1=0.5, k2=0.6
esferas_4=[]
t=odeint(fun,[0.,0.1,0.1,0.1],Yp,(0.5,0.6))
tot=t[-1,1]+t[-1,2]+t[-1,3]
for i in range(10):
	for j in range(10):
		bola=sphere(pos=vector(i+25,j-20,0), radius=r)
		esferas_4.append(bola)
for i in range(100):
	if i<= int((t[-1,1]/tot)*100):
		esferas_4[i].color=color.green#carbono
	elif int((t[-1,1]/tot)*100)<i<=int(((t[-1,1]+t[-1,2])/tot)*100):
		esferas_4[i].color=color.blue#oxigeno
	elif int(((t[-1,1]+t[-1,2])/tot)*100)<i<=100:
		esferas_4[i].color=color.red#neon		

label(pos=(28,-10,0), text='Oxigeno', color=color.blue)
label(pos=(23,-15,0), text='Carbono', color=color.green) 
label(pos=(35,-12,0), text='Neon', color=color.red) 
label(pos=(30,-9,0), text='k1=0,5 ; k2=0,6')
label(pos=(30,-7,0), text='Concentraciones iniciales: C=0,1, O=0,1, Ne=0,1')


#---------------------------------------------------------------
'''
def k1fijo(k2):
	t=odeint(fun,[0,0,0,0],Yp,(1,k2))
	return t
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
k2=linspace(0.5,1.5,len(t[:,0]))
m=mgrid[0.5:1.5:1/100,0:t[-1,0]:t[-1,0]/100]
print(m)

fig = plt.figure(); ax = Axes3D(fig)

Cs=ax.plot_surface(m[0,:,:],k1fijo(m[0,:,:]),m[1,:,:], rstride=1, cstride=1, cmap=cm.spring)
#plt.colorbar(Cs)
#ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
#plt.show(block=False)'''
