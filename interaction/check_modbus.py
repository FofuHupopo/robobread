import minimalmodbus


PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
STOPBITS = 1.5
PARITY = 'E'

instrument = minimalmodbus.Instrument(PORT, slaveaddress=1, mode='rtu')

instrument.serial.baudrate = BAUDRATE
instrument.serial.bytesize = 8
instrument.serial.parity = PARITY
instrument.serial.stopbits = STOPBITS

register_address = 0x0000
number_of_registers = 1


value = instrument.read_register(register_address, number_of_registers, functioncode=3)
print("Значение из регистра:", value)
