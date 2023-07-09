#creando una funcion que nos devuelve los numeros primos 
#entre el 0 y el numero que l pasemos
#crea funcion si un numero es primo
def es_primo(num):
    #verificar que el num no pueda dividirce por ningun numero entre 2 y el mismo numero -1
    for i in range(2, num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num % i == 0: return False
    #si termina el bucle, significa que no fue divicibble entonces es primo
    return True

#creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos lista
    primos = []
    for i in range(3, num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos

res = es_primo(23)
print(res)
resultado = primos_hasta(15)
print(resultado) 

prim_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5)+1)), range(3, num)))
print(prim_hasta(15))
