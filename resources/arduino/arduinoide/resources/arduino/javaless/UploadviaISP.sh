PORT="/dev/ttyUSB*"
AVRDUDE_PROGRAMMER=stk500v2
MCU=atmega168
AVRDUDE=avrdude
TARGET=Graph

# Programming support using avrdude. Settings and variables.
AVRDUDE_PORT=$PORT
AVRDUDE_WRITE_FLASH="-U flash:w:applet/$TARGET.hex"
AVRDUDE_FLAGS=" -V -F -p $MCU -P $AVRDUDE_PORT -c $AVRDUDE_PROGRAMMER "

# Program the device.  
$AVRDUDE $AVRDUDE_FLAGS $AVRDUDE_WRITE_FLASH 
