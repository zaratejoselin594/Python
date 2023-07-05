diccionario = {
  "nombre": "pepe",
  "edad": 2463,
  "nombre_completo": "pepe pepito pepa"
}

#devuelve las claves del diccionario, sirve para iterar
print(diccionario.keys())

#devuelve el valor de la clave, si no se encurentra el valor devuelve none y el programa continua
print(diccionario.get("edad"))

#elimina todos los elementos de la lista
#print(diccionario.clear())

#elimina un elemento del diccionario
print(diccionario.pop("edad"))

#obtiene los elementos del diccionario y se puede iterar
print(diccionario.items())
