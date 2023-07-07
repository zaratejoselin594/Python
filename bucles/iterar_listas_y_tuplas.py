#crear lista con varios elementos
animales = ["gato", "perro", "loro", "paloma", "pato"]
numeros = (123,545,3,453,6)

#recorrer la lista e impriir los elementos de la lista
for animal in animales:
  print(animal)
  
#recorriendo la lista numeros y cada valor multiplicado por 2
for numero in numeros:
  print(f"el n es: {numero} y el {numero} * 2 es: {numero * 2}")
  
#recorriendo dos listas con un solo for, tienen que ser con la misma cantidad de elementos cada lista
for numero, animal in zip(numeros,animales):
  print("recorriendo lista uno ",numero)
  print("recorriendo lista dos ",animal)
  
#recorriendo numeros desde 4 hasta el 22 el 23 no cuenta
for num in range (4, 23):
  print(num)
  
#recorriendo los numeros desde el indice de la lista, no es una mejor forma de recorrer la lista
for num in range(len(numeros)):
  print(numeros[num])
  
#mejor forma de recorrerlo con su indice
for indice, num in enumerate(numeros):
  #print(type(num))
  valor = num
  print(f"indice: {indice}, valor: {valor}")
  
#usando el for/else 
for num in numeros:
  print(num)
else: #lo muestra siempre al final de cada bucle
  print("el bucle termino")

#todo lo anterior funciona exactamente igual con las tuplas