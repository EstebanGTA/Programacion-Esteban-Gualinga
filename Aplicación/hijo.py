from padre import Persona
from padre import Persona2
from madre import Madre

class Hijo3(Persona):
    vivienda  = str
    
    def __init__(self,nombre,apellido,edad,vivienda):
        super().__init__(nombre,apellido,edad)
        self.vivienda
        
hijo3 = Hijo3("Diego", "Yanez", 29, "Centro historico")
padre3 = Persona("German", "Yanez", 55)

print(vars(hijo3))
print(vars(padre3))
print(padre3.conversar(hijo3))

class Hijo4(Persona2):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad      = edad
        self.semestre = semestre
        
    def felicitar(self, padre):
        return f'Felicidades {self.nombre}, acabas de terminar tu {self.semestre} semestre a tus {self.edad}. Att {padre.nombre} {padre.apellido}'
    
padre4 = Persona2("Ivan", "Borja")
hijo4  = Hijo4("Ivan", "Borja", 18, "Quinto")

print(vars(padre4))
print(vars(hijo4))
print(hijo4.felicitar(padre4))

class Hijofinal(Madre):
    nombre          = str
    apellidoPaterno = str
    apellidoMaterno = str
    madre = Madre("","","","")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, madre, ciudad, apellido):
        super().__init__(nombre, apellido, edad, ciudad)
        self.apellidoMaterno = apellidoMaterno 
        self.apellidoPaterno = apellidoPaterno        
        self.madre           = madre
        

#madrefinal = Madre("vERONICA" "Flores", 55, "Quito")
hijofinal  = Hijofinal("Diego", "Yanez", "Floes", 29, Madre("vERONICA", "Flores", 55, "Quito"), "", "Quito")

print(hijofinal.madre)
print(hijofinal)

print(vars(hijofinal))

