#!/usr/bin/env python

import gtk

class About:


    def show(self):
	#base this on a message dialog
	dialog = gtk.MessageDialog(
		None,
		gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		gtk.MESSAGE_QUESTION,
		gtk.BUTTONS_OK,
		None)
	dialog.set_markup("<b><big>TIXO</big></b>\n\nDepartamento de Ingenieria - rodripf\nFundacion Teleton - 2011")

	dialog.show_all()
	#go go go
	dialog.run()
	dialog.destroy()



if __name__ == '__main__':
	d = About()
        print d.show()
	gtk.main()
