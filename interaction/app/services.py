import serial
from pymodbus.client.serial import ModbusSerialClient


class ModbusService:
    def __init__(self, port, address):
        self.serial_port = serial.serial_for_url(f'modbusRTU:{port}', baudrate=9600, bytesize=8, parity='N', stopbits=serial.STOPBITS_ONE_POINT_FIVE, timeout=1)
        self.client = ModbusSerialClient(method='rtu', port=self.serial_port, timeout=1, stopbits=1.5, baudrate=9600)
        self.address = address

    def connect(self):
        if not self.client.connect():
            raise ConnectionError('Failed to connect to the modbus device')

    def disconnect(self):
        self.client.close()

    def write_registers(self, register, values):
        self.client.write_registers(register, values, unit=self.address)

    def sell_item(self, cell_number):
        sell_command = [0x10, 0x10, 0x00, 0x00, 0x01, 0x02, 0x00, cell_number, 0x00, 0x00]
        self.write_registers(16, sell_command)
