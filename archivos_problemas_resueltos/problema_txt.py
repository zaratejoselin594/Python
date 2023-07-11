#2 lisras, una con nombres otra con apellidos
nombres = ["pepe", "pedro", "juana", "lola"]
apellidos = ["pepepita", "pepa", "juan", "lalo"]

#registrar esta informacion en un txt de orma optima
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt", "w", encoding="UTF-8") as ar:
    ar.writelines("Los datos son: \n\n")
    [ar.writelines(f" Nombre: {n}\n Apellido {a}\n--------------\n") for n,a in zip(nombres,apellidos)]