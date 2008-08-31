# Arduino 0011 Makefile
# Arduino adaptation by mellis, eighthave, oli.keller, it.daniher
#
# This makefile allows you to build sketches from the command line
# without the Arduino environment (or Java).
# HEAVILY MODIFIED FROM STOCK VERSION!
# ONLY COMPILES SKETCH TO A .HEX FILE - Upload.sh needed to burn to AVR
# Supports only "make" and "make clean"

TARGET = Blink1
#Name of the .pde you're trying to compile
MCU = atmega168
#Name of the MCU in your arduino
F_CPU = 16000000
#hz of the MCU in your arduino
ARDHOME = /home/it/SOURCE/arduino
#Hacked-up Arduino Home
EXTRALIBDIR = extralibs
#Folder containing Servo/ etc.
BASELIBDIR = baselibs
#Folder containing the necessary libs, located normally in arduino-0011/hardware/cores/arduino
INC = 
#Name of the non-default library you want to use
############################################################################
# Below here nothing should be changed...

BASELIBS = $(ARDHOME)/baselibs
AVR_TOOLS_PATH = /usr/bin
SRC =  $(BASELIBS)/pins_arduino.c $(BASELIBS)/wiring.c \
$(BASELIBS)/wiring_analog.c $(BASELIBS)/wiring_digital.c \
$(BASELIBS)/wiring_pulse.c $(BASELIBS)/wiring_serial.c \
$(BASELIBS)/wiring_shift.c $(BASELIBS)/WInterrupts.c
CXXSRC = $(BASELIBS)/HardwareSerial.cpp $(BASELIBS/WMath.cpp $(ARDHOME)/$(EXTRALIBDIR)/$(INC)/$(INC).cpp
FORMAT = ihex

# Debugging format.
# Native formats for AVR-GCC's -g are stabs [default], or dwarf-2.
# AVR (extended) COFF requires stabs, plus an avr-objcopy run.
# DEBUG = stabs

OPT = s

# Place -D or -U options here
CDEFS = -DF_CPU=$(F_CPU)
CXXDEFS = -DF_CPU=$(F_CPU)

# Place -I options here
CINCS = -I$(BASELIBS)
CXXINCS = -I$(BASELIBS)

# Compiler flag to set the C Standard level.
# c89   - "ANSI" C
# gnu89 - c89 plus GCC extensions
# c99   - ISO C99 standard (not yet fully implemented)
# gnu99 - c99 plus GCC extensions
# CSTANDARD = -std=gnu99
CDEBUG = -g$(DEBUG)
CWARN = -Wall
CTUNING = -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums
#CEXTRA = -Wa,-adhlns=$(<:.c=.lst)

CFLAGS = $(CDEBUG) $(CDEFS) $(CINCS) -O$(OPT) $(CWARN) $(CSTANDARD) $(CEXTRA)
CXXFLAGS = $(CDEFS) $(CINCS) -O$(OPT)
#ASFLAGS = -Wa,-adhlns=$(<:.S=.lst),-gstabs 
LDFLAGS = -lm

# Program settings
CC = $(AVR_TOOLS_PATH)/avr-gcc
CXX = $(AVR_TOOLS_PATH)/avr-g++
OBJCOPY = $(AVR_TOOLS_PATH)/avr-objcopy
OBJDUMP = $(AVR_TOOLS_PATH)/avr-objdump
AR  = $(AVR_TOOLS_PATH)/avr-ar
SIZE = $(AVR_TOOLS_PATH)/avr-size
NM = $(AVR_TOOLS_PATH)/avr-nm
REMOVE = rm -f
MV = mv -f

# Define all object files.
OBJ = $(SRC:.c=.o) $(CXXSRC:.cpp=.o) $(ASRC:.S=.o) 

# Define all listing files.
LST = $(ASRC:.S=.lst) $(CXXSRC:.cpp=.lst) $(SRC:.c=.lst)

# Combine all necessary flags and optional flags.
# Add target processor to flags.
ALL_CFLAGS = -mmcu=$(MCU) -I. $(CFLAGS)
ALL_CXXFLAGS = -mmcu=$(MCU) -I. $(CXXFLAGS)
ALL_ASFLAGS = -mmcu=$(MCU) -I. -x assembler-with-cpp $(ASFLAGS)


# Default target.
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
	cat $(BASELIBS)/main.cxx >> applet/$(TARGET).cpp

elf: applet/$(TARGET).elf
hex: applet/$(TARGET).hex

# Display size of file.
HEXSIZE = $(SIZE) --target=$(FORMAT) applet/$(TARGET).hex
ELFSIZE = $(SIZE)  applet/$(TARGET).elf
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
