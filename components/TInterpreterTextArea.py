from components.TInterpreterCommonControl import TInterpreterCommonControl
import pygtk
pygtk.require('2.0')
import gtk
__author__="Rodrigo"
__date__ ="$26-sep-2012 10:50:05$"

class TInterpreterTextArea(TInterpreterCommonControl, gtk.Entry):
    def __init__(self):
        super(TInterpreterTextArea, self).__init__()