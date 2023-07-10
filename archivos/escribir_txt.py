#el "w" primero sobre escribe y luego escribe
with open("archivos\\texto.txt","w", encoding="UTF-8") as archivo:
  #archivo.write("jdfa hola") # sobre escibe el archivo
  archivo.writelines(["hola\n", "mundo\n"]) #se debe de escribir de manera en lista, 
  #\n es para dejar un espacio en linea

  #ahora no sobreescribe solo añade
  archivo.writelines(["holaaaa\n", "pepe"]) 