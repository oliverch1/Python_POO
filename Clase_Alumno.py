import time

class Alumno:
    def __init__(self,nombre,codigo,correo,telefono):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__correo = correo
        self.__telefono = telefono

    def __repr__(self):
        return "Alumno:[nombre:'{}',codigo:'{}',correo:'{}',telefono:'{}']".format(
            self.__nombre,self.__codigo,self.__correo,self.__telefono)

    def set_nombre(self, dato):
        if isinstance(dato, str):
            self.__nombre = dato
        else:
            raise TypeError("error en el tipo de dato")
            
    def get_nombre(self):
        return self.__nombre

    def set_codigo(self,dato):
        if isinstance(dato,str):
            self.__codigo = dato
        else:
            raise TypeError("error en el tipo de dato")

    def get_codigo(self):
        return self.__codigo

    def set_correo(self,dato):
        if isinstance(dato,str):
            self.__correo = dato
        else:
            raise TypeError("error en el tipo de dato")

    def get_correo(self):
        return self.__correo

    def set_telefono(self,dato):
        if isinstance(dato,str):
            self.__telefono = dato
        else:
            raise TypeError("error en el tipo de dato")

    def get_telefono(self):
        return self.__telefono

def menu(opcion):
    while True:
        print("#"*50)
        print("1. ingresar datos del alunmo")
        print("2. listar alumnos")
        print("3. buscar alumno")
        print("4. quitar de la lista a un alumno")
        print("5. salir")
        opcion = int(input("ingrese opcion: "))
        if 0<opcion<6:
            break
        else:
            print("ingrese opcion correcta")
    return opcion

def agregar_alumno(Lista):
    nombre = input("ingrese nombre completo: ")
    codigo = input("ingrese codigo: ")
    correo = input("ingrese correo: ")
    telefono = input("ingrese telefono: ")
    alumno = Alumno(nombre,codigo,correo,telefono)
    Lista[nombre] = alumno

def listar_alumnos(Lista):
    if not Lista:
        print("no hay alumnos en la lista")
    else:
        print("#"*50)
        time.sleep(3)
        print("mostrando datos de la lista .....")
        for nombre,alumno in Lista.items():
            time.sleep(3)
            print(f"\ndatos del estudiante {nombre}: ")
            print(f"Nombre: {alumno.get_nombre()}")
            print(f"Codigo: {alumno.get_codigo()}")
            print(f"Correo: {alumno.get_correo()}")
            print(f"Telefono: {alumno.get_telefono()}\n")
    time.sleep(3)

def salir():
    print("cerrando el programa .....")
    time.sleep(3)

#desarrollando un programa que pida datos del alumno, los almacene y los muestre
Lista_Alumnos = {}

while True:
    opc = 0
    opc = menu(opc)
    if opc == 1:
        agregar_alumno(Lista_Alumnos)
        pregunta = "si"
        while pregunta == "si":
            pregunta = input("seguir agregando?(si o no): ")
            if pregunta == "si":
                agregar_alumno(Lista_Alumnos)
            else:
                break
    elif opc == 2:
        listar_alumnos(Lista_Alumnos)
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    else:
        exit()
