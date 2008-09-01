#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System Imports
import os
import gtk
import gtk.glade
# Our imports
import arduinoide.globals as gbls

class MainWindow:
	def __init__(self):
		"""
			Initialize the main window.
		"""

		self.gladefile = os.path.join(gbls.RESOURCES_PATH, "glade/editor.glade") # TODO: Fix this!
		self.widgets = gtk.glade.XML(self.gladefile)
		self.window = self.widgets.get_widget("MainWindow")

	def show(self):
		"""
			Shows the widgets (as necessary)
		"""

		self.window.show()
