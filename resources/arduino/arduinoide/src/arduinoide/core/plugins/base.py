#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

class GenericPlugin:
	capabilities = []
	priority = 0

	def __repr__(self):
		return '<%s %r @ %d>' % (self.__class__.__name__, self.capabilities, self.priority)
		


