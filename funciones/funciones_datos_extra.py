#creamos funcion de tres aprametros
def frace(nombre, apellido, adj):
  return f"Hola {nombre} {apellido}, sos muy {adj}"

#utilizando keyword arguments
res = frace(adj = "denso", nombre = "Pepe", apellido = "pepepita")
print(res) 

#creando la misma funcion con un parametro opcional y un valor por defecto
def frace(nombre, apellido, adj = "denso"):
  return f"Hola {nombre} {apellido}, sos muy {adj}"
ress = frace("Pepe", "pepepita", "bueno")
print(ress) 