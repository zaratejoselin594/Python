frutas = {"banana", "pera", "frutilla", "manzana", "duranzno", "naranja", "mandarina", "ciruela"}

#evita que se coma una pera con la sentencia contiue
for fruta in frutas:
  if fruta == "pera":
    continue  #se salte la fruta pera pero el recorrido sigue funcionando
  print(f"voy a comer una {fruta}")
print("-----------------")
  
#evitando el bucle siga ejecutandoce con la sentencia break, el else no se ejecuta
for fruta in frutas:
  print(f"voy a comer una {fruta}")
  if fruta == "durazno":
    break
else:
  print("bucle terminado")
print("-----------------")

#recorrer cadena de texto
cadena = "hola mundo"
for caracter in cadena:
  print("caracter")
print("-----------------")

#for en una sola linea de codigo
numeros = [2,3,6,8]
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)