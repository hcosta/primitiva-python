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
    
"""Script de ejemplo
apuesta = [0, 1, 49, 3, 23, 43] # APUESTA: Lista de 6 numeros del 1 al 49 no repetidos
reintegro = 7                   # REINTEGRO: 1 numero del 1 al 9
repeticiones = 1000             # REPETICIONES: Numero de veces a repetir el sorteo
minimo = 3                      # MINIMO: Mostrar a partir de 3 o mas aciertos

print "="*50    
print "NUMERO APOSTADO\t\t%s" % apuesta
print "REINTEGRO\t\t[%d]\nREPETICIONES\t\t%d " % (reintegro, repeticiones)
print "MOSTRANDO RESULTADOS A PARTIR DE -%d- ACIERTOS " % minimo
print "="*50   
for i in range(repeticiones):
    s = Sorteo()
    s.setApuesta(apuesta)
    aciertos = s.getAciertos()
    resCom = "NO" 
    resRei = "NO"
    if s.isComplementarioInApuesta(): resCom = "SI"
    if reintegro == s.getReintegro(): resRei = "SI"
    if aciertos >= minimo:
        print "Repeticion %d\nSorteo %s\nComplementario > [%s] %s toca\nAciertos %d\nReintegro [%d] > %s toca\n%s" % (i, 
                                                            s.getBolasPremiadas(), s.getComplementario(), resCom,
                                                            aciertos, s.getReintegro(), resRei, "="*50)
    s = None"""