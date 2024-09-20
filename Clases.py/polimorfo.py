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


"""  
¿Qué instrucciones se utilizaron para establecer la herencia entre 
las clases?

   Para establecer la herencia entre clases en Python, se utiliza la sintaxis class Hijo(Padre):,
   donde Hijo es la clase que hereda de Padre. En este contexto, la clase padre se define primero,
   como en el caso de ActorAcademico, y luego las clases hijas, como Docente, Estudiante e Investigador, 
   se definen indicando que heredan de ActorAcademico.
   Esto permite que las clases hijas accedan a los atributos y métodos de la clase padre, 
   promoviendo la reutilización del código y la organización de la lógica en una jerarquía de clases.

b. ¿Qué función tiene la instrucción pass?
    La instrucción pass en Python se utiliza como un marcador de posición en el código,
    permitiendo que la estructura del programa se mantenga sin ejecutar ninguna acción.

c. Por cada clase se ha generado un archivo. ¿Cuáles son las 
instrucciones que se usaron para vincular los archivos entre sí y 
lograr la herencia entre hijos y padre?
    Para vincular los archivos entre sí y permitir la herencia en Python, se utilizan las instrucciones 
    import y from ... import .... Por ejemplo, para importar la clase ActorAcademico desde el archivo
    actorAcademico.py, se puede usar from actorAcademico import ActorAcademico. Esto permite a las clases 
    hijas en otros archivos acceder directamente a los atributos y métodos de la clase padre, facilitando 
    la reutilización y organización del código.

d. Para que sirven las funciones setter y getter que se agregaron a 
las clases. 
    Las funciones setter y getter permiten el acceso y modificación controlada de atributos en una clase.
    Los getters obtienen el valor de atributos privados, mientras que los setters permiten establecer o 
    modificar esos valores, a menudo validando el nuevo dato. Esto ayuda a mantener la integridad de los
    datos y a encapsular la lógica de acceso en la clase.
"""