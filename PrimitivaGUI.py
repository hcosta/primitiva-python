#!/usr/bin/python
# -*- coding: latin-1 -*- 

""" Clase Primitiva para el simulador del Sorteo de la Primitiva
    Interfaz creada con wxFormBuilder
    :author: Hector Costa Guzman
    :version: 0.1 """
    
###########################################################################
## Python code generated with wxFormBuilder (version May  4 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from Sorteo import *
from random import *
from thread import *
import wx
import threading
import time
import datetime

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        self.t0 = None
        self.counter = 0
        self.jugador_apuesta = []
        self.jugador_reintegro = None
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Simulador Sorteo Primitiva", pos = wx.DefaultPosition, size = wx.Size( 580,280 ) )
        
        self.SetSizeHintsSz( wx.Size( 580,280 ), wx.Size( 580,280 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL ) 
               
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tu apuesta", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2.Enable( False )
        self.m_textCtrl2.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.Enable( False )
        self.m_textCtrl3.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl4.Enable( False )
        self.m_textCtrl4.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
        
        self.m_textCtrl5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl5.Enable( False )
        self.m_textCtrl5.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
        
        self.m_textCtrl6 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl6.Enable( False )
        self.m_textCtrl6.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
        
        self.m_textCtrl7 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl7.Enable( False )
        self.m_textCtrl7.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u" R", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.m_textCtrl71 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl71.Enable( False )
        self.m_textCtrl71.SetMinSize( wx.Size( 30,-1 ) )
        
        bSizer5.Add( self.m_textCtrl71, 0, wx.ALL, 5 )
        
        
        bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Generar apuesta", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button1, 0, wx.ALL, 5 )
        
        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Número de intentos", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        m_choice1Choices = [ u"5000", u"10000", u"50000", u"100000"]
        self.m_choice1 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer4.Add( self.m_choice1, 0, wx.ALL, 5 )
        
        
        bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Empezar simulación", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
        
        bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText11 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Apuestas Premiadas", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer8.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_panel7 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"1ª Categoría", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText12.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        
        bSizer10.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        #self.m_textCtrl32 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl32.Enable( False )
        
        self.m_staticText32 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )
        self.m_staticText32.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText32.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer10.Add( self.m_staticText32, 1, wx.ALL, 5 )
        
        self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"2ª Categoría", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer10.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        #self.m_textCtrl33 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl33.Enable( False )
        self.m_staticText133 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText133.Wrap( -1 )
        self.m_staticText133.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText133.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer10.Add( self.m_staticText133, 1, wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"3ª Categoría", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
        
        bSizer10.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        #self.m_textCtrl34 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl34.Enable( False )
        
        self.m_staticText34 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        self.m_staticText34.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText34.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer10.Add( self.m_staticText34, 1, wx.ALL, 5 )
        
        bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText121 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"4ª Categoría ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText121.Wrap( -1 )
        self.m_staticText121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer101.Add( self.m_staticText121, 0, wx.ALL, 5 )
        
        #self.m_textCtrl321 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl321.Enable( False )
        
        self.m_staticText321 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText321.Wrap( -1 )
        self.m_staticText321.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText321.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer101.Add( self.m_staticText321, 1, wx.ALL, 5 )
        
        self.m_staticText141 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"5ª Categoría", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText141.Wrap( -1 )
        self.m_staticText141.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer101.Add( self.m_staticText141, 0, wx.ALL, 5 )
        
        #self.m_textCtrl331 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl331.Enable( False )
        
        self.m_staticText331 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText331.Wrap( -1 )
        self.m_staticText331.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText331.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer101.Add( self.m_staticText331, 1, wx.ALL, 5 )
        
        self.m_staticText151 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Reintegro", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText151.Wrap( -1 )
        self.m_staticText151.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 94, 92, False, wx.EmptyString ) )
        
        bSizer101.Add( self.m_staticText151, 0, wx.ALL, 5 )
        
        #self.m_textCtrl341 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl341.Enable( False )
        
        self.m_staticText341 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText341.Wrap( -1 )
        self.m_staticText341.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText341.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer101.Add( self.m_staticText341, 1, wx.ALL, 5 )
        
        bSizer9.Add( bSizer101, 1, wx.EXPAND, 5 )
        
        self.m_panel7.SetSizer( bSizer9 )
        self.m_panel7.Layout()
        bSizer9.Fit( self.m_panel7 )
        bSizer8.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_EXIT, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )
        
        self.m_menubar1.Append( self.m_menu1, u"Archivo" ) 
        
        self.m_menu11 = wx.Menu()
        self.m_menuItem11 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"El juego de la Lotería Primitiva", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem11 )
        
        self.m_menuItem111 = wx.MenuItem( self.m_menu11, wx.ID_ABOUT, u"Acerca de", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu11.AppendItem( self.m_menuItem111 )
        
        self.m_menubar1.Append( self.m_menu11, u"Ayuda" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
        self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
        self.Bind( wx.EVT_MENU, self.m_menuItem1OnMenuSelection, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem11OnMenuSelection, id = self.m_menuItem11.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem111OnMenuSelection, id = self.m_menuItem111.GetId() )  
        
        self.generarApuestaAleatoria()
        
        icon = wx.Icon('Primitiva.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)    
        
        self.lista_botones_apuestas = [self.m_staticText32, self.m_staticText133, self.m_staticText34, self.m_staticText321, self.m_staticText331, self.m_staticText341]              
               
    def __del__( self ):
        pass

  
    # Virtual event handlers, overide them in your derived class
    def m_button1OnButtonClick( self, event ):
        """Genera una apuesta aleatoria para el usuario"""
        self.generarApuestaAleatoria()
        
    def m_button2OnButtonClick( self, event ):
        """Crea el bucle de sorteos"""
        #self.t0 = datetime.datetime.now()
        self.counter = 1
        self.m_statusBar2.SetStatusText("Calculando resultados.")
        
        self.reiniciarCuenta()
        
        r = int(self.m_choice1.GetStringSelection()) / 1000
        for i in range(r):
            thread = threading.Thread(target=self.do_big_work)
            thread.setDaemon(0)
            thread.start()
        
        
        #self.m_statusBar2.SetStatusText("Cálculo completado")
        
    def do_big_work(self):
        # processing code here
        for i in range(100):
            thread = threading.Thread(target=self.do_little_work)
            thread.setDaemon(0)
            thread.start()
            
    def do_little_work(self):
        # processing code here
        for i in range(10):
            sorteo = Sorteo()
            # do stuff
            wx.CallAfter(self.update_view, sorteo)

    def update_view(self, sorteo):
        
        sorteo.setApuesta(self.jugador_apuesta)
        numero_aciertos = sorteo.getAciertos()
        reintegro_ganador = sorteo.getReintegro()
        combinacion_ganadora = sorteo.getBolasPremiadas()
        complementario = sorteo.getComplementario()  
        toca_complementario = sorteo.isComplementarioInApuesta()
        self.m_statusBar2.SetStatusText("Simulando intento " + str(self.counter) + ".")
        self.counter += 1
        
        """Mostramos el resultado de la simulacion
        
        for j in range(6):
            valor_bola_ganadora = list(combinacion_ganadora).pop(j)
            lista_botones_combinacion[j].SetValue(str(valor_bola_ganadora))
            
        self.m_textCtrl27.SetValue(str(complementario))
        self.m_textCtrl28.SetValue(str(reintegro_ganador))"""

        if numero_aciertos == 6:
            self.lista_botones_apuestas[0].SetLabel(str (int(self.lista_botones_apuestas[0].GetLabel()) + 1))
        elif numero_aciertos == 5 and toca_complementario:
            self.lista_botones_apuestas[1].SetLabel(str (int(self.lista_botones_apuestas[1].GetLabel()) + 1))
        elif numero_aciertos == 5 and not toca_complementario:
            self.lista_botones_apuestas[2].SetLabel(str (int(self.lista_botones_apuestas[2].GetLabel()) + 1))
        elif numero_aciertos == 4:
            self.lista_botones_apuestas[3].SetLabel(str (int(self.lista_botones_apuestas[3].GetLabel()) + 1))
        elif numero_aciertos == 3:
            self.lista_botones_apuestas[4].SetLabel(str (int(self.lista_botones_apuestas[4].GetLabel()) + 1))
           
        if reintegro_ganador == self.jugador_reintegro:
            self.lista_botones_apuestas[5].SetLabel(str (int(self.lista_botones_apuestas[5].GetLabel()) + 1))
        
        #print str(datetime.datetime.now() - self.t0)
        
        
    def m_menuItem1OnMenuSelection( self, event ):
        """Cierra el programa"""
        self.Close(True)
    
    def m_menuItem11OnMenuSelection( self, event ):
        """Muestra una ventana de información"""
        dlg = wx.MessageDialog( self, "La Lotería Primitiva es un juego de azar regulado por Loterías y Apuestas del Estado (LAE) que consiste en elegir 6 números diferentes entre 1 y 49, con el objetivo de acertar la Combinación Ganadora en el sorteo correspondiente, formada por 6 bolas de las 49 que se extraen del bombo (modalidad comúnmente conocida como 6/49). También se extrae una bola extra como número complementario, y otra bola de un bombo aparte, entre el 0 y el 9, que hace de número de «reintegro».", "Lotería Primitiva de España", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def m_menuItem111OnMenuSelection( self, event ):
        """Genera una apuesta aleatoria para el usuario"""
        dlg = wx.MessageDialog( self, "Este es un simulador creado por Héctor Costa Guzmán y programado en Python.\n\nMás información en http://hcosta.info", "Sobre el Simulador del Sorteo de la Lotería Primitiva", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def generarApuestaAleatoria(self):
        self.jugador_apuesta = []
        jugador_numeros_aleatorios = [i+1 for i in range(49)]
        shuffle(jugador_numeros_aleatorios)
        jugador_lista = [self.m_textCtrl2, self.m_textCtrl3, self.m_textCtrl4, self.m_textCtrl5, self.m_textCtrl6, self.m_textCtrl7]
        
        for i in range(6):
            valor_bola_apuesta = jugador_numeros_aleatorios.pop(randint(1, len(jugador_numeros_aleatorios)-1))
            self.jugador_apuesta.append(valor_bola_apuesta)
            jugador_lista[i].SetValue(str(valor_bola_apuesta))
        self.jugador_reintegro = randint(1, 9)
        self.m_textCtrl71.SetValue(str(self.jugador_reintegro))
        
    def reiniciarCuenta(self):
        lista_botones_apuestas = [self.m_staticText32, self.m_staticText133, self.m_staticText34, self.m_staticText321, self.m_staticText331, self.m_staticText341]
        for boton in lista_botones_apuestas:
            boton.SetLabel("0")
    

app = wx.App(False)
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
