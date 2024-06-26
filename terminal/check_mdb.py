import serial


ser = serial.Serial('COM1', 9600, timeout=1)

command = b'\x02PAY\x03'
ser.write(command)

response = ser.read(10)

print("Response from terminal:", response)

ser.close()
