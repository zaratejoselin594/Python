usuario = "pepe"
clave = 1234

nom_usuario = input("Ingrese su nombre de ususario.  ")
contraseña = int(input("Ingrese su contraseña.  "))

if nom_usuario != usuario or contraseña != clave:
  if nom_usuario != usuario:
    print("Nombre de usuario incorrecto")
    nom_usuario = input("Ingrese nuevamente su nombre de ususario.  ")
    while nom_usuario !=  usuario:
      print("Nombre de usuario incorrecto")
      nom_usuario = input("Ingrese nuevamente su nombre de ususario.  ")
    if contraseña == clave and nom_usuario == usuario:
      print("Iniciando session correctamente. ")
      n1 = int(input("Ingrese un numero.  "))
      n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
      tf = "si"
      while tf == "si":
        calculo = int(input("Cual de estas calculo quieres realizar: 1) Suma, 2) Resta, 3) Multiplicacion, 4) Potenciar, 5) Division (devolviendo float), 6) Division (devolviento int), 7) Division (devolviendo resto), Coloque el numero de operacion deseada.  "))
        if calculo == 1: print(n1 + n2)
        elif calculo == 2: print(n1 - n2)
        elif calculo == 3: print(n1 * n2)
        elif calculo == 4: print(n1 ** n2)
        elif calculo == 5: print(n1 / n2)
        elif calculo == 6: print(n1 // n2)
        elif calculo == 7: print(n1 % n2)
        tf_numero = input("Deseas camiar los numeros dados? si o no  ")
        if tf_numero == "si":
          n1 = int(input("Ingrese un numero.  "))
          n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
        tf = input("Quieres realizar otra operacion? si o no  ")
        
  if contraseña != clave:
    print("Contraseña incorrecta")
    contraseña = int(input("Ingrese nuevamente su contraseña  "))
    while contraseña !=  clave:
      print("Contraseña incorrecta")
      contraseña = int(input("Ingrese nuevamente contraseña  "))
    if contraseña == clave and nom_usuario == usuario:
      print("Iniciando session correctamente  ")
      n1 = int(input("Ingrese un numero  "))
      n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar  "))
      tf = "si"
      while tf == "si":
        calculo = int(input("Cual de estas calculo quieres realizar: 1) Suma, 2) Resta, 3) Multiplicacion, 4) Potenciar, 5) Division (devolviendo float), 6) Division (devolviento int), 7) Division (devolviendo resto), Coloque el numero de operacion deseada.  "))
        if calculo == 1: print(n1 + n2)
        elif calculo == 2: print(n1 - n2)
        elif calculo == 3: print(n1 * n2)
        elif calculo == 4: print(n1 ** n2)
        elif calculo == 5: print(n1 / n2)
        elif calculo == 6: print(n1 // n2)
        elif calculo == 7: print(n1 % n2)
        tf_numero = input("Deseas camiar los numeros dados? si o no  ")
        if tf_numero == "si":
          n1 = int(input("Ingrese un numero.  "))
          n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
        tf = input("Quieres realizar otra operacion? si o no  ")
elif nom_usuario == usuario and contraseña == clave:
  print("Iniciando session correctamente. ")
  n1 = int(input("Ingrese un numero.  "))
  n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
  tf = "si"
  while tf == "si":
    calculo = int(input("Cual de estas calculo quieres realizar: 1) Suma, 2) Resta, 3) Multiplicacion, 4) Potenciar, 5) Division (devolviendo float), 6) Division (devolviento int), 7) Division (devolviendo resto), Coloque el numero deseado...  "))
    if calculo == None: calculo = int(input("Cual de estas calculo quieres realizar: 1) Suma, 2) Resta, 3) Multiplicacion, 4) Potenciar, 5) Division (devolviendo float), 6) Division (devolviento int), 7) Division (devolviendo resto), Coloque el numero deseado...  "))
    elif calculo == 1: print(n1 + n2)
    elif calculo == 2: print(n1 - n2)
    elif calculo == 3: print(n1 * n2)
    elif calculo == 4: print(n1 ** n2)
    elif calculo == 5: print(n1 / n2)
    elif calculo == 6: print(n1 // n2)
    elif calculo == 7: print(n1 % n2)
    tf_numero = input("Deseas camiar los numeros dados? si o no  ")
    if tf_numero == "si":
      n1 = int(input("Ingrese un numero  "))
      n2 = int(input("Ingrese otro numero, luego eligiras el calculo que quieras realizar.  "))
      tf = input("Quieres realizar otra operacion? si o no  ")
      
#si ingresa dos numeros realizar dos operaciones
#si queda en blanco repetir nuevamente el input 
