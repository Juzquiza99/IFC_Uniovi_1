x = input("x ? ")
assert x > 0, "x debe ser no negativa"
try:
   y = 1./x
except:
   print("se divide por cero")
else:
   print("no se divide por cero")
finally: #se ejecuta si o si, haya o no error
   print("%3f esto se ejecuta siempre al final "%(y))
