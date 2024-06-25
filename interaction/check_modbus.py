from pymodbus.client.sync import ModbusSerialClient


client = ModbusSerialClient(method='rtu', port='COM4', baudrate=9600, timeout=1)

connection = client.connect()
if connection:
    print("Соединение установлено.")
    client.close()
else:
    print("Не удалось установить соединение.")
