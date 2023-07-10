with open("archivos\\texto.txt","w", encoding="UTF-8") as archivo:
  #archivo.write("jdfa hola") # sobre escibe el archivo
  archivo.writelines(["hola\n", "mundo\n"])