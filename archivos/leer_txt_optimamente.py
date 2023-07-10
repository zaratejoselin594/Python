#consume menos recursos, es mas rapido, trae menos errores
#abriendo archivo con with open
with open("archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())

#no es necesario cerrarlo con with open