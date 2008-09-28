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

# Handle the substitution macros like $(SRC:.c=.s) in a Makefile 
# Replaces all occurances of a with b in src.
def BSubst(src, a, b):
	t = src + " ";
	t = t.replace(a + " ", b + " ");
	t = t.rstrip(t);
	return t;

# epath = Path to file
# size = MSG_SIZE_BEFORE or MSG_SIZE_AFTER
# shex = HEX size (i.e, HEXSIZE)
def BShowSize(epath, size, shex):
	if (os.path.exists(epath)):
		print;
		print size; shex;
		print;

	return;

# Execute a system command, such as to compile a file
def BExecute(cmd):
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

	fout.write("\n");
	fout.write("void main()\n");
	fout.write("{\n");
	fout.write("}\n");
	lcnt = lcnt + 3;	

	# Close up shop
	finp.close();
	fout.close();

	return lcnt;
