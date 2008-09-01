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
	print " %s" % exception.message
	raise SystemExit

# Our imports
try:
	import arduinoide.core.ui.main
	import arduinoide.core.i18n.gt
	from arduinoide import globals
except:
	print "*****************************************************************"
	print " There was an error loading the following ArduinoIDE dependency: "
	print " %s" % exception.message
	print " You may need to reinstall ArduinoIDE."
	raise SystemExit

def version_error(product):
	dialog = gtk.MessageDialog(parent=None, flags=0, type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK,
		message_format = "%s Version Error" % (product))
	err_msg = "Your version of %s is not compatible with this program. Please upgrade before continuing."
	dialog.format_secondary_text(err_msg % (product))
	dialog.run()
	sys.exit()

def version_checks():
	# check GTK
	if gtk.gtk_version[0] < 2 or gtk.gtk_version[1] < 4:
		version_error("GTK")
	# Check PyGTK
	if gtk.pygtk_version[0] < 2 or gtk.pygtk_version[1] < 4:
		version_error("PyGTK")
	# Check Python
	if sys.version_info[0] < 2 or sys.version_info[1] < 4:
		version_error("Python")

if __name__ == "__main__":
	# Run the version checks
	version_checks()
	arduinoide.core.i18n.gt.initialize(os.path.join(globals.RESOURCES_PATH, "mo"))
	mainwindow = arduinoide.core.ui.main.MainWindow()
	mainwindow.connect_signals()
	mainwindow.show()
	gtk.main()
