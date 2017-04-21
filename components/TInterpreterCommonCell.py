__author__="Rodrigo"
__date__ ="$21-sep-2012 12:25:32$"

from components.TInterpreterCommonControl import TInterpreterCommonControl
import pygtk
pygtk.require('2.0')
import gtk
import pango

class TInterpreterCommonCell(gtk.Button, TInterpreterCommonControl):
#=======SETUP==========================================================

    def __init__(self):
        super(TInterpreterCommonCell, self).__init__()
        self._VerticalTextPosition = 0        
        self._Icon = None
        self._Text = None
        self.BackgroundColor = None;


    def setIcon(self, value):
        self._Icon = value   

    def getIcon(self):
        return self._Icon        

    def setAlternativeBorderColor(self, value):
        self._AlternativeBorderColor = value

    def setAlternativeBorderWidth(self, value):
        self._AlternativeBorderWidth = value

    def setVerticalTextPosition(self, value):
        self._VerticalTextPosition = value

    def setId(self, value):
        #self.set_label(value)
        self._Id = value

#========GET FUNCTIONS========================================================
    def getId(self):
        return self._Id

    def getX(self):
        return self._OriginalRect[0]

    def getY(self):
        return self._OriginalRect[1]

    def getWidth(self):
        return self._OriginalRect[2]

    def getHeight(self):
        return self._OriginalRect[3]


#=======COLORIZE================================================================

    def resaltar(self):
        color = self.get_colormap().alloc_color("#ff0000")

        self.modify_bg(gtk.STATE_NORMAL, color)
        self.modify_bg(gtk.STATE_ACTIVE, color)
        self.modify_base(gtk.STATE_NORMAL, color)
        self.modify_bg(gtk.STATE_PRELIGHT, color)
        
        self.grab_focus()

    def desResaltar(self):
        color = self.get_colormap().alloc_color("#" + self.BackgroundColor.upper()[2:])

        self.modify_bg(gtk.STATE_NORMAL, color)
        self.modify_bg(gtk.STATE_PRELIGHT, color)


#=======Events Handlers=========================================================
    def onMouseOver(self, widget):
        pass

    def onMouseOut(self, widget):
        pass

    def onClick(self, widget):
        pass



#=======INITIALIZATION==========================================================
    def initialize(self):
        #bacground color
        #make a gdk.color for red

        if self.BackgroundColor:
            color = self.get_colormap().alloc_color("#" + self.BackgroundColor.upper()[2:])

            self.modify_bg(gtk.STATE_NORMAL, color)
            self.modify_bg(gtk.STATE_PRELIGHT, color)

        


        if self._Text != None and self._Icon != None:
            vbox = gtk.VBox(False, 0)
            lbl = gtk.Label(self._Text)
            if self._VerticalTextPosition == 3: #bottom
                vbox.pack_start(self.loadImage(True))
                vbox.pack_end(lbl)
            else: #top or center = top
                vbox.pack_start(lbl, False, False, 0)
                vbox.pack_end(self.loadImage(True), False, False, 0)

            self.add(vbox)
            text = lbl

        elif self._Text!=None:
            self.set_label(self._Text)
            text = self
        elif self._Icon != None:
            self.add(self.loadImage())
            text = self

        if self._ForegroundColor:
            color = self.get_colormap().alloc_color("#" + self._ForegroundColor.upper()[2:])
            text.modify_fg(gtk.STATE_NORMAL, color)
            text.modify_fg(gtk.STATE_PRELIGHT, color)
        else:
            color = self.get_colormap().alloc_color("black")
            text.modify_fg(gtk.STATE_NORMAL, color)
            text.modify_fg(gtk.STATE_PRELIGHT, color)

        if self._FontSize:
            text.modify_font(pango.FontDescription("sans " + str(self._FontSize)))
            
    def deInitialize(self):
        children = self.get_children()
        for child in children:
            self.remove(child)

    def loadImage(self, texto = False, img = None):
        image = gtk.Image()
        if img==None:
            img = self._Icon
        pixbuf = gtk.gdk.pixbuf_new_from_file(img)

        maxW = float(self.getWidth())
        maxH = float(self.getHeight() if not texto else self.getHeight() - self._FontSize * 4)

        im = pixbuf.scale_simple(int(maxW - 10), int(maxH - 10), gtk.gdk.INTERP_BILINEAR)
        image.set_from_pixbuf(im)
        return image

if __name__ == "__main__":
    print "Hello World"
