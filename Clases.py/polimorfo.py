# Importar las clases
from actorAcademico import ActorAcademico
from docente import Docente
from estudiante import Estudiante 
from investigador import Investigador

# Crear objetos de cada clase
actor_academico = ActorAcademico("Jorge Acevedo Gomez", "001", "unad@example.com")
docente = Docente("Diego Fernando Luna Ceballos", "002", "Diego@example.com", "Programacion Avanzada")
estudiante = Estudiante("Angie Carolina Chitiva Muñoz", "202047919_29", "angiecarolinacm@gmail.com", "Tecnologo en desarrollo de software")
investigador = Investigador("Ana Torres", "004", "ana@example.com", "Inteligencia Artificial")

# Invocar el método describir en cada clase
actor_academico.describir()  # Salida: Estoy respondiendo desde la clase ActorAcademico
docente.describir()          # Salida: Estoy respondiendo desde la clase Docente
estudiante.describir()        # Salida: Estoy respondiendo desde la clase Estudiante
investigador.describir()      # Salida: Estoy respondiendo desde la clase Investigador

# Ejemplo de uso de métodos adicionales
docente.darClase()           # Salida: Maria Lopez está dando clase de Matemáticas.
estudiante.estudiar()        # Salida: Carlos García está estudiando para su carrera en Ingeniería.
investigador.investigar()     # Salida: Ana Torres está investigando en el área de Inteligencia Artificial.
