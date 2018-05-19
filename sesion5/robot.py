import time

class Robot:
    tipo = "generico"
    dof = 2
    sensores = {}
    actuadores = {}
    color = "negro"
    def __init__(self, tipo, dof, nombre='robot'):
        self.tipo = tipo
        self.dof = dof
        self.nombre = nombre

    def saludar(self):
        print("Hola! me llamo " + self.nombre + " y soy un " + self.tipo)

    def agregarSensor(self, tipo, cantidad):
        self.sensores[tipo] = cantidad
    
    def agregarActuador(self, tipo, cantidad):
        self.actuadores[tipo] = cantidad

    def caracteristicas(self):
        print("Tipo: ", self.tipo)
        print("Grados de Libertad: ", self.dof)
        print("Sensores: ", self.sensores)
        print("Actuadores: ", self.actuadores)
    

class Carro(Robot):
    aceleracion = 0
    encendido = False
    def __init__(self, nombre="carro"):
        self.dof = 2
        self.tipo = "carro"
        self.nombre = nombre
        self.actuadores = {"motoresDC": 2}

    def acelerar(self, acel):
        self.aceleracion = acel

    def estado(self):
        print("Aceleracion: ", self.aceleracion)
        print("Encendido: ", self.encendido)
        print("Color: ", self.color)
    
    def encender(self):
        print("Encendiendo...")
        time.sleep(2)
        self.encendido = True
        print("Encendido!!")

    def apagar(self):
        print("Apagando...")
        time.sleep(4)
        self.encendido = False
        print("Apagado!!")
    
    def tunear(self, tuneo, arg):
        tuneo(self, arg)


def pintar(robot, color):
    robot.color = color

# esto solo se ejecuta cuando corro el archivo no cuando importo
if __name__ == '__main__':        
    seguidor = Carro("jorge")
    seguidor.estado()
    seguidor.tunear(pintar, "amarillo")
    seguidor.estado()