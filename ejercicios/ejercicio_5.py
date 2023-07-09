#creando una funcion que muestre la serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
  a,b = 0,1
  lista = [0]
  for i in range(num):
    if b > num: return lista
    else: 
      lista.append(b)
      a,b = b, a+b
  return lista

res = fibonacci(15)
print(res)