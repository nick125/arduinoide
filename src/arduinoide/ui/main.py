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

	def _addTopLevelMenu(self, menubar, label):
		"""
			Adds a toplevel menu entry to the specified menubar
		"""
		mitem = gtk.MenuItem(label)
		menu = gtk.Menu()
		mitem.set_submenu(menu)
		menubar.append(mitem)
		return mitem
		
	def _addChildMenuItem(self, menu, label, callback=None, data=None):
		"""
			Adds a simple Menu item with a callback
		"""

		mitem = gtk.MenuItem(label)
		if callback:
			mitem.connect_object("activate", callback, data)		
		menu.append(mitem)
				
	def _buildMenu(self):
		"""
			Builds The application menu
		"""

		self.mainmenu = gtk.MenuBar()
		self.menuitems = {}
		# Build the base menus
		for menu in (("file", _("_File")), ("edit", _("_Edit")), ("view", _("_View")), ("help", _("_Help")),):
			self.menuitems[menu[0]] = self._addTopLevelMenu(self.mainmenu, menu[1])

		# Build the File menu
		fm = self.menuitems["file"].get_submenu()
		self._addChildMenuItem(fm, _("_New"), callback=None, data=None)
		self._addChildMenuItem(fm, _("_Open"), callback=None, data=None)
		self._addChildMenuItem(fm, _("_Save"), callback=None, data=None)
		self._addChildMenuItem(fm, _("Save _As"), callback=None, data=None)
		fm.append(gtk.SeparatorMenuItem())
		self._addChildMenuItem(fm, _("Quit"), callback=self.close, data=None)
			
		return self.mainmenu
		
	def _addToolbarStock(self, toolbar, image, label, tooltip, callback=None, data=None, position=-1):
		"""
			Adds a stock toolbar item
		"""
		toolitem = gtk.ToolButton()
		toolitem.set_stock_id(image)
		toolitem.set_label(label)

		if callback:
			toolitem.connect("clicked", callback, data)

		toolbar.insert(toolitem, position)

	def _buildToolBar(self):
		"""
			Builds The IDE toolbar

			Returns The toolbar.
		"""

		handlebox = gtk.HandleBox()

		self.toolbar = gtk.Toolbar()
		self.toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
		self.toolbar.set_style(gtk.TOOLBAR_BOTH)
		self.toolbar.set_border_width(5)
        
		self._addToolbarStock(self.toolbar, gtk.STOCK_NEW, _("New"), _("Create New File"), callback=None) 
		self._addToolbarStock(self.toolbar, gtk.STOCK_OPEN, _("Open"), _("Open File"), callback=None) 
		self._addToolbarStock(self.toolbar, gtk.STOCK_SAVE, _("Save"), _("Save File"), callback=None) 
		self.toolbar.insert(gtk.SeparatorToolItem(), -1)
		self._addToolbarStock(self.toolbar, gtk.STOCK_EXECUTE, _("Compile"), _("Compile"), callback=None)
		self._addToolbarStock(self.toolbar, gtk.STOCK_GO_UP, _("Upload"), _("Upload"), callback=None)

		handlebox.add(self.toolbar)

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
		raise SystemExit
