from src.clients.client import Client

class Mollapp(Client):
    
    def __init__(self):
        self.programadorTareas = None

    def set_programador_tareas(self, programadorTareas):
        self.programadorTareas = programadorTareas

    def enviar(self, id):
        self.programadorTareas.ejecucion(id)

