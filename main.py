class persona:
            nombre = str
            edad = int
            
            def _init_(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
            def saluda (self, otra_persona):
                return f'Hola {otra_persona.nombre}'