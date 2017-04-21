import TInterpreterProject
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
__date__ ="$20-sep-2012 11:11:29$"

import speak.espeak_cmd as espeak_cmd
import speak.GoogleTTS as GoogleTTS

from components.TInterpreterCommonCell import TInterpreterCommonCell
from threads.TInterpreterPlaySound import TInterpreterPlaySound
import pygtk
pygtk.require('2.0')
import gtk



class TInterpreterCell(TInterpreterCommonCell):
    projectName = ""


    def __init__(self):
         super(TInterpreterCell, self).__init__()
         self.connect("clicked", self.onClick)
#         self.connect("enter", self.onMouseOver)
#         self.connect("enter", self.onMouseOut(widget))
         
         self._FollowingBoard = None
         self._Acumulable = False
         self._AlternativeIcon = None
         self._SoundFile = None
         self._VoiceText = None


#========SETUP FUNCTIONS========================================================

    def setSendTextTarget(self, value):
        self._SendTextTarget = value

    def setSendText(self, value):
        self._SendText = value

    def setAlternativeIcon(self, value):
        self._AlternativeIcon = value    

   
    def setSoundFile(self, value):
        self._SoundFile = value

    def setAlternativeSoundFile(self, value):
        self._AlternativeSoundFile = value

    def setVoiceText(self, value):
        self._VoiceText = value


#=======ADD LISTENERS===========================================================

    def setFollowingBoard(self, value, action):
        self._FollowingBoard = value
        self._actionChangeBoard = action


    def setAcumulable(self, value, action):
        self._Acumulable = value
        self._actionAcumulable = action






#=======ON EVENTS==========================================================

    def sonido(self):
        t = TInterpreterPlaySound((self._SoundFile,))
        t.start()

    def sintetizar(self):
        funciono = GoogleTTS.intentar(TInterpreterCell.projectName, self._VoiceText)
        if not funciono:
            espeak_cmd.hablar(self._VoiceText)

    def onMouseOver(self, widget):
        if self._AlternativeIcon:
            self.deInitialize()
            self.add(self.loadImage(img = self._AlternativeIcon))

    def onMouseOut(self, widget):
        self.initialize()

    def onClick(self, widget):
        if self._Acumulable:
            self._actionAcumulable(self)

        if self._SoundFile:
            self.sonido()

        if self._VoiceText:
            self.sintetizar()

        if self._FollowingBoard != None:
            self._actionChangeBoard(self._FollowingBoard)

if __name__ == "__main__":
    print "Hello World"
