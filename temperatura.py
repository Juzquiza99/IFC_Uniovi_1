# Este programa se encarga de transformar una temperatura en grados

# Celsius y transformarla a grados Farenheit

c=float(input("Introduce una temperatura en grados Celsius. ")) 
#grabamos en la variable c el valor introducido

F=9./5*c+32; #realizamos la operacion para transformarlo y lo guardamos
# en la variable F

print("%.1f grados Celsius (C) son %.1f grados Farenheit (F)"%(c,F)) #Mostramos por pantalla
# ese texto
