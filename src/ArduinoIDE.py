#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import arduinoide.core.ui.main
import arduinoide.core.i18n.gt
import os
import gtk

if __name__ == "__main__":
	arduinoide.core.i18n.gt.initialize(os.path.abspath("resources/mo"))
	mainwindow = arduinoide.core.ui.main.MainWindow()
	mainwindow.window.show()
	#mainwindow.show()
	gtk.main()
