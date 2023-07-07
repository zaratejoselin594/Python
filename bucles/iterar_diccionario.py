#crear diccionario
diccionario = {
  "nombre": "pepe",
  "apellido": "pepita",
  "numero": 3234
}
print(diccionario)

#iterar diccionario para obtener las claves
for key in diccionario:
  print(key)
  
#iterar diccionario con items() para obtener clave y valor
for key in diccionario.items():
  clave = key[0]
  valor = key[1]
  print(f"clave: {clave}, valor: {valor}")