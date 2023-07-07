#creando conjunto con set
conjunto = set(["dato1", "dato2"])
#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = ([conjunto1, "dato3"])

print(conjunto2)

#teoria de conjuntos
conjunt1 = {1,5,4,7,8,3,2}
conjunt2 = {2,1,5}

#verifica si es o no un subconjunto
resultado = conjunt2.issubset(conjunt1)
res = conjunt2 <= conjunt1 
print(resultado + "   " + res)

#verifica si es o no un superconjunto
resultado2 = conjunt2.issuperset(conjunt1)
res2 = conjunt1 >= conjunt2
print(resultado2 + "   " + res2)
  
#verifica si hay algun numero en comun
print(conjunt2.isdisjoint(conjunt1))