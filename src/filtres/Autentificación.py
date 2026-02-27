import Filtre


class Autentificacion(Filtre):
    def __init__(self):
        pass

    def ejecucion(self, nombre):
        print("Has sido autentificado " + nombre)
