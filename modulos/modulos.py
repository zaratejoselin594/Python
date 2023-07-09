#As se utiliza para crear un alias al importar un módulo, el as tambien aplica para las funciones
#importando un modulo
import modulo_saludar as ms
saludo = ms.saludar("pepe")
print(saludo)

#From es para decir que de modulo_saludo vamos a importar solo una funcion
from modulo_saludar import saludar2 as salu_dos
saludo = ms.salu_dos("pepe")
print(saludo)

#para seleccionar todas las funciones no es una buena practica hacer esto:
# from modulo_saludar import *
# es una muy mala practica debido a que sobrecarga el sistema inesesariamente

#otra cosa a tener en cuenta es que no pongas el mismo nombre a las variables igual a las funciones

#para ver las probiedades y metodos de el namespace
print(dir(ms))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
print(ms.__name__)

#esto si l modulo se encuentra en la misma carpeta 
#imaginemos que el modulo_saludar se encuentra dentro de una carpeta y esta carpeta se llama modulos, ¿como accederiamos al modulo?
#se accederia de esta manera:
#from modulos.modulo_saludar import saludar

# o tambien:
import modulos.modulo_saludar as mms
print(mms.saludar("pepe"))

# para utilizar las funciones debemos hacerlo de esta forma:
# print(modulos.modulo_saludar.saludar("pepe"))
# si no te sabes la ruta de donde esta el modulo que deseas usar, en el mismo modulo donde estan las funciones debes colocar print(__name__)  y te mostrara el nombre completo que deberias usar. de todas formas podras usar el as

