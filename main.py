from src.administrador.programador_tareas import Progrmador_tareas
from src.clients.mollapp import Mollapp
from src.filtres.Autentificación import Autentificacion
from src.filtres.Autorización import Autorizacion
from src.targets.Vehicle import Vehicle

class App:
    def main():

        id = input("Dinos tu nombre: ")

        programador_tareas = Progrmador_tareas()

        programador_tareas.programar_tarea(Vehicle())

        programador_tareas.add_tarea(Autentificacion())
        
        programador_tareas.add_tarea(Autorizacion())

        mollap = Mollapp()
        mollap.set_programador_tareas(programador_tareas)
        mollap.enviar(id)

if __name__ == "__main__":
    App.main()