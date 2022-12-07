class Persona:
    nombre          = str
    edad            = int
    cedula          = int
    centroEstudios  = str
    
    def _init_(self, nombre, edad, cedula, centroEstudios):
        self.nombre =   nombre
        self.edad   =   edad
        self.cedula =  cedula
        self.centroEstudios =   centroEstudios
    
    def conversar (self, otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}, estudio en {self.centroEstudios}'
    
if __name__ == "__main__":
    pers1 = Persona()   #no me deja usar el constructor, sale error por eso le doy atributos por separado
    pers1.nombre="Juan"
    pers1.edad = 12
    pers1.cedula = 123123
    pers1.centroEstudios = "El Yavi"
    pers2 = Persona()
    pers2.nombre="Jose"
    pers2.edad = 121
    pers2.cedula = 121323123
    pers2.centroEstudios = "dxdd"
    print(pers1.conversar(pers2))
