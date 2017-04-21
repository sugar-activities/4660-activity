import os
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
__date__ ="$27-sep-2012 12:59:02$"


from zipfile import *
import os.path


class OpenNewProject:
    PROYECTOS = "proyectos"

    def __init__(self, file, proyName):
        proyName = os.path.splitext(proyName)[0]
        destFolder = os.path.join(self.PROYECTOS, proyName)
        if os.path.exists(destFolder):
            raise Exception("El proyecto ya existe.")
        else:
            if is_zipfile(file):
                os.makedirs(destFolder)
                zip = ZipFile(file, 'r')
                zip.extractall(destFolder)
                self.carpeta = proyName
            else:
                raise Exception("El archivo no es valido o esta corrupto.")

    def getProjectName(self):
        return self.carpeta

if __name__ == "__main__":
    try:
        o = OpenNewProject("pruebaControl.tco", "pruebaControl")
    except Exception as ex:
        print ex
