#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
# System imports
import os
import gtk
# Our imports
import arduinoide.core.ui.main
import arduinoide.core.i18n.gt
from arduinoide import globals

if __name__ == "__main__":
	arduinoide.core.i18n.gt.initialize(os.path.join(globals.RESOURCES_PATH, "mo"))
	mainwindow = arduinoide.core.ui.main.MainWindow()
	mainwindow.connect_signals()
	mainwindow.show()
	gtk.main()
