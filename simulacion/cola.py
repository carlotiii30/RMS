from cliente import Cliente

class Cola:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)

    def atender(self, reloj):
        if self.clientes:
            cliente = self.clientes.pop(0)
            tiempo_servicio = cliente.procesar(reloj)
            print (f"Cliente {cliente.id} sale en t = {reloj + tiempo_servicio}")
            print()
            return tiempo_servicio

        return 0