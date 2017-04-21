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

__author__="Rodrigo"
__date__ ="$21-sep-2012 12:21:37$"

from components.TInterpreterCommonCell import TInterpreterCommonCell
import pygtk
pygtk.require('2.0')
import gtk

class TInterpreterAcumulatedCell(TInterpreterCommonCell):

    def __init__(self, original):
        self._original = original
        super(TInterpreterAcumulatedCell, self).__init__()
        self.setText(original.getText())
        self.setIcon(original.getIcon())
        self.initialize()

    def getOriginal(self):
        return self._original

    def getHeight(self):
        return 100

    def getWidth(self):
        return 80

    def getId(self):
        return self._original.getId()


if __name__ == "__main__":
    print "Hello World"
