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
#			BFileCopy() now works and returns the number of lines written.
# Author:	Dale Weber <robotguy@hybotics.org>
#
import os;

# epath = Path to file
# size = MSG_SIZE_BEFORE or MSG_SIZE_AFTER
# shex = HEX size (i.e, HEXSIZE)
def BShowSize(epath, size, shex):
	if (os.path.exists(epath)):
		print;
		print size; shex;
		print;

	return;

# Copy src to dst after writing a header - not yet tested
# The output file is over written if it exists, or created.
#	Returns: Total number of lines written to the output file.
def BCopyFile(src, dest, header):
	line = "x";					# Input buffer

	# Open files
	finp = open(src, 'r');
	fout = open(dest, 'w');
	
	fout.write(header + "\n");	# Write out the header line
	lcnt = 1;					# Line counter

	# Copy src to dest
	while (line <> ""):
		line = finp.readline();	# Get some data

		if (line <> ""):		# Make sure we have data to write
			fout.write(line);	# Write the line
			lcnt = lcnt + 1;	# Increment line counter

	# Close up shop
	finp.close();
	fout.close();

	return lcnt;
