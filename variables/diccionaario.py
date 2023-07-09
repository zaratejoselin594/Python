#creando diccionario con dict()
diccionario = dict(nombre = "pepe", apellido = "pepita")
print(diccionario)

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
dic = {frozenset(["pep"]):"e"} #stack overflow
print(dic)
#creando diccionario con fromkeys()
dicc = dict.fromkeys(["nombre","apellido"], "no se")
print(dicc)