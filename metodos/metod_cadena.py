cadena = "hoLa"
cadena2 = "mUnDoooo"
cadena3 = "3223432"
cadena4 = "lksdjf2nl234ln4"
cadena5 = "fruta, 10, pepe, dia, noche, flor, arbol"
#devuelve los atributos validos para el objeto (dir es una funcion)
#print(dir(cadena)) 
#convierte toda la cadena en mayuscula
print(cadena.upper()) 
#convierte toda la cadena en minuscula
print(cadena.lower()) 
#convierte la primera letra a mayuscula
print(cadena2.capitalize()) 

#buscar cierto caracter en nuestra cadena
print(cadena2.find("o")) #devuelve -1 si no encuentra el valor 
#buscar cierto caracter en nuestra cadena
print(cadena2.index("m")) #devuelve una exepcion si no encuentra el valor 
 
#si es numerico devuelve true sino false, por mas que sea string (que contenga todo el texto numero retorna true)
print(cadena3.isnumeric())
#si es alfanumerico de true sino false
print(cadena4.isalpha())

#buscar cierto caracter en nuestra cadena, devuelve cantidad de veces encontrada la cadena
print(cadena2.count("o"))   #si no se encuentra dvuelve 0
#cuanta cuantos caracteres contiene una cadena
print(len(cadena2))

#verifica si una cadena empieza con cierto caracter
print(cadena.startswith("h"))
#verifica si una cadena termina con cierto caracter
print(cadena.endswith("a"))

#remplaza unos caracteres por otros
print(cadena2.replace("mUn", "Mun"))
#separar cadena con la cadena que le pasemos
print(cadena5.split(","))