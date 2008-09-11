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
import vte
import gtksourceview2 as gtksv
# Our importsi

from arduinoide.ui.i18n import _

class MainWindow( gtk.Window ):
	def __init__(self):
		"""
			Initialize the main window.
		"""

		gtk.Window.__init__(self)

		self.buildGui()
    
    
	def buildGui( self ):
		"""
			This functions builds the main gui
		"""

        
		accelGroup = gtk.AccelGroup()
		self.add_accel_group(accelGroup)
		self.accelGroup = accelGroup
        
		self.set_title("%s %s")
		self.connect( "destroy", self.close)
       
		self.vBox = gtk.VBox()
        
		self.vBox.pack_start( self._buildMenu(), False, False )
		self.vBox.pack_start( self._buildToolBar(), False, False )
		self.vBox.pack_start( self._buildMainNoteBook(), False, False )
        
		self._buildVte()

		self.vBox.show_all()
		self.add(self.vBox)
		self.show()

	def _buildMenu( self ):
		"""
			Builds The application menu
		"""

		menu = gtk.Menu()
		mainItems = {}

		menuBar = gtk.MenuBar()
		menuBar.show()
        
		for item in ( _( "File" ), _( "Edit" ), _( "Project" ), _( "View" ), _("Snippets") ):
			mainItems[item] = gtk.MenuItem(item)
			mainItems[item].show()


		for item in ( _( "File" ), _( "Edit" ), _( "Project" ), _( "View" ), _("Snippets") ):
			menuBar.append(mainItems[item])

		return menuBar

	def _buildToolBar( self ):
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

#		toolbar.append_widget( self._newStockImageButton( "Upload", gtk.STOCK_GO_UP ), _( "Upload" ), _( "Upload" ) )
		handlebox.add(toolbar)


		return handlebox

	def _buildMainNoteBook( self ):
		"""
			Builds the main notebook of the ide
			Returns The notebook.
		"""

		self.notebook = gtk.Notebook()
		self.notebook.set_tab_pos( gtk.POS_TOP )
        
		tab =  gtksv.View()
		tab.set_show_line_numbers( True ) 
        
		self.notebook.append_page( tab, gtk.Label( _( "New Tab" ) ) )
		self.notebook.show()

		return self.notebook

	def _buildVte( self ):
		"""
			Builds a VTE
		"""
        
		vt = vte.Terminal ()
		vt.connect("child-exited", lambda term: gtk.main_quit())
		vt.fork_command()

		self.notebook.append_page( vt, gtk.Label( "VTE" ) )
    
	def _newStockImageButton( self, label, stock ):
		"""
			Creates an image button from gtk's stock.
        
			Arguments:
			- self
			- label: The buttons label
			- stock: The Stock image the button will use. E.g: gtk.STOCK_GO-FORWARD
        
			Returns buttonLabelBox - A gtk.HBox that contains the new image stock button.
		"""
        
		buttonLabelBox = gtk.HBox()
       
		im = gtk.image_new_from_stock( stock, gtk.ICON_SIZE_BUTTON )
       
		label = gtk.Label( label )
		label.set_alignment( 0.0, 0.5 )
		label.set_use_underline( True )
        
		buttonLabelBox.pack_start( im )
		buttonLabelBox.pack_start( label )
		buttonLabelBox.show_all()
        
		return buttonLabelBox

	def close( self, *args ):
		"""
			Close Function for the quit button.
        
			Arguments:
			- self: The main object pointer.
			- *args: The widget callback arguments.
		"""
		print "close"
