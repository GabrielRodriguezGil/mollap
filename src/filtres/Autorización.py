import Filtre


class Autorizacion(Filtre):
    def __init__(self):
        pass

    def ejecucion(self, nombre):
        print("Has sido autorizado " + nombre)
