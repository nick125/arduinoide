!#/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPL v2 or later. View LICENSE for more information
#
# MakeLib module for the Python IDE for Arduino
#

#
# Copy src to dst after writing a header - not yet tested
def MCopyFile(src, dest, header):
	line = "";

	# Open files
	finp = os.open(src, "r");
	fout = os.open(dest, "w");
	
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
