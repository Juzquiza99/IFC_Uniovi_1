for x in range(-20,40+5,5): #bucle desde la minima a la maxima cada 5
   t=x*9./5 + 32 #calculamos el valor en farhenheit
   D.append(x) #aniadimos los valores a la lista D
   B.append(t) #aniadimos los valores a la lista B
   
#mostramos los resultados obtenidos
c=range(-20,40+5,5)
for x in (c):
  print("|  %4d   |  %5.1f   |"%(D[i],B[i]))

f=open('temperaturasC.dat', 'w')

a=range(len(D)

for x in (a):
   f.write(str(a) + '\n')

f.close()
