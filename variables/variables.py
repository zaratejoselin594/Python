a = 7  #definir variable
b = 4
a += 3 #suma el numero actual con el nuevo y se queda guardado el resultado
c = a + b
print(c)

#concatenacion f-string
nombre = "pepe"
bienvenida = f"Hola {nombre}, ¿Cómo estás?"

del nombre
print(bienvenida) # se imprime igual porque ya se almaceno en bievenida

#del bienvenida
#print(bienvenida);

#operador de pertenencia in/not in
print("ola" in bienvenida) #busca esos carateres en la variable bienvenida y devuelve un valor booleano
print("sfls" not in bienvenida) 

#definir variable con camelCase
holaCualEsTuNombre = "";
#definir variable con snake_case
hola_cual_es_tu_nombre = "";