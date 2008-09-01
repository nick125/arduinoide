#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System imports
import os
import sys
import gtk
# Our imports
import arduinoide.core.ui.main
import arduinoide.core.i18n.gt
from arduinoide import globals

if __name__ == "__main__":
	# GTK Version check
	if gtk.gtk_version[0] < 2 or gtk.gtk_version[1] < 8:
		ver_dialog = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK, message_format="GTK Version Error")
		ver_dialog.format_secondary_text("Your version of GTK is not compatible with this program. Please upgrade before continuing.")
		ver_dialog.run()
		sys.exit()
	# PyGTK Version check
	if gtk.pygtk_version[0] < 2 or gtk.pygtk_version[1] < 8:
		ver_dialog = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK, message_format="PyGTK Version Error")
		ver_dialog.format_secondary_text("Your version of PyGTK is not compatible with this program. Please upgrade before continuing.")
		ver_dialog.run()
		sys.exit()

	arduinoide.core.i18n.gt.initialize(os.path.join(globals.RESOURCES_PATH, "mo"))
	mainwindow = arduinoide.core.ui.main.MainWindow()
	mainwindow.connect_signals()
	mainwindow.show()
	gtk.main()
