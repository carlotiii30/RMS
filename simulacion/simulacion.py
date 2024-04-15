from cliente import Cliente
from cola import Cola

class Simulacion:
    def __init__(self):
        self.reloj = 0
        self.cola = Cola()

    def simular(self, tiempo_simulacion):
        while self.reloj < tiempo_simulacion:
            self.reloj += 1
            if self.reloj % 3 == 0:
                cliente = Cliente(self.reloj)
                self.cola.agregar(cliente)
            tiempo_servicio = self.cola.atender(self.reloj)
            if tiempo_servicio:
                self.reloj += tiempo_servicio