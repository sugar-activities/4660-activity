
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
__date__ = "$28/09/2012 01:24:15 PM$"

from TInterpreter import TInterpreter
from util.OpenNewProject import OpenNewProject
from util.ChooseProject import ChooseProject
import util.ControlFactory as ControlFactory

from sugar.activity import activity

import os
import pygtk
pygtk.require('2.0')
import gtk
import sugar

from gettext import gettext as _

class Tixo(activity.Activity):
    PROYECTOS = "proyectos"

    _NEW_TOOLBAR_SUPPORT = True
    try:
        from sugar.graphics.toolbarbox import ToolbarBox
        from sugar.graphics.toolbarbox import ToolbarButton
        from sugar.activity.widgets import StopButton
    except:
        _NEW_TOOLBAR_SUPPORT = False

    def __init__(self, handle, create_jobject=True):
        activity.Activity.__init__(self, handle, False)

        def activityToolbar(toolbar):
            ControlFactory.buttonFactory('open', toolbar, self.__abrir, tooltip=_('Open'))
            ControlFactory.buttonFactory('barrido', toolbar, self.__barrer, tooltip=_('Scanning'))
            ControlFactory.spinFactory(2.0, 0.5, 8.0, self.__cambioVelocidad, toolbar)
            ControlFactory.separatorFactory(toolbar, expand = True)


        if self._NEW_TOOLBAR_SUPPORT: #toolbar nuevo
            self.toolbar_box = sugar.graphics.toolbarbox.ToolbarBox()

            activityToolbar(self.toolbar_box.toolbar)

            stop_button = sugar.activity.widgets.StopButton(self)
            stop_button.props.accelerator = '<Ctrl><Shift>Q'
            self.toolbar_box.toolbar.insert(stop_button, -1)
            stop_button.show()

            self.set_toolbar_box(self.toolbar_box)
            self.toolbar_box.show()

        else: #old toolbar
            toolbox = activity.ActivityToolbox(self)

            self.activity_tb = toolbox.get_activity_toolbar()
            self.activity_tb.share.props.visible = False
            self.activity_tb.keep.props.visible = False

            activityToolbar(self.activity_tb)

            self.activity_tb.show_all()

            self.set_toolbox(toolbox)
            toolbox.show()

        self.activity = TInterpreter()

        self.set_canvas(self.activity.getContenedor())

    def __abrir(self, widget):
        abr = ChooseProject(self.PROYECTOS)
        abr.addOnAbrirListener(self.__abierto)
        abr.show()

    def __barrer(self, widget):
        self.activity.barrido()

    def __abierto(self, proyName):
        self.activity.load(os.path.join(self.PROYECTOS, proyName, "project.xml"),)

    def __cambioVelocidad(self, widget):
        self.activity.cambiarVelocidad(widget.get_value())
        print widget.get_value()

    def close(self, skip_save=False):
        activity.Activity.close(self, True)


    def write_file(self, file_path):
        pass


    def read_file(self, file_path):
        try:
            onp = OpenNewProject(file_path, self.metadata['title'])
            self.__abierto(onp.getProjectName())
        except Exception, e:
            print "Exception: ", e

        
