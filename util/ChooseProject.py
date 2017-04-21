import os.path
# -*- coding: utf-8 -*-
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

__author__ = "rodripf"
__date__ = "$01/02/2012 10:45:52 AM$"

import os
import pygtk
pygtk.require('2.0')
import gtk
import string

class ChooseProject:
    def limpiarNombres(self, text):
        tmp = string.replace(text, "_", " ")
        return string.replace(tmp, ".jpg", "")

    def __init__(self, dir):
        self.onAbrir = []
        # Create a new window
        self.window = gtk.Dialog("Abrir")

        self.window.set_size_request(400, 500)

        self.window.connect("delete_event", self.deleteEvent)
        self.window.set_position(gtk.WIN_POS_CENTER)

        self.treestore = gtk.TreeStore(str, str)

        #dir = "./"
        car = os.listdir(dir)
        print car
        for e in car:
            if(os.path.isdir(os.path.join(dir, e))):
                self.treestore.append(None, [e,e])


        self.treeview = gtk.TreeView(self.treestore)
        self.tvcolumn = gtk.TreeViewColumn()
        self.treeview.append_column(self.tvcolumn)
        self.cell = gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        # make it searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        self.window.vbox.add(self.treeview)

        abrir = gtk.Button("Abrir")
        abrir.connect("clicked", self.abrirCB)
        self.window.action_area.pack_start(abrir, True, True, 0)


        cancelar = gtk.Button("Cancelar")
        cancelar.connect("clicked", self.cancelarCB)
        self.window.action_area.pack_start(cancelar, True, True, 0)

    def addOnAbrirListener(self, action):
        self.onAbrir.append(action)

    def show(self):
        self.window.show_all()

    def abrirCB(self, b):
        treeselection = self.treeview.get_selection()
        treeselection.set_mode(gtk.SELECTION_SINGLE)
        (model, iter) = treeselection.get_selected()

        d = self.treestore.get_value(iter, 1)
        
        self.window.destroy()
        for f in self.onAbrir:
            f(d)
            
        return d


    def cancelarCB(self, b):
        self.window.destroy()

    def deleteEvent(self, widget, event, data=None):
        self.window.destroy()
def main():
    gtk.main()

if __name__ == "__main__":
    tvexample = ChooseProject("../proyectos")
    tvexample.show()
    main()
    