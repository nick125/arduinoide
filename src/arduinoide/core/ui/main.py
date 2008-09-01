#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System Imports
import os
import sys
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
		self.window.set_title("%s %s" % (gbls.PRODUCT_NAME, \
                	gbls.PRODUCT_VERSIONSTR))

	def connect_signals(self):
		"""
			Connect signals for the main UI here.
		"""

		##
		## This will eventually connnect signals for plugins (possibly?)
		##

		signals = { 
			# Window
			"on_MainWindow_destroy": self.destroy,
			# Menus
			"on_FileQuitMenuItem_activate": self.destroy,
			}

		self.widgets.signal_autoconnect(signals)

	def show(self):
		"""
			Shows the widgets (as necessary)
		"""

		self.window.show()

	def destroy(self, *args, **kwargs):
		"""
			Destroys the Main Window
		"""

		## This will eventually call some type of shutdown routine
		## that will shutdown plugins, trigger tabs to shutdown (save?),
		## etc.

		gtk.main_quit()
