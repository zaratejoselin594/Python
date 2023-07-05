#le pedimos al usuario que nos escriba una frace
frace = input("Escribe una frace y calculare caunto tardarias en decirlo  ")

#crear lista con todas las palabras de la frace
palabras = frace.split(" ");

#usamos len para saber cuantas palabras hay
cantidad_palabras = len(palabras)

#en caso de que tarde un minuto le decimos que pare un poco
if cantidad_palabras > 120:
  print("para un poco")

#calcular cuanto tiempo tardaria en decirlo
print(f"Dijiste {cantidad_palabras} palabras y tardarias en decirlo {cantidad_palabras/2} segundos");