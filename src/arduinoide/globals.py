#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPLv2 or later. View LICENSE for more information
#
import os

PRODUCT_NAME = "ArduinoIDE"
PRODUCT_VERSION = (0,0,1,'Git')
try:
	RESOURCES_PATH = os.path.abspath(os.path.join(os.path.join("../", os.path.dirname(__file__)), "resources"))
except NameError:
	RESOURCES_PATH = os.path.abspath(os.path.join(os.path.getcwd(), "resources"))
