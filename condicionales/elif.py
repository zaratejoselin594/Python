usuario = "pepe"
clave = 1234

nom_usuario = input("Ingrese su nombre de ususario...  ")
contraseña = int(input("Ingrese su contraseña...  "))

if nom_usuario != usuario or contraseña != clave:
  if nom_usuario != usuario:
    print("Nombre de usuario incorrecto")
    nom_usuario = input("Ingrese nuevamente su nombre de ususario...  ")
    while nom_usuario !=  usuario:
      print("Nombre de usuario incorrecto")
      nom_usuario = input("Ingrese nuevamente su nombre de ususario...  ")
  if contraseña != clave:
    print("Contraseña incorrecta")
    contraseña = int(input("Ingrese nuevamente su contraseña...  "))
    while contraseña !=  clave:
      print("Contraseña incorrecta")
      contraseña = int(input("Ingrese nuevamente contraseña...  "))
      break
elif nom_usuario == usuario and contraseña == clave:
  print("Iniciando session correctamente... ")
  calculo = input("""Cual de estas calculo quieres realizar: 
                  1) Suma,
                  2) Resta,
                  3) Multiplicacion,
                  4) Division (devolviendo float)
                  5) Division (devolviento int)
                  6) Division (devolviendo resto)
                  Coloque el numero deseado...  """)

