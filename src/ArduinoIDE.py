#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System imports
try:
	import gtk
	import gtksourceview2
	
except ImportError, exception:
	print "******************************************************"
	print " There was an error loading the following dependency: "
	print " %s" % exc.message
	raise SystemExit, "** Error loading required dependencies. **"

import arduinoide.ui.main

def init():
	gui = arduinoide.ui.main.MainWindow()
	gui.notebook.new_tab(gtksourceview2.View(), "New Tab")
	gui.notebook.new_tab(gtksourceview2.View(), "New Tab 2")
	gtk.main()

if __name__ == "__main__":
	init()

