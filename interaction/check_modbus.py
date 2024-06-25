from pymodbus.client.serial import ModbusSerialClient


client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', stopbits=1.5, bytesize=8, parity='E', baudrate=9600, timeout=1)

connection = client.connect()
if connection:
    print("Соединение установлено.")
    client.close()
else:
    print("Не удалось установить соединение.")
