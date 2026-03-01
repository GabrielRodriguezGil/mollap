class Tareas():
    
    def __init__(self):
        self.tareas = []
        self.target = None
    
    def get_tareas(self):
        return self.tareas
    
    def get_target(self):
        return self.target
    
    def set_target(self, vehicle):
        self.target = vehicle

    def add_tarea(self,tarea):
        self.get_tareas().append(tarea)

    def ejecucion(self,id):
        for tarea in self.get_tareas():
            tarea.ejecucion(id)

        if self.target is not None:
            self.target.ejecucion(id)
        else:
            pass
