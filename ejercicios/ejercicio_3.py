#falto el profe y los pibes van a armar la clase
#pedir el nombre y la edad de los compañeros que vinieron que vineron a clase

#funcion para obtener al asistente y al profesor
def obtener_compañeros(cantidad):

  #creando lista con los compañeros
  compañeros = []

  #ejecutando un for para pedir informacion de cada compañero
  for i in range(cantidad):
    nombre = input("Ingrese el nombre del compañero  ")
    edad = int(input("ingrese la edad del compañero  "))
    compañero = (nombre, edad)

    #agregando informacion a la lista
    compañeros.append(compañero)

  #ordenandolos de menor a mayor segun su edad
  compañeros.sort(key = lambda x:x[1])

  #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
  #para definir al asistente y profesor
  asistente = compañeros[0][0]
  profesor = compañeros[-1][0]

  #retornamos una tupla
  return asistente, profesor

#desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(5)

#mostramos resultado
print(f"profesor: {profesor}, asistente {asistente}")