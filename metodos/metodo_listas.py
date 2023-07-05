#creando una lista con list
lista = list(["pepe", "aaa", 3224, "casa", "jardin"])
print(lista)

#decuelve la cantidad de elementos
print(len(lista))

#agrega elementos a una lista
lista.append(":)")
print(lista)

#agrega un elemento en un indice determinado
lista.insert(2, "flor")
print(lista)

#agrega varios elementos a una lista
lista.extend([True, 3423, "hola mundo", 54636, False])
print(lista)

#elimina un elemento de la lista a travez de su indice
lista.pop(5)
print(lista)

#remueve elementos de una lista por el valor del elemento
lista.remove(True)
print(lista)

#elimina todos los elementos de una lista
#lista.clear()
print(lista)

#ordena los elementos de una lista de forma acendente (si colocamos reverse=True ordena al reves)
lista2 = [23,43,234,543,56326678,7889,42,68,7,5532,64,466,7,8865,433,544]
print(lista2)
lista2.sort()
print(lista2)

#invierte los elementos de una lista
lista.reverse()
print(lista)