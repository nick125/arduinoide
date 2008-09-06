#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import gtk

class TabManager:
	def __init__(self, notebook):
		# Replace the notebook
		notebook = NotebookWidget()

class NotebookWidget(gtk.Notebook):
	def __init__(self):
		gtk.Notebook.__init__(self)
		# Set some properties
		self.set_property('show-tabs', False)

	def new_tab(self, widget, scrolled=True):
		"""
			Creates a tab from the widget (and depending on the 
			scrolled variable) and will put it in a scrolled
			window.
		"""
		if scrolled:
			window = gtk.ScrolledWindow()
			window.add(widget)
			window.show()
		else:
			window = widget
		
