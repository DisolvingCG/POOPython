from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("----------------------------")
    Alumno().facultad = "FES Aragon del EDOMEX"

    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("----Un vistazzo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print("----Modificar atributos publicos")
    al1.edad = 9999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno("Diego", 19, "ICO")
    al2 = Alumno("Montse", 20, "Derecho")
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))
main()