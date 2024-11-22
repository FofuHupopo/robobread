import minimalmodbus
import time


instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_EVEN
instrument.serial.stopbits = 1.5
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_RTU

instrument.write_register(0x1008, 0x0001, functioncode=6)

time.sleep(10)

instrument.write_registers(0x1000, [0x000a])

time.sleep(1)

instrument.write_register(0x1006, 0x0001, functioncode=6)
