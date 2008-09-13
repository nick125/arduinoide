#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#

import sys

class PluginManager:

	def __init__(self):
		self.plugins = {}
		
	def add_search_path(self, path):
		if path not in sys.path:
			sys.path.insert(0, path)
	
	def load_plugin(self, plugin):
		pass

