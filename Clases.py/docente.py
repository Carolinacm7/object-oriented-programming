#!/usr/bin/python
# -*- coding: utf-8 -*-
from actorAcademico import ActorAcademico #llamado de archivo padre

class Docente(ActorAcademico):
    def __init__(self, nombre, id, email, profesion):
        super().__init__(nombre, id, email)  # es crucial para la herencia, ya que permite que la clase hija inicialice correctamente los atributos de la clase padre.s
        self.profesion = profesion

    def darClase(self):
        print(f"{self.nombre} está dando clase de {self.profesion}.")#La letra f indica que es una cadena formateada, y al colocar self.nombre dentro de llaves {}, se evalúa el valor de nombre para insertarlo en la cadena resultante. 

    def describir(self):
        print("Estoy respondiendo desde la clase Docente")

    def asesorar(self):
        print(f"{self.nombre} está asesorando a los estudiantes.")

    def getProfesion(self):
        return self.profesion

    def setProfesion(self, value):
        self.profesion = value
