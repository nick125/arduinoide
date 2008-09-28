avrdude -p m168 -b 115200 -P usb -c avrispmkII -V -e -U lock:w:0×3F:m -U hfuse:w:0xDF:m -U lfuse:w:0xFF:m -U efuse:w:0×0:m
avrdude -p m168 -b 115200 -P usb -c avrispmkII -V -D -U flash:w:ATmegaBOOT_168.hex
avrdude -p m168 -b 115200 -P usb -c avrispmkII -V -U lock:w:0xCF:m