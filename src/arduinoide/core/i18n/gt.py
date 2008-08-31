#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import gettext

def initialize(mopath):
	gettext.bindtextdomain('ArduinoIDE', mopath)
	gettext.textdomain('ArduinoIDE')

_ = gettext.gettext
