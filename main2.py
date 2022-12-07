class miClase:
    x=5
    
p1 = miClase()
print(p1.x)

class persona():
    nombre = str
    edad = int
    
    def _init_(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def _str_(self):
        return f"{self.nombre} es su nombre"        
    

class Persona2:
    nombre = str
    edad = int
    cedula = int
    
    def _init_(self,nombre,edad,cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
    
    def miFuncion(self):
        print("Hola mi nombre es "+self.nombre + " mi cedula es {self.cedula} y tengo {self.edad} anos")
p2 = Persona2()

p2.nombre = "XD"
p2.cedula = 123123
p2.edad = 12

p2.miFuncion()