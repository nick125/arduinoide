#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import gtk

class NotebookWidget(gtk.Notebook):
	def __init__(self):
		gtk.Notebook.__init__(self)
		# Set some properties
		self.set_property('show-tabs', False)

	def new_tab(self, widget, title, scrolled=True):
		"""
			Creates a tab from the widget (and depending on the 
			scrolled variable) and will put it in a scrolled
			window.
		"""
		
		if scrolled:
			window = gtk.ScrolledWindow()
			window.add(widget)
			window.show_all()
		else:
			window = widget
			window.show()
			
		# Check if we have more than one tab, if so, show the tabs
		if (self.get_n_pages() + 1) > 1:
			self.set_property('show-tabs', True)
			
		# Create the tab label
		label = self.create_tab_label(title, window)

		# Append the page
		self.append_page(window)
		self.set_tab_label(window, label)
		
		self.set_current_page(self.get_n_pages())
		
	def create_tab_label(self, title, tab):
		hbox = gtk.HBox()
		cbtn = gtk.Button()
		label = gtk.Label(title)
		image = gtk.Image()

		image.set_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
		cbtn.set_image(image)
		cbtn.set_relief(gtk.RELIEF_NONE)
		cbtn.connect("clicked", self.close_tab, tab)

		hbox.pack_start(label, True, True)
		hbox.pack_end(cbtn, False, False)
		hbox.show_all()
		
		return hbox
		
	def close_tab(self, widget, tab):
		pagenum = self.page_num(tab)
		if pagenum != -1:
			self.remove_page(pagenum)
			tab.destroy()
			
		if self.get_n_pages() <= 1:
			self.set_property('show-tabs', False)
