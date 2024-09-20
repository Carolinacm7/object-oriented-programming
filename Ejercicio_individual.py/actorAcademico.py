#!/usr/bin/python
# -*- coding: utf-8 -*-

class ActorAcademico:
    def __init__(self, nombre, id, email):
        self.nombre = nombre
        self.id = id
        self.email = email

    def describir(self):
        print("Estoy respondiendo desde la clase ActorAcademico")

    def contratar(self):
        print(f"{self.nombre} ha sido contratado.")

    def getNombre(self):
        return self.nombre

    def setNombre(self, value):
        self.nombre = value

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value

    def getEmail(self):
        return self.email

    def setEmail(self, value):
        self.email = value
