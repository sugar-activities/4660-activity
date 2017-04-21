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

from components.TInterpreterCommonCell import TInterpreterCommonCell
__author__="Rodrigo"
__date__ ="$25-sep-2012 14:28:49$"

import pygtk
pygtk.require('2.0')
import gtk


class TInterpreterControlCell(TInterpreterCommonCell):
    EXIT_ACTION_CODE = 1
    UNDO_ACTION_CODE = 2
    UNDO_ALL_ACTION_CODE = 3
    READ_ACTION_CODE = 4
    RETURN_ACTION_CODE = 5
    STOP_ACTION_CODE = 6
    HOME_ACTION_CODE = 7
    COPY_ACTION_CODE = 8

    def __init__(self):
        super(TInterpreterControlCell, self).__init__()
        self.connect("clicked", self.onClick)

    def setActionCode(self, value, action = None):
        self._ActionCode = value
        
        if action!= None:
            self._action = action



#=======ON EVENTS==========================================================

    def onClick(self, widget):
        if self._ActionCode == self.EXIT_ACTION_CODE:
            gtk.main_quit()
        else:
            self._action()


