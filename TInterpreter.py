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
__date__ = "$20-sep-2012 12:16:32$"

from TInterpreterProject import TInterpreterProject
from util.OpenNewProject import OpenNewProject
from util.ChooseProject import ChooseProject
import pygtk
pygtk.require('2.0')
import gtk
import os
import sys

class TInterpreter:
    PROYECTOS = "proyectos"

    def __init__(self):        
        self.project = TInterpreterProject()

    def load(self, xml):
        self.project.XMLDecode(xml)
        self.project.setCurrentBoard(self.project.getInitialBoard())
        self.project.show_all()


    def getContenedor(self):
        return self.project

    def exit(self, widget, data=None):
        gtk.main_quit()
        sys.exit
        
    def barrido(self, otro=None):
        self.project.barrido()

    def cambiarVelocidad(self, value):
        self.project.cambiarVelocidad(value)



#PARA EL FUNCIONAMIENTO FUERA DE SUGAR
    def mainPropio(self):
        #self.project.XMLDecode("proyectos/Muestra/project.xml")
        #self.project.setCurrentBoard(self.project.getInitialBoard())

        self.win = gtk.Window()
        w = self.win
        w.connect("destroy", self.exit)
        
        self.container = gtk.VBox();
        
        self.toolbar = gtk.Toolbar()
        self.toolbar.append_item("Agregar", "Agregar Proyecto", None, None, self.__agregar) 
        self.toolbar.append_item("Abrir", "Abrir Proyecto", None, None, self.__abrir) 
        self.toolbar.append_item("Barrido", "Barrido Automatico", None, None, self.barrido) 
        self.toolbar.show()      
        self.container.pack_start(self.toolbar)
        
        self.container.pack_start(self.project)   
        
        w.add(self.container)    
        
        w.show_all()


        gtk.main()
        
    def __agregar(self, widget):
        dialog = gtk.FileChooserDialog(title="Abrir", action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            try:
                onp = OpenNewProject(dialog.get_filename(), os.path.basename(dialog.get_filename()))
                self.load(os.path.join(self.PROYECTOS, onp.getProjectName(), "project.xml"),)
            except Exception, e:
                print "Exception: ", e
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        
        dialog.destroy()
        
    def __abrir(self, widget):
        abr = ChooseProject(self.PROYECTOS)
        abr.addOnAbrirListener(self.__abierto)
        abr.show()
        
    def __abierto(self, proyName):
        self.load(os.path.join(self.PROYECTOS, proyName, "project.xml"),)

    

if __name__ == "__main__":
    b = TInterpreter()
    b.mainPropio()
