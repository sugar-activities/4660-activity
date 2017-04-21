__author__="Rodrigo"
__date__ ="$25-sep-2012 14:47:44$"

class TInterpreterCommonControl:
    def __init__(self):
        self._ForegroundColor = None
        self.BackgroundColor = None
        self._FontFamily = None
        self._FontSize = None
        pass

    def setBackgroundColor(self, value):
        self.BackgroundColor = value


    def setOriginalRect(self, value):
        self._OriginalRect = value

    def setFontFamily(self, value):
        self._FontFamily = value

    def setFontSize(self, value):
        self._FontSize = value

    def setFontBold(self, value):
        self._FontBold = value

    def setFontItalic(self, value):
        self._FontItalic = value

    def setForegroundColor(self, value):
        self._ForegroundColor=value

    def setText(self, value):
        self._Text = value

    def setBorderWidth(self, value):
        self._BorderWidth = value

    def setBorderColor(self, value):
        self._BorderColor = value

    def getText(self):
        return self._Text

if __name__ == "__main__":
    print "Hello World";
