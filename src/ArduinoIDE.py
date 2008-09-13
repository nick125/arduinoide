#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System imports
try:
	import os
	import sys
	import gtk
except ImportError, exception:
	print "******************************************************"
	print " There was an error loading the following dependency: "
	print " %s" % exc.message
	raise SystemExit, "** Error loading required dependencies. **"

import arduinoide.ui.main as mainGui

def init():
	gui = mainGui.MainWindow()
	gtk.main()

if __name__ == "__main__":
	init()

