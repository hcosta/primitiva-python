#!/usr/bin/python
""" Clase Sorteo para el simulador del Sorteo de la Primitiva
    :author: Hector Costa Guzman
    :version: 0.1 """

from Bombo import *

class Sorteo:
    """Genera un sorteo."""
    def __init__(self):
        """Inicializa la clase."""
        self.bolasPremiadas = []
        self.bombo = Bombo()
        self.aciertos = 0
        # Sacamos 6 bolas del bombo y las guardamos
        for i in range(6): 
            self.bolasPremiadas.append(self.bombo.extraerBola())
        # Sacamos el complementario y lo guardamos
        self.complementario = self.bombo.extraerBola()
        # Sacamos el reintegro
        self.reintegro = self.bombo.getReintegro()
            
    def getBolasPremiadas(self):
        """Devuelve una lista con las bolas premiadas."""
        return self.bolasPremiadas
    
    def setApuesta(self, apuesta):
        """Establece la lista con la apuesta."""
        self.apuesta = apuesta
        
    def getApuesta(self):
        """Devuelve la lista con la apuesta."""
        return self.apuesta
        
    def getAciertos(self):
        """Compara las apuestas y las bolas sacadas del bombo
                y devuelve el numero de aciertos."""
        for i in self.apuesta:
            try:
                if self.bolasPremiadas.index(i):
                    self.aciertos = self.aciertos + 1
            except ValueError:
                pass
        return self.aciertos    

    def getComplementario(self):
        """Devuelve el complementario."""
        return self.complementario
    
    def isComplementarioInApuesta(self):
        """Devuelve Verdadero si el complentario esta en la apuesta."""
        try:
            if self.apuesta.index(self.complementario):
                return True
        except ValueError: pass
        return False
                
    def getReintegro(self):
        """Devuelve el reintegro."""
        return self.reintegro     
    
    def reiniciarSorteo(self):
        self.bolasPremiadas = None
        self.bolasPremiadas = []
        self.bombo = Bombo()
        self.aciertos = 0
        # Sacamos 6 bolas del bombo y las guardamos
        for i in range(6): 
            self.bolasPremiadas.append(self.bombo.extraerBola())
        # Sacamos el complementario y lo guardamos
        self.complementario = self.bombo.extraerBola()
        # Sacamos el reintegro
        self.reintegro = self.bombo.getReintegro()