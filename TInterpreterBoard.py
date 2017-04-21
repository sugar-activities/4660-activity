#   Tixo - A Sugar interpreter for TICO projects
#   Copyright (C) 2012  Rodrigo Perez Fulloni
#   Fundacion Teleton Uruguay - Departamento de Ingenieria
#
#   Based on TICO Project: http://www.proyectotico.com/
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


__author__ = "Rodrigo"
__date__ = "$20-sep-2012 10:15:25$"

from threading import Thread
import gobject
gobject.threads_init()
import time
import pygtk
pygtk.require('2.0')
import gtk


class TInterpreterBoard(gtk.EventBox):
    def __init__(self):
        self.cellList = {}
        super(TInterpreterBoard, self).__init__()
        self.f = gtk.Fixed()
        self.add(self.f)

        self.cellResaltada = None

        self._backgroundColor = None
        self.barriendo = False
        self.velocidadBarrido = 2.0


#========SETUP FUNCTIONS========================================================
    def setNombre(self, value):
        self._nombre = value

    def setOrderedCellList(self, list):
        self._orderedCellList = list

    def setOriginalSize(self, value):
        self._originalSize = value

    def addCell(self, cell):
        self.cellList[cell.getId()] = cell

    def setBackgroundColor(self, color):
        self._backgroundColor = color


#======GET FUNCTIONS============================================================
    def getNombre(self):
        return self._nombre

#======INITIALIZATION

    def initialize(self):
        if self._backgroundColor:
            color = self.get_colormap().alloc_color("#" + self._backgroundColor.upper()[2:])

            self.modify_bg(gtk.STATE_NORMAL, color)
            self.modify_bg(gtk.STATE_PRELIGHT, color)

        for cell in self.cellList.itervalues():
            cell.initialize()
            cell.set_size_request(cell.getWidth(), cell.getHeight())
            self.f.put(cell, cell.getX(), cell.getY())

        self.show_all()


#======BARRIDO AUTOMATICO=======================================================
    def barrer(self):
        while self.barriendo:            
            if self.cellResaltada != None:
                gobject.idle_add(self.cellList[self.cellResaltada].desResaltar)

            self.cellResaltada = self._orderedCellList[self.barridoActual]
            gobject.idle_add(self.cellList[self.cellResaltada].resaltar)

            if self.barridoActual < len(self._orderedCellList) - 1:
                self.barridoActual += 1
            else:
                self.barridoActual = 0

            time.sleep(self.velocidadBarrido)

    def accionarSeleccionado(self, widget, data):
        self.cellList[self.cellResaltada].onClick(None)

        
        

    def iniciarBarrido(self):
        self.barriendo = True
        # And bind an action to it
        #self.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        self._handl_id = self.connect("button_press_event", self.accionarSeleccionado)
        self.barridoActual = 0
        #self.t = Timer(2.0, self.barrerSiguiente)
        self.t = Thread(target= self.barrer)

        self.t.start()

    def detenerBarrido(self):
        self.barriendo = False
        self.disconnect(self._handl_id)

    def setVelocidadBarrido(self, value):
        self.velocidadBarrido = value

    def getVelocidadBarrido():
        return self.velocidadBarrido


if __name__ == "__main__":
    print "Hello World"
