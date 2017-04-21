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
import os
if os.name != "nt":
	import pygst
	pygst.require("0.10")
	import gst

import threading
import os

class TInterpreterPlaySound (threading.Thread):
    player = None
    def __init__(self, sounds):
        super(TInterpreterPlaySound, self).__init__()
        self.sounds = []
        for s in sounds:
            self.sounds.append("file://" + os.path.abspath(s))

        if TInterpreterPlaySound.player == None:
            TInterpreterPlaySound.player = gst.element_factory_make("playbin", "player")

            bus = TInterpreterPlaySound.player.get_bus()
            bus.add_signal_watch()
            bus.connect("message", self.onMessage)

    def onMessage(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
        elif t == gst.MESSAGE_ERROR:
            self.player.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print "Error: %s" % err, debug


    def run (self):
        #set the uri
        print self.sounds[0]
        TInterpreterPlaySound.player.set_property('uri', self.sounds[0])
        #start playing
        TInterpreterPlaySound.player.set_state(gst.STATE_PLAYING)

#        #listen for tags on the message bus; tag event might be called more than once
#        bus = player.get_bus()
#        bus.enable_sync_message_emission()
#        bus.add_signal_watch()
#        bus.connect('message::tag', on_tag)
