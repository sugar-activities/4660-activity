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

__author__ = "Rodrigo"
__date__ = "$18-sep-2012 12:35:06$"

from components.TInterpreterTextArea import TInterpreterTextArea
from components.TInterpreterControlCell import TInterpreterControlCell
from components.TInterpreterAcumulatedCell import TInterpreterAcumulatedCell
from TInterpreterBoard import TInterpreterBoard
from components.TInterpreterCell import TInterpreterCell
import xml.etree.ElementTree as ET

import pygtk
pygtk.require('2.0')
import gtk
import os

import string

class TInterpreterProject(gtk.VBox):
    PROYECTOS = "proyectos"
    

    def __init__(self):
        super(TInterpreterProject, self).__init__()
        self.currentBoard = None
        self.boardList = {}
        self.acumuladas = []
        self.acumuladasContainer = gtk.HBox(False, 0)
        self.pack_end(self.acumuladasContainer)
        self.show_all()

        self.barriendo = False
        self.velActual = 2.0

    def __getRealPath(self, path):
        path = string.replace(path, "\\", os.sep)
        path = string.replace(path, "/", os.sep)
        

        salida = os.path.join(self.PROYECTOS, self.projectName, path)
        return salida

        



    def XMLDecode(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        self.projectName = root.attrib["name"]
        TInterpreterCell.projectName = self.projectName
        self.initialBoard = root.find("initial_board").text

        for boardXML in root.findall("board"):
            board = TInterpreterBoard()
            board.setNombre(boardXML.attrib["name"])

            model = boardXML.find("model")

            for attrXML in model.find("attributes").findall("attribute"):
                key = attrXML.get("key")

                if key == "imageResizeStyle":
                    pass
                elif key == "orderedCellList":
                    orderedCellList = []
                    for cell in attrXML.findall("element"):
                        orderedCellList.append(cell.text)
                    board.setOrderedCellList(orderedCellList)
                elif key == "size":
                    width = int(float(attrXML.find("width").text))
                    height = int(float(attrXML.find("height").text))
                    board.setOriginalSize((width, height))
                elif key == "soundFile":
                    pass
                elif key == "icon":
                    pass
                elif key == "backgroundColor":
                    board.setBackgroundColor(attrXML.text)
                elif key == "gradientColor":
                    pass

            for compXML in model.findall("component"):
                type = compXML.get("type")

                if type == "cell":
                    cell = TInterpreterCell()

                    for attrXML in compXML.find("attributes").findall("attribute"):
                        key = attrXML.get("key")

                        if key == "followingBoard":
                            cell.setFollowingBoard(attrXML.text, self.setCurrentBoard)                        

                        elif key == "backgroundColor":
                            cell.setBackgroundColor(attrXML.text)

                        elif key == "gradientColor":
                            pass

                        elif key == "bordercolor":
                            cell.setBorderColor(attrXML.text)

                        elif key == "linewidth":
                            cell.setBorderWidth(int(float(attrXML.text)))                        

                        elif key=="environmentAction":
                            pass                        

                        elif key=="alternativeBorderColor":
                            cell.setAlternativeBorderColor(attrXML.text)

                        elif key=="alternativeLinewidth":
                            cell.setAlternativeBorderWidth(attrXML.text)

                        elif key=="accumulated":
                            acumulable = True if attrXML.text == "true" else False
                            cell.setAcumulable(acumulable, self.acumular)

                        elif key=="sendTextTimer":
                            pass

                        elif key=="sendTextTarget":
                            cell.setSendTextTarget(attrXML.text)

                        elif key=="sendText":
                            cell.setSendText(attrXML.text)

                        elif key=="alternativeIcon":
                            cell.setAlternativeIcon(self.__getRealPath(attrXML.text))
                        elif key=="verticalTextPosition":
                            cell.setVerticalTextPosition(attrXML.text)

                        elif key=="soundFile":
                            cell.setSoundFile(self.__getRealPath(attrXML.text))
                            
                        elif key=="alternativeSoundFile":
                            cell.setAlternativeSoundFile(self.__getRealPath(attrXML.text))

                        elif key=="voiceName":
                            pass
                        elif key=="voiceText":
                            cell.setVoiceText(attrXML.text)
                        elif key=="videoFile":
                            pass
                        elif key=="videoURL":
                            pass                    

                elif type == "controllerCell":
                    cell = TInterpreterControlCell()

                    for attrXML in compXML.find("attributes").findall("attribute"):
                        key = attrXML.get("key")
                        
                        if key=="actionCode":
                            code = int(attrXML.text)

                            if code == TInterpreterControlCell.EXIT_ACTION_CODE:
                                cell.setActionCode(code)
                            elif code == TInterpreterControlCell.UNDO_ACTION_CODE:
                                cell.setActionCode(code, self.desAcumular)
                            elif code == TInterpreterControlCell.UNDO_ALL_ACTION_CODE:
                                cell.setActionCode(code, self.desAcumularTodas)
                            elif code == TInterpreterControlCell.HOME_ACTION_CODE:                                
                                cell.setActionCode(code, self.irAInicial)
                            elif code==TInterpreterControlCell.READ_ACTION_CODE:
                                cell.setActionCode(code, self.readAcumuladas)


                elif type == "line":
                    pass

                elif type == "oval":
                    pass

                elif type == "rectangle":
                    pass

                elif type == "textArea":
                    cell = TInterpreterTextArea()

                    for attrXML in compXML.find("attributes").findall("attribute"):

                        if key=="horizontalAlignment":
                            pass
                        elif key == "verticalAlignment":
                            pass
                elif type == "roundRect":
                    pass
                elif type=="label":
                    pass


                #common attributes
                if type == "cell" or type == "controllerCell":
                    for attrXML in compXML.find("attributes").findall("attribute"):
                        key = attrXML.get("key")

                        if key == "font":
                            cell.setFontFamily(attrXML.find("family").text)
                            cell.setFontSize(int(attrXML.find("size").text))

                            bold = False if attrXML.find("bold") == None else True
                            cell.setFontBold(bold)

                            italic = False if attrXML.find("italic") == None else True
                            cell.setFontBold(italic)

                        elif key == "id":
                            cell.setId(attrXML.text)

                        elif key=="foregroundColor":
                            cell.setForegroundColor(attrXML.text)

                        elif key == "bounds":
                            x = int(float(attrXML.find("x").text))
                            y = int(float(attrXML.find("y").text))
                            width = int(float(attrXML.find("width").text))
                            height = int(float(attrXML.find("height").text))

                            cell.setOriginalRect((x, y, width, height))

                        elif key == "text":
                            cell.setText(attrXML.text)

                        elif key=="icon":
                            cell.setIcon(self.__getRealPath(attrXML.text))




                #agregar al tablero
                if type == "cell" or type == "controllerCell":
                    board.addCell(cell)
                                            


            self.boardList[board.getNombre()] = board
            


#========PROJECT ACTIONS========================================================
        
    def setCurrentBoard(self, nombre):
        if self.currentBoard != None:
            if self.barriendo:
                self.currentBoard.detenerBarrido()
            self.remove(self.currentBoard)

        board = self.boardList[nombre]
        board.initialize()
        self.pack_start(board)
        self.currentBoard = board

        if self.barriendo:
            self.currentBoard.iniciarBarrido()
        

    def acumular(self, cell):
        acu = TInterpreterAcumulatedCell(cell)
        self.acumuladasContainer.pack_start(acu, False, False, 0)
        acu.set_size_request(acu.getWidth(), acu.getHeight())
        acu.show_all()
        self.acumuladas.append(acu)

    def desAcumular(self):
        if len(self.acumuladas) > 0:
            self.acumuladasContainer.remove(self.acumuladas.pop())

    def desAcumularTodas(self):
        for acu in self.acumuladas:
            self.acumuladasContainer.remove(acu)
        self.acumuladas = []

    def irAInicial(self):
        self.setCurrentBoard(self.getInitialBoard())
        
    def readAcumuladas(self):
        for acu in self.acumuladas:
            acu.leer()

    def barrido(self):
        if not self.barriendo:
            self.cambiarVelocidad(self.velActual)
            self.currentBoard.iniciarBarrido()
            self.barriendo = True
        else:
            self.currentBoard.detenerBarrido()
            self.barriendo = False

    def cambiarVelocidad(self, value):
        self.velActual = value
        self.currentBoard.setVelocidadBarrido(value)



#=========GET===================================================================

    def getInitialBoard(self):
        return self.initialBoard

    def getProjectName(self):
        return self.projectName


if __name__ == "__main__":
    x = TInterpreterProject()
    x.XMLDecode("proyectos/Muestra/project.xml")
