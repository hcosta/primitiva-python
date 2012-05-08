#!/usr/bin/python
""" Clase Bombo para el simulador del Sorteo de la Primitiva
    :author: Hector Costa Guzman
    :version: 0.1 """

from random import *

class Bombo:
    """Genera un Bombo con bolas (numeros)."""
    def __init__(self):
        """Inicializa la clase."""
        self.bolas = [i+1 for i in range(49)]
        shuffle(self.bolas)
        self.reintegro = randint(1,  9)
        
    def extraerBola(self):
        """Extrae una bola (numero) del Bombo."""
        return self.bolas.pop(randint(1,  len(self.bolas)-1))
        
    def getBolas(self):
        """Retorna la lista de bolas (numeros)."""
        return self.bolas
    
    def getReintegro(self):
        """Retorna la bola (numero) del reintegro."""
        return self.reintegro