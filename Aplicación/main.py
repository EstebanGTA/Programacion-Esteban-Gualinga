class Persona:
    nombre      =   str
    apellido    =   str
    edad        =   int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre     =   nombre
        self.apellido   =   apellido
        self.edad       =   edad

if __name__ == "__main__":
    persona1    =   Persona("Esteban", "Gualinga", 18)
    lenin       =   Persona("lenin", "Montalvo", 19)

    print(persona1.apellido+persona1.nombre+str(persona1.edad))
    print(vars(persona1))
    print(lenin.apellido)
    
class Persona2:
    nombre      =   str
    apellido    =   str
    edad        =   int
    carrera     =   str
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre     =   nombre
        self.apellido   =   apellido
        self.edad       =   edad
        self.carrera    =   carrera
    
    def __str__(self):
        return f'Hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} y estudio {self.carrera}'

persona2    =   Persona2("Esteban","Gualinga",18,"Software")
print(persona2)

class Persona3:
    nombre      =   str
    apellido    =   str
    edad        =   int
    carrera     =   str
    semestre    =   str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre     =   nombre
        self.apellido   =   apellido
        self.edad       =   edad
        self.carrera    =   carrera
        self.semestre   =   semestre
    
    def Xd(self):
        print("Hola "+ self.nombre +" Bienvenido a la carrera "+ self.carrera)
        
#persona33    =   Persona3("Santiago","Venegas",26,"Software","Segundo")
#persona33.Xd()

class   Personax:
    nombre      =   str
    apellido    =   str
    edad        =   int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre     =   nombre
        self.apellido   =   apellido
        self.edad       =   edad
        
    def saludar(self, otra_persona):
        return f'Hola {otra_persona.nombre} mi nombre es {self.nombre} {self.apellido}'

prs1    =   Personax("Jose", "Tuqueres", 26)
prs2    =   Personax("Kevin", "Salazar", 18)


print(prs1.saludar(prs2))
print(prs2.saludar(prs1))
