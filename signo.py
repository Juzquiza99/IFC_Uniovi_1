a=input("Introduce el valor de a (x^2): ")
b=input("Introduce el valor de b(x): ")
c=input("Introduce el valor de c: ")

print("El valor de a (x^2) es: "+a)
print("El valor de b (x) es: "+b)
print("El valor de c es: "+c)

disc=(b**2-4*a*c)
disc_0=(-b/2*a)

if disc==0:
	print("x=" +str(disc_0))
	
else:
	if disc > 0:
		disc_pos=(-b+(((disc)**0.5)/2*a))
		disc_neg=(-b-(((disc)**0.5)/2*a))
		print("x=" +str(disc_pos))
		print("x=" +str(disc_neg))
	
	elif disc > 0:
		comp_pos=(-b/2*a) +(1.j*(-d)**0.5)/2*a
