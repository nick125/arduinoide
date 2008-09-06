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
# Our importsi

from ui.i18n import _

class MainWindow( gtk.Window ):
    
    def __init__(self):
        """
            Initialize the main window.
        """

        gtk.Window.__init__( self )

        self.buildGui()
    
    
    def buildGui( self ):
        """
        This functions builds the main gui

        Arguments:
        - self: The main object pointer
        """

        
        accelGroup = gtk.AccelGroup()
        self.add_accel_group( accelGroup )
        
        self.accelGroup = accelGroup
        
        self.set_title( "mouseTrap" )
        self.connect( "destroy", self.close)
       
        self.vBox = gtk.VBox()
        
        self.vBox.pack_start( self.buildMenu(), False, False )

        self.vBox.show_all()
        self.add(self.vBox)
        self.show()

    def buildMenu( self ):
        """
        Builds The application menu

        Arguments:
        - self: The main object pointer.
        """

        menu = gtk.Menu()
        mainItems = dict()

        menuBar = gtk.MenuBar()
        menuBar.show()
        
        for item in ( _( "File" ), _( "Edit" ), _( "Project" ), _( "View" ), _("Snippets") ):
            mainItems[ item ] = gtk.MenuItem( item )
            mainItems[ item ].show()


        for item in ( _( "File" ), _( "Edit" ), _( "Project" ), _( "View" ), _("Snippets") ):
            menuBar.append( mainItems[item] )

        return menuBar

    def close( self, *args ):
        """
        Close Function for the quit button.
        
        Arguments:
        - self: The main object pointer.
        - *args: The widget callback arguments.
        """
        print "close"
