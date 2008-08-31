PORT="/dev/ttyUSB*"
UPLOAD_RATE=19200
AVRDUDE_PROGRAMMER=stk500v1
MCU=atmega168
AVRDUDE=avrdude
TARGET=shtxx0

# Programming support using avrdude. Settings and variables.
AVRDUDE_PORT=$PORT
AVRDUDE_WRITE_FLASH="-U flash:w:applet/$TARGET.hex"
AVRDUDE_FLAGS=" -V -F -p $MCU -P $AVRDUDE_PORT -c $AVRDUDE_PROGRAMMER -b $UPLOAD_RATE"

# Program the device.  
$AVRDUDE $AVRDUDE_FLAGS $AVRDUDE_WRITE_FLASH 
