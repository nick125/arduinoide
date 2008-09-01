#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import os
import gtk
import gtk.glade

class MainWindow:
	def __init__(self, title=_("Arduino IDE")):
		"""
			Initialize the main window.
		"""
		self.gladefile = os.path.abspath("../../resources/glade/editor.glade") # TODO: Fix this!
		self.widgets = gtk.glade.XML(self.gladefile)
		self.window = self.widgets.get_widget("MainWindow")
	
