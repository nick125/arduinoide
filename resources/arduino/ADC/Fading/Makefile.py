#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under the GPL v2 or later. View LICENSE for more information
#
# Arduino 0011 Makefile
# Arduino adaptation by mellis, eighthave, oli.keller, it.daniher
#
# This makefile allows you to build sketches from the command line
# without the Arduino environment (or Java).
# HEAVILY MODIFIED FROM STOCK VERSION!
# ONLY COMPILES SKETCH TO A .HEX FILE - Upload.sh needed to burn to AVR
# Supports only "make" and "make clean"
#
# Date:			10-Sep-2008
# Purpose:		More Pythonizing; removed some old code no longer needed.
# Author:		Dale Weber <robotguy@hybotics.org>
#
# Date:			02-Sep-2008
# Purpose:		More Pythonizing vars; Starting to convert code;
#				Moved ShowSize() to BuildSystemLib as BShowSize()
# Author:		Dale Weber <robotguy@hybotics.org>
#
# Date:			01-Sep-2008
# Purpose:		Pythonizing variables and starting code conversion
# Author:		Dale Weber <robotguy@hybotics.org>				
#
# Date:			31-Aug-2008
# Purpose:		Conversion to Python started
# Author:		Dale Weber <robotguy@hybotics.org>				
#
import BuildSystemLib, os, shutil;

command = "";

#Name of the .pde you're trying to compile
# TARGET will be pased into the Build System
TARGET = "Fading";
# TARGET_EXT will be passed in or will be a part of TARGET
TARGET_EXT = ".pde";
#Name of the MCU in your arduino
MCU = "atmega168";									##### Should be a board preference
#hz of the MCU in your arduino
F_CPU = "16000000";									##### Should be a board preference

############################################################################
# Below here nothing should be changed...

ARDUINO = "/home/robotgy/Projects/Arduino/arduino-011/hardware/libraries";
AVR_TOOLS_PATH = "/usr/bin"							##### Should be a tools preference;
SRC =  ARDUINO + "/pins_arduino.c " + ARDUINO + "/wiring.c " + ARDUINO + "/wiring_analog.c " + ARDUINO + "/wiring_digital.c " + ARDUINO + "/wiring_pulse.c " + ARDUINO + "/wiring_serial.c " + ARDUINO + "/wiring_shift.c " + ARDUINO + "/WInterrupts.c";
CXXSRC = ARDUINO + "/HardwareSerial.cpp " + ARDUINO + "/WMath.cpp";
FORMAT = "ihex";									##### Should be a project preference

# Debugging format.
# Native formats for AVR-GCC's -g are stabs [default], or dwarf-2.
# AVR (extended) COFF requires stabs, plus an avr-objcopy run.
DEBUG = "stabs";

OPT = "s";											##### Should be a build preference

# Place -D or -U options here
CDEFS = "-DF_CPU=" + F_CPU;							###### Should be a build preference
CXXDEFS = "-DF_CPU=" + F_CPU;						###### Should be a build preference

# Place -I options here
CINCS = "-I" + ARDUINO;								##### Should be a build preference
CXXINCS = "-I" + ARDUINO;							##### Should be a build preference

# Compiler flag to set the C Standard level.
# c89   - "ANSI" C
# gnu89 - c89 plus GCC extensions
# c99   - ISO C99 standard (not yet fully implemented)
# gnu99 - c99 plus GCC extensions
CSTANDARD = "-std=gnu99";							#### Default or build preference
CDEBUG = "-g$" + DEBUG;								#### Default or build preference
CWARN = "-Wall -Wstrict-prototypes";				#### Default or build preference
CTUNING = "-funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums"#### Default or build preference;
#CEXTRA = -Wa,-adhlns=$(<:.c=.lst)

CFLAGS = "$" + CDEBUG + " " + CDEFS + " " + CINCS + " -O" + OPT + " " + CWARN + " " + CSTANDARD + " " + CEXTRA;
CXXFLAGS = CDEFS + " " + CINCS + " -O" + OPT;		#### Default or build preference
#ASFLAGS = -Wa,-adhlns=$(<:.S=.lst),-gstabs 
LDFLAGS = "-lm";

# Program settings - AVR_TOOLS_PATH should be a preference.
#
CC = AVR_TOOLS_PATH + "/avr-gcc";
CXX = AVR_TOOLS_PATH + "/avr-g++";
OBJCOPY = AVR_TOOLS_PATH + "/avr-objcopy";
OBJDUMP = AVR_TOOLS_PATH + "/avr-objdump";
AR  = AVR_TOOLS_PATH + "/avr-ar";
SIZE = AVR_TOOLS_PATH + "/avr-size";
NM = AVR_TOOLS_PATH + "/avr-nm";

REMOVE = "rm -f";
MV = "mv -f";

# Define all object files.
OBJ = "$(SRC:.c=.o) $(CXXSRC:.cpp=.o) $(ASRC:.S=.o)" # OBJ = "$(SRC:.c=.o) $(CXXSRC:.cpp=.o) $(ASRC:.S=.o)";

# Define all listing files.
LST = "$(ASRC:.S=.lst) $(CXXSRC:.cpp=.lst) $(SRC:.c=.lst)" # LST = "$(ASRC:.S=.lst) $(CXXSRC:.cpp=.lst) $(SRC:.c=.lst)";

# Combine all necessary flags and optional flags.
# Add target processor to flags.
ALL_CFLAGS = "-mmcu=" + MCU + " -I." + CFLAGS;
ALL_CXXFLAGS = "-mmcu=" + MCU + " -I." + CXXFLAGS;
ALL_ASFLAGS = "-mmcu=" + MCU + " -I. -x assembler-with-cpp " + ASFLAGS;
#
# Targets start here - the real conversion begins!
#
appletFile = "applet/" + TARGET;
appletFileElf = appletFile + ".elf";
appletFileHex = appletFile + ".hex";
appletFileCpp = appletFile + ".cpp";

targetFile = "";
sourceFile = "";

def BuildAppletFiles():
# applet_files: $(TARGET).pde
	# Here is the "preprocessing".
	# It creates a .cpp file based with the same name as the .pde file.
	# On top of the new .cpp file comes the WProgram.h header.
	# At the end there is a generic main() function attached.
	# Then the .cpp file will be compiled. Errors during compile will
	# refer to this new, automatically generated, file.
	# Not the original .pde file you actually edit...

	if (not os.path.isdir("applet")):
		os.mkdir("applet");
		sourceFile = TARGET + TARGET_EXT;

		# Copy the file
		BCopyFile(sourceFile, appletFileCpp, '#include "WProgram.h"');

	return;

def BuildElf():

	return;

def BuildHex():

	return;

def Build():
	
	BuildElf();
	BuildHex();

	return;

# Default target.
def BuildAll():
	BuildAppletFiles();
	Build();
	BShowSize(appletFileElf, MSG_SIZE_AFTER, HEXSIZE);
	return;

# all: applet_files build sizeafter

#build: elf hex 

elf: appletFileElf;
hex: appletFileHex;

# Display size of file.
HEXSIZE = SIZE + " --target=" + FORMAT + appletFileHex;
ELFSIZE = SIZE + appletFileElf;

.SUFFIXES: .elf .hex
# LOOK:
# I think the $@ is the same as in bash scripts - the rest of
#	the command line arguments.  I'm not sure about the "$<"
#	though.
#
.elf.hex:
	$(OBJCOPY) -O $(FORMAT) -R .eeprom $< $@


	# Link: create ELF output file from library.
applet/$(TARGET).elf: $(TARGET).pde applet/core.a 
	$(CC) $(ALL_CFLAGS) -o $@ applet/$(TARGET).cpp -L. applet/core.a $(LDFLAGS)
	
	command =  CC + " " + ALL_CFLAGS + " -o " +  $@ + " " + appletFileCpp + " -L. applet/core.a " + LDFLAGS
	BExecute(command);

applet/core.a: $(OBJ)
	@for i in $(OBJ); do
		echo $(AR) rcs applet/core.a $$i;
		$(AR) rcs applet/core.a $$i;
	done

# Pythonized
	for i in OBJ:
		command = AR + " rcs applet/core.a " + i;
		print command;
		BExecute(command);

# Compile: create object files from C++ source files.
.cpp.o:
	$(CXX) -c $(ALL_CXXFLAGS) $< -o $@ 

# Compile: create object files from C source files.
.c.o:
	$(CC) -c $(ALL_CFLAGS) $< -o $@ 

# Compile: create assembler files from C source files.
.c.s:
	$(CC) -S $(ALL_CFLAGS) $< -o $@

# Assemble: create object files from assembler source files.
.S.o:
	$(CC) -c $(ALL_ASFLAGS) $< -o $@

# Target: clean project.
clean:
	$(REMOVE) applet/$(TARGET).hex applet/$(TARGET).eep applet/$(TARGET).cof applet/$(TARGET).elf \
	applet/$(TARGET).map applet/$(TARGET).sym applet/$(TARGET).lss applet/core.a \
	$(OBJ) $(LST) $(SRC:.c=.s) $(SRC:.c=.d) $(CXXSRC:.cpp=.s) $(CXXSRC:.cpp=.d)

	# Pythonized - Not done yet.
	REMOVE + appletFile + ".hed " + appletFile + ".eep " + appletFile + ".cof " + appletFileElf + \
	appletFile + ".map " + appletFile + ".sym " + appleFile + ".lss applet/core.a " + \
	OBJ + " " + LST + " " + $(SRC:.c=.s) $(SRC:.c=.d) $(CXXSRC:.cpp=.s) $(CXXSRC:.cpp=.d)
