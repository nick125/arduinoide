#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import gtk
import arduinoide.core.i18n.gt._ as _ 

class MainWindow:
	def __init__(self, title=_("Arduino IDE")):
		"""
			Initialize the main window.
		"""
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	
	def show(self):
		"""
			Place all of your widget show() calls here
		"""
		self.window.show()
