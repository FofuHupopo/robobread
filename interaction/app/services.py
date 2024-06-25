import minimalmodbus

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
        pass

    def disconnect(self):
        pass

    def write_registers(self, register, values):
        self.instrument.write_registers(register, values, functioncode=16)

    def sell_item(self, cell_number):
        sell_command = [0x10, 0x10, 0x00, 0x00, 0x01, 0x02, 0x00, cell_number, 0x00, 0x00]
        self.write_registers(16, sell_command)
