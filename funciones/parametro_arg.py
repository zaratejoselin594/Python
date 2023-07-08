#forma no optima de sumar valores
#def suma(lista):
#  num_sumados = 0
#  for numero in lista:
#    num_sumados += numero
#  return num_sumados

#resultado = suma([4,8,2,6])
#print(resultado)

#utilizando parametro args, forma optima
def suma(*numeros):
  return sum(numeros)
res = suma(34,2,55,234,1)
print(res)

