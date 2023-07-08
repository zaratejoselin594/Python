#nombre = lamnda x :x*2
#creadon una funcion lambda para multiplicar por 2
mult = lambda x : x * 2
#que es lo mismo a 
def mult_por_dos(x):
  return x * 2

print(f"lambda: {mult(20)}, def: {mult_por_dos(30)}")

#creando funcion que diga si es par o no
numeros = [2,6,7,3,5,0,1,3,4,2,5,6]
def es_par(num):
  if num % 2 == 0:
    return True

#usando filter con una funcion comun
num_par = filter(es_par, numeros)
print(list(num_par))

#creando lo mismo que antes pero con lambda
numeros_par = filter(lambda numero:numero % 2 ==0, numeros)
print(list(numeros_par))