from main import persona


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
    
    def saluda(self, otra_persona):
        return f'Hola mi nombre es '

if __name__ == "_main_":
    David = persona("David",33)
    Erika = persona("Erika",35)

print(David.sa)