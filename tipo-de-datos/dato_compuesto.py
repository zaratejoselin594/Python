
#creando lista si se puede modificar
lista = ["joselin", "banana", 1.47, 15]

#creando tupla no se puede modificar
tupla = ("joselin", "banana", 1.47, 15)

#esto es valido
lista[2] = "pepe";

#esto no es valido
# tupla[2] = "pepe";

#creardo conjunto (set) no se puede modificar elemento 
set = {"joselin", "banana", 1.47, 15}
#pero si se puede reconstruir
set = {"ldkfjas"}
#no muestra datos repetidos y no se accede a los elementos a travez de un indice
set = {"joselin", "banana", 1.47, 15, "joselin"}
print(set)

#creando diccionaria (dict), estructura key:value, se separa con comas ,
diccionario = {
  "nombre": "joselin",
  "fruta": "banana",
  "altura": 1.47,
  "edad":15
}
