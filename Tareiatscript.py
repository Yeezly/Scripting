array = []
class Persona:
    def __init__(self, nombre, apellido, sexo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
def add():
    nombre = input("Insertar nombre: ")
    apellido = input("Insertar apellido: ") 
    sexo = input("Insertar sexo: ") 
    edad = input("Insertar edad: ") 
    newperson = Persona(nombre, apellido, sexo, edad)
    return newperson
def age():
    edadsuma = int(input("Edad que quieres sumar: "))
    edadindice = int(input("Indice donde quieres sumar: "))
    for i in range (0, len(array), edadindice):
        setattr(array[i], "edad", edadsuma + int(getattr(array[i], "edad")))
def printt():
    contador = 1
    for i in array:
        print("persona", contador)
        for j in vars(i):
            print (j, " ", getattr(i, j))
        contador += 1
print("Selecciona lo que quieres hacer a continuación, Para agregar a una persona presiona 1, para sumar la edad presiona 2:")
selection = int(input(""))
if selection == 1:
    activador = "y"
    while activador == "y":
        array.append(add())
        activador = input("¿Quiéres agregar a otra persona? y/n  ")
if selection == 2:
    age()
    printt()

