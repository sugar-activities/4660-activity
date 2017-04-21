#!/usr/bin/python
import os
import os.path
import string
import urllib2
from threads.TInterpreterPlaySound import TInterpreterPlaySound


def __internetOn():
    try:
        urllib2.urlopen('http://www.google.com',timeout=1)        
        return True
    except urllib2.URLError as err:
        pass
    return False

def intentar(projectName, texto):
    texto = texto.split(" ")
    texto = string.join(texto, "+")

    destino = os.path.join("proyectos", projectName, texto + ".mp3")
    if os.path.exists(destino): #ya lo tengo, lo reproduzco
        t = TInterpreterPlaySound([destino, ])
        t.start()
        return True
    else: #no lo tengo
        if __internetOn(): #hay internet
            os.system("wget -q -U Mozilla -O \"" + destino + "\" \"http://translate.google.com/translate_tts?ie=UTF-8&tl=es&q=" + texto + "\"")
            t = TInterpreterPlaySound([destino, ])
            t.start()
            return True
        else: #no hay internet y no lo tengo
            return False
