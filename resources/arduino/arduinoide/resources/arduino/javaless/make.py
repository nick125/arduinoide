extralibdir="extralibs"
baselibdir="baselibs"
ardhome="/home/it/SOURCE/arduino"
baselibs = ardhome+"/baselibs"
avr_tools_path = "/usr/bin"
SRC =  $(BASELIBS)/pins_arduino.c $(BASELIBS)/wiring.c \
$(BASELIBS)/wiring_analog.c $(BASELIBS)/wiring_digital.c \
$(BASELIBS)/wiring_pulse.c $(BASELIBS)/wiring_serial.c \
$(BASELIBS)/wiring_shift.c $(BASELIBS)/WInterrupts.c
CXXSRC = $(BASELIBS)/HardwareSerial.cpp $(BASELIBS)/WMath.cpp $(ARDHOME)/$(EXTRALIBDIR)/$$
FORMAT = ihex

def make(target,mcu,f_cpu):
	