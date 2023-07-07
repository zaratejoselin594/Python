#encontrando el numero mayor de una lista
num = [23,34,7,657,4,5464,2364,88,6564]
print(max(num))

#el numero menor de la lista
print(min(num))

#redondiando numeros
numero = 15.35452
print(round(numero, 2)) #el segudo parametros muestra la cantidad de decimales que queremos

#retora false => 0, vacio, false, none / retorna true => distinto a 0, true, cadena, datos no vacios
print(bool([]))
print(bool([23,123,2]))

#retorna true si todos los datos son verdaderos
print(all(234,True, "ldkfga", [234,54]))

#suma todos los valores iterables
print(sum(num))