#el "a" agrega 
with open("archivos\\texto.txt","a", encoding="UTF-8") as archivo:
  #archivo.write("ola") cada vez que lo ejecutamos se agrega el texto
  #usando un bucle para agregar varias lineas
  for i in range(5):
    #agregando lineas
    archivo.write(f"linea {i+1} agregada \n")