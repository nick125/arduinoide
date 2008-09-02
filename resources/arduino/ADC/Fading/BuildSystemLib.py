#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPL v2 or later. View LICENSE for more information
#
# BuildSystemLib module for the Python IDE for Arduino
#
# Date:		02-Sep-2008
# Purpose:	New name for MakeLib is BuildSystemLib; Added BShowSize()
# Author:	Dale Weber <robotguy@hybotics.org>
#
import os, sys, errno;

# epath = Path to file
# size = MSG_SIZE_BEFORE or MSG_SIZE_AFTER
# shex = HEX size (i.e, HEXSIZE)
def BShowSize(epath, size, shex):
	if (os.path.exists(epath)):
		print;
		print size; shex;
		print;

# Copy src to dst after writing a header - not yet tested
def BCopyFile(src, dest, header):
	line = "";

	# Open files
	finp = os.open(src, O_RDONLY);
	fout = os.open(dest, WRITE);
	
	fout.write(header);			# Write out the header line
	lcnt = 1;					# Line counter

	# Copy src to dest
	while (line <> ""):
		finp.read(line);		# Get some data

		if (line != ""):		# Make sure we have data to write
			fout.write(line);	# Write the line
			lcnt += 1;			# Increment line counter

	# Close up shop
	finp.close();
	fout.close();
	
	return lcnt;

BCopyFile("a.txt", "b.txt", "This is the header");