import random


class Cliente:
    def __init__(self, id):
        self.id = id
        self.tiempo_servicio = random.randint(1, 10)
        self.tiempo_llegada = 0 + self.tiempo_servicio

    def procesar(self, reloj):
        print(
            f"Cliente {self.id} llega en t = {reloj} y requiere {self.tiempo_servicio} unidades de tiempo para ser atendido."
        )
        return self.tiempo_servicio
