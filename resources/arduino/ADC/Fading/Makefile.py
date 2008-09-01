#!/usr/bin/env python
#
# ArduinoIDE Project (http://arduino.bitmeadow.org)
# (c) 2008 ArduinoIDE Contributors
# Licensed under GPLv2. View LICENSE for more information
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
# 31-Aug-2008:	Conversion to Python started
# Author:		Dale Weber <robotguy@hybotics.org>				
#
#
#Name of the .pde you're trying to compile
TARGET = "Fading"
TARGET_EXT = ".pde"
#Name of the MCU in your arduino
MCU = "atmega168"
#hz of the MCU in your arduino
F_CPU = "16000000"

############################################################################
# Below here nothing should be changed...

ARDUINO = "/home/it/SOURCE/arduino/leetcompilelibs"
AVR_TOOLS_PATH = "/usr/bin"
SRC =  "$(ARDUINO)/pins_arduino.c $(ARDUINO)/wiring.c $(ARDUINO)/wiring_analog.c $(ARDUINO)/wiring_digital.c $(ARDUINO)/wiring_pulse.c $(ARDUINO)/wiring_serial.c $(ARDUINO)/wiring_shift.c $(ARDUINO)/WInterrupts.c"
CXXSRC = "$(ARDUINO)/HardwareSerial.cpp $(ARDUINO)/WMath.cpp"
FORMAT = "ihex"

# Debugging format.
# Native formats for AVR-GCC's -g are stabs [default], or dwarf-2.
# AVR (extended) COFF requires stabs, plus an avr-objcopy run.
DEBUG = "stabs"

OPT = "s"

# Place -D or -U options here
CDEFS = "-DF_CPU=$(F_CPU)"
CXXDEFS = "-DF_CPU=$(F_CPU)"

# Place -I options here
CINCS = "-I$(ARDUINO)"
CXXINCS = "-I$(ARDUINO)"

# Compiler flag to set the C Standard level.
# c89   - "ANSI" C
# gnu89 - c89 plus GCC extensions
# c99   - ISO C99 standard (not yet fully implemented)
# gnu99 - c99 plus GCC extensions
CSTANDARD = "-std=gnu99"
CDEBUG = "-g$(DEBUG)"
CWARN = "-Wall -Wstrict-prototypes"
CTUNING = "-funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums"
#CEXTRA = -Wa,-adhlns=$(<:.c=.lst)

CFLAGS = "$(CDEBUG) $(CDEFS) $(CINCS) -O$(OPT) $(CWARN) $(CSTANDARD) $(CEXTRA)"
CXXFLAGS = "$(CDEFS) $(CINCS) -O$(OPT)"
#ASFLAGS = -Wa,-adhlns=$(<:.S=.lst),-gstabs 
LDFLAGS = "-lm"

# Program settings
CC = "$(AVR_TOOLS_PATH)/avr-gcc"
CXX = "$(AVR_TOOLS_PATH)/avr-g++"
OBJCOPY = "$(AVR_TOOLS_PATH)/avr-objcopy"
OBJDUMP = "$(AVR_TOOLS_PATH)/avr-objdump"
AR  = "$(AVR_TOOLS_PATH)/avr-ar"
SIZE = "$(AVR_TOOLS_PATH)/avr-size"
NM = "$(AVR_TOOLS_PATH)/avr-nm"

REMOVE = "rm -f"
MV = "mv -f"

# Define all object files.
OBJ = "$(SRC:.c=.o) $(CXXSRC:.cpp=.o) $(ASRC:.S=.o)" 

# Define all listing files.
LST = "$(ASRC:.S=.lst) $(CXXSRC:.cpp=.lst) $(SRC:.c=.lst)"

# Combine all necessary flags and optional flags.
# Add target processor to flags.
ALL_CFLAGS = "-mmcu=$(MCU) -I. $(CFLAGS)"
ALL_CXXFLAGS = "-mmcu=$(MCU) -I. $(CXXFLAGS)"
ALL_ASFLAGS = "-mmcu=$(MCU) -I. -x assembler-with-cpp $(ASFLAGS)"
#
# Targets start here - the real conversion begins!
#
# Default target.
def BuildAll():
	BuildAppletFiles();
	Build();
	currsize = SizeAfter();
	
	return;
	
def BuildAppletFiles():

	return;

def Build():
	BuildElf();
	BuildHex();

	return;

def SizeAfter():

	return;

def BuildElf():

	return;

def BuildHex():

	return;
		
all: applet_files build sizeafter

build: elf hex 

applet_files: $(TARGET).pde
	# Here is the "preprocessing".
	# It creates a .cpp file based with the same name as the .pde file.
	# On top of the new .cpp file comes the WProgram.h header.
	# At the end there is a generic main() function attached.
	# Then the .cpp file will be compiled. Errors during compile will
	# refer to this new, automatically generated, file. 
	# Not the original .pde file you actually edit...
	test -d applet || mkdir applet
	echo '#include "WProgram.h"' > applet/$(TARGET).cpp
	cat $(TARGET).pde >> applet/$(TARGET).cpp
	cat $(ARDUINO)/main.cxx >> applet/$(TARGET).cpp

elf: applet/$(TARGET).elf
hex: applet/$(TARGET).hex

# Display size of file.
HEXSIZE = "$(SIZE) --target=$(FORMAT) applet/$(TARGET).hex"
ELFSIZE = "$(SIZE)  applet/$(TARGET).elf"
sizebefore:
	@if [ -f applet/$(TARGET).elf ]; then echo; echo $(MSG_SIZE_BEFORE); $(HEXSIZE); echo; fi

sizeafter:
	@if [ -f applet/$(TARGET).elf ]; then echo; echo $(MSG_SIZE_AFTER); $(HEXSIZE); echo; fi

.SUFFIXES: .elf .hex

.elf.hex:
	$(OBJCOPY) -O $(FORMAT) -R .eeprom $< $@


	# Link: create ELF output file from library.
applet/$(TARGET).elf: $(TARGET).pde applet/core.a 
	$(CC) $(ALL_CFLAGS) -o $@ applet/$(TARGET).cpp -L. applet/core.a $(LDFLAGS)

applet/core.a: $(OBJ)
	@for i in $(OBJ); do echo $(AR) rcs applet/core.a $$i; $(AR) rcs applet/core.a $$i; done



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
