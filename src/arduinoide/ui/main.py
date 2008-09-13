#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System Imports
import gtk

# Our imports

from arduinoide.core.i18n.gt import _
from arduinoide import ideglobals
from arduinoide.ui.tabs import NotebookWidget

class MainWindow( gtk.Window ):
	def __init__(self):
		"""
			Initialize the main window.
		"""

		gtk.Window.__init__(self)

		self.buildGui()
    
    
	def buildGui(self):
		"""
			This functions builds the main gui
		"""

        
		accelGroup = gtk.AccelGroup()
		self.add_accel_group(accelGroup)
		self.accelGroup = accelGroup
        
		self.set_title("%s %s" % (ideglobals.PRODUCT_NAME, ideglobals.PRODUCT_VERSIONSTR))
		self.connect("destroy", self.close)
       
		self.vBox = gtk.VBox()
        
		self.vBox.pack_start(self._buildMenu(), False, False)
		self.vBox.pack_start(self._buildToolBar(), False, False)
		self.vBox.pack_start(self._buildMainNoteBook(), True, True)
		
		self.set_default_size(640, 480)

		self.vBox.show_all()
		self.add(self.vBox)
		self.show()

	def _buildMenu(self):
		"""
			Builds The application menu
		"""

		menu = gtk.Menu()
		mainItems = {}

		menuBar = gtk.MenuBar()
		menuBar.show()
        
		for item in (_("File"), _("Edit"), _("Project"), _("View"), _("Snippets")):
			mainItems[item] = gtk.MenuItem(item)
			mainItems[item].show()
			menuBar.append(mainItems[item])

		return menuBar

	def _buildToolBar(self):
		"""
			Builds The IDE toolbar

			Returns The toolbar.
		"""

		handlebox = gtk.HandleBox()

		toolbar = gtk.Toolbar()
		toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
		toolbar.set_style(gtk.TOOLBAR_BOTH)
		toolbar.set_border_width(5)
        
		toolbar.insert_stock( gtk.STOCK_NEW, _( "Create New File" ), _( "Create New File" ), None, None, -1  ) 
		toolbar.insert_stock( gtk.STOCK_OPEN, _( "Open File" ), _( "Open File" ), None, None, -1  ) 
		toolbar.insert_stock( gtk.STOCK_SAVE, _( "Save File" ), _( "Save File" ), None, None, -1  ) 
		toolbar.append_space()
		toolbar.insert_stock( gtk.STOCK_EXECUTE, _( "Compile" ), _( "Compile" ), None, None, -1  )
		toolbar.insert_stock( gtk.STOCK_GO_UP, _( "Upload" ), _( "Upload" ), None, None, -1  )

		handlebox.add(toolbar)

		return handlebox

	def _buildMainNoteBook(self):
		"""
			Builds the main notebook of the ide
			Returns The notebook.
		"""

		self.notebook = NotebookWidget()
		self.notebook.set_tab_pos( gtk.POS_TOP )
		self.notebook.show()

		return self.notebook

	def close(self, *args):
		"""
			Close Function for the quit button.
        
			Arguments:
			- self: The main object pointer.
			- *args: The widget callback arguments.
		"""
		gtk.main_quit()
