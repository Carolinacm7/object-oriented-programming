#!/usr/bin/python
# -*- coding: utf-8 -*-

from actorAcademico import ActorAcademico

class Investigador(ActorAcademico):
    def __init__(self, nombre, id, email, areaInvestigacion):
        super().__init__(nombre, id, email)  
        self.areaInvestigacion = areaInvestigacion

    def describir(self):
        print("Estoy respondiendo desde la clase Investigador")

    def investigar(self):
        print(f"{self.nombre} está investigando en el área de {self.areaInvestigacion}.")

    def getAreaInvestigacion(self):
        return self.areaInvestigacion

    def setAreaInvestigacion(self, value):
        self.areaInvestigacion = value
