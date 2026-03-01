
from src.administrador.tareas import Tareas

class Progrmador_tareas():

    def __init__(self):
        self.tareas = None

    def programar_tarea(self, target):
        tareas = Tareas()
        tareas.set_target(target)
        self.tareas = tareas

    def get_tareas(self):
        return self.tareas
    
    def add_tarea(self, tarea):
        self.get_tareas().add_tarea(tarea)
    
    def ejecucion(self, id):
        self.tareas.ejecucion(id)
