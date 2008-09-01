#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPL v2 or later. View LICENSE for more information
#
# ArduinoPy module for Python
#
# Copy src to dst after writing a header
def acopyfile(src, dest, header):
	line = "";

	# Open files
	finp = os.open(src, "r");
	fout = os.open(dest, "w");
	
	# Write the header
	fout.write(header);

	# Copy src to dest
	while (line <> ""):
		finp.read(line);

		if (line != ""):
			fout.write(line);

	# Close up shop
	finp.close();
	fout.close();
	
	return lcnt;
