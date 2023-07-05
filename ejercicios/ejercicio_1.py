# Curso de Soy Dalto (en youtube)

#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_prom = 4
pepe_curso = 1.5

#Duracion crudo
crudo_prom = 5
crudo_pepe = 3.5

#diferencias de duracion
diferencia_curso_min = 100 - pepe_curso / otros_cursos_min *100
diferencia_curso_max = 100 - pepe_curso *1000 // otros_cursos_max / 10
diferencia_curso_prom = 100 - pepe_curso / otros_cursos_prom *100
print(f"El curso de pepe dura un {diferencia_curso_min} que el curso mas rapido")
print(f"El curso de pepe dura un {diferencia_curso_max} que el curso mas lento")
print(f"El curso de pepe dura un {diferencia_curso_prom} que el curso promedio")

#calcular el porcentaje de tiempo vacio removido
tiempo_vacio_prom = 100 - otros_cursos_prom *1000 // crudo_prom / 10
tiempo_vacio_pepe = 100 - pepe_curso *1000 // crudo_pepe / 10
print(f"pepe:  {tiempo_vacio_pepe}")
print(f"otros prom:  {tiempo_vacio_prom}")

#mostrando diferencias si los cursos duraran 10 horas
print(otros_cursos_prom*100 // pepe_curso / 10)
print(pepe_curso*100 // otros_cursos_prom / 10)