#crear funciones con def, es una funcion simple
def saludar():
  print("Hola pepe")
saludar()

#crear funcion con parametros
def saludar(nombre, sexo):
  sexo = sexo.lower()
  if sexo == "mujer":
    adj = "maestra"
  elif sexo == "hombre":
    adj = "maestro"
  print(f"Hola {nombre}, mi {adj}, ¿Cómo andas?")
 
saludar("pepe", "hombre")
saludar("pepita", "mujer")

#crear funcion que nos retorne valores
def crear_contraseña(num):
  chars = "abcdefghijklmnñopqrstuvwxyz"
  num_str = str(num)
  num = int(num_str[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
  return contraseña

passs = crear_contraseña(29384)
print(passs)