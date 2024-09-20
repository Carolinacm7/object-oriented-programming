#!/usr/bin/python
# -*- coding: utf-8 -*-

from actorAcademico import ActorAcademico

class Estudiante(ActorAcademico):
    def __init__(self, nombre, id, email, carrera):
        super().__init__(nombre, id, email) 
        self.carrera = carrera

    def describir(self):
        print("Estoy respondiendo desde la clase Estudiante")

    def estudiar(self):
        print(f"{self.nombre} está estudiando para su carrera en {self.carrera}.")

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, value):
        self.carrera = value
