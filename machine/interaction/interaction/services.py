import minimalmodbus
import time


class ModbusService:
    def __init__(self, port, address):
        self.instrument = minimalmodbus.Instrument(port, address)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1.5
        self.instrument.serial.timeout = 1
        self.instrument.mode = minimalmodbus.MODE_RTU

    def connect(self):
        self.instrument.write_register(0x1008, 0x0001, functioncode=6)

    def disconnect(self):
        pass

    def write_registers(self, register, values):
        self.instrument.write_registers(register, values, functioncode=16)

    def sell_item(self, cell_number):
        self.instrument.write_registers(0x1000, [cell_number])

        time.sleep(1)

        self.instrument.write_register(0x1006, 0x0001, functioncode=6)
