class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido,edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad      = edad
        
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} {self.apellido}, tengo {self.edad}'

class Hijo(Persona):
    ciudad = str
    
    def __init__(self,nombre,apellido,edad,ciudad):
        Persona.__init__(self,nombre,apellido,edad)
        self.ciudad = ciudad
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} {self.apellido}'
        
padre = Persona("Victor", "Grados", 50)
print(vars(padre))

hijo = Hijo("Elena", "Gradps", 25, "Quito")
print(vars(hijo))

#Agregar Metodos de herencia

class Persona2:
    nombre   = str
    apellido = str
    
    
    def __init__(self,nombre,apellido):
        self.nombre   = nombre
        self.apellido = apellido
        
    def conversar(self, otra_persona):
            return f'Hola {otra_persona.nombre}, me llamo {self.nombre} {self.apellido}'
    
        
class Hijo2(Persona2):
    estudios      = str
    lugarEstudios = str
    
    def __init__(self,nombre,apellido, materia, lugarEstudios):
        super().__init__(nombre, apellido)
        self.materia           = materia
        self.lugarEstudios     = lugarEstudios
        
    def informar(self, otra_persona):
        return f'Buenas tardes, {otra_persona.nombre} acabo de estudiar, {self.materia} llegue de {self.lugarEstudios}'

padre2 = Persona2("Juan", "Flores")
hijo2  = Hijo2("Jose", "Peres", "Programacion 00", "IST Yavirac")

print(hijo2.informar(padre2))
            
class Padre:
    nombre   = str
    apellido = str
    edad     = int
    ciudad   = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre     = nombre
        self.apellido   = apellido
        self.edad        = edad
        self.ciudad     = ciudad
        
    def bienvenida(self, hijo):
        return f'Buenas noches {hijo.nombre} bienvenido a la casa, la cena esta en el micro yo me encuentro de viaje en {self.ciudad} , Att {self.nombre} {self.apellido}'
    