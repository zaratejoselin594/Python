archivo = open("archivos\\texto.txt", encoding="UTF-8") #utilizar encoding="utf-8 para que no salgan errores"
print(archivo);

#leer archivo completo
#   print(archivo.read()) #depues de leer un archivo no se puede volver a leer

#para leer una linea, lee la primera linea  sin parametros
#luego si agregamos numeros de parametros, la cantidad de numeros seran los caracteres que se mostraran
leer_linea = archivo.readline()
print(leer_linea)
 
#leer linea por linea, nos devuelve una lista
leer_lineas = archivo.readlines() #para archivos grandes readlines nos puede consumir toda la memoria
print(leer_lineas)

#cerrar el archivo, una vez que lo cerramos no se pued volver a leer
#es importante cerrarlo se pueden eliminar los datos si se cierra de manera inesperada
archivo.close()