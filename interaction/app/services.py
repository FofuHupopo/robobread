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
        initial_command = [0x01, 0x06, 0x10, 0x08, 0x00, 0x01, 0xCD, 0x08]
        
        self.write_registers(16, initial_command)

    def disconnect(self):
        pass

    def write_registers(self, register, values):
        self.instrument.write_registers(register, values, functioncode=16)

    def sell_item(self, cell_number):
        sell_command = [0x01, 0x10, 0x10, 0x00, 0x00, 0x01, 0x02, 0x00, cell_number]
        sell_command.extend(self.calculate_crc16_modbus(sell_command))
        dispense_command = [0x01, 0x06, 0x10, 0x06, 0x00, 0x01, 0xAC, 0xCB]

        commands = [sell_command, dispense_command]

        for command in commands:
            self.write_registers(16, command)
            time.sleep(1)

    def calculate_crc16_modbus(self, data):
        crc = 0xFFFF
        polynomial = 0xA001

        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ polynomial
                else:
                    crc >>= 1

        return crc.to_bytes(2, byteorder='little')
