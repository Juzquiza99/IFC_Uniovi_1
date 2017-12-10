nMax=input("Introduce el maximo valor: ")
n = 1
a = [ ] # crea una lista vacia
while n < nMax:
   if n %11==0 and n%13== 0: # si n es par
      a.append(n) # aniade un elemento a la lista
   n = n + 1

i=0
while (i<len(a)):
   print("El numero %4d es multiplo de 11 y 13"%a[i])
   i+=1

print("Hasta "+str(nMax)+" existen "+str(len(a))+ " multiplos de 11 y 13")
