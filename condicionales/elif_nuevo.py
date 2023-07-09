usuario = "pepe"
clave = 1234

nom_usuario = input("Ingrese su nombre de usuario  ")
contraseña = int(input("Ingrese su clave   "))
print("----------------")

def valor_incorrecto(valor_ingresado, valor_predeterminado, ms, mss, valor_ingresado2, valor_predeterminado2):
    if valor_ingresado != valor_predeterminado: 
      print(ms)
      valor_ingresado = input(f"Ingrese nuevamente su {mss}  ")
      print("----------------")
      if valor_ingresado == valor_predeterminado and valor_ingresado2 == valor_predeterminado2:
        realizar_calculo()
      while valor_ingresado !=  valor_predeterminado:
        print(ms)
        valor_ingresado = input(f"Ingrese nuevamente su {mss}  ")
        print("----------------")

def realizar_calculo():
  print("Iniciando session correctamente ")
  print("----------------")
  n1 = int(input("Ingrese un numero  "))
  n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar  "))
  print("----------------")
  tf = "si"
  while tf == "si":
    calculo = int(input("Cual de estas calculo quieres realizar: 1) Suma, 2) Resta, 3) Multiplicacion, 4) Potenciar, 5) Division (devolviendo float), 6) Division (devolviento int), 7) Division (devolviendo resto), Coloque el numero de operacion deseada.  "))
    op = { 1: n1 + n2, 2: n1 - n2, 3: n1 * n2, 4: n1 ** n2, 5: n1 / n2, 6: n1 // n2, 7: n1 % n2}
    print(op[calculo])
    tf_numero = input("Deseas camiar los numeros dados? si o no  ")
    print("----------------")
    if tf_numero == "si":
      n1 = int(input("Ingrese un numero.  "))
      n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
      print("----------------")
    tf = input("Quieres realizar otra operacion? si o no  ")

if nom_usuario != usuario or contraseña != clave:
  if nom_usuario != usuario:
    valor_incorrecto(nom_usuario, usuario, "Nombre de usuario incorrecto ", "Nombre de usuario", contraseña, clave)
  if contraseña != clave:
    valor_incorrecto(contraseña, clave, "Contraseña incorrecta ", "Contraseña", nom_usuario, usuario)
elif nom_usuario == usuario or contraseña == clave:
  realizar_calculo()
  