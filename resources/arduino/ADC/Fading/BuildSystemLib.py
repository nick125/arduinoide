#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPL v2 or later. View LICENSE for more information
#
# BuildSystemLib module for the Python IDE for Arduino
#
# Date:		10-Sep-2008
# Purpose:	Removed testing code and rearranged code to fit structure.
#			Added some more comments.
# Author:	Dale Weber <robotguy@hybotics.org>
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

# Copy src to dest after writing a header
# The output file is over written if it exists, or created.
#	Returns: Total number of lines written to the output file.
def BCopyFile(src, dest, header):
	line = "x";					# Input buffer

	# Open files
	finp = open(src, 'r');		# Input file is read only.
	fout = open(dest, 'w');		# This will over write any existing output file.
	
	fout.write(header + "\n");	# Write out the header line
	lcnt = 1;					# Line counter

	# Copy src to dest
	while (line <> ""):			# Go until end of file.
		line = finp.readline();	# Read a line

		if (line <> ""):		# Make sure we have a real line
			fout.write(line);	# Write the line
			lcnt = lcnt + 1;	# Increment line counter

	# Close up shop
	finp.close();
	fout.close();

	return lcnt;