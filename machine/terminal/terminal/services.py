import serial


class MDBService:
    def __init__(self, port) -> None:
        self.client = serial.Serial(port, 9600, timeout=1)

    def connect(self):
        pass
    
    def disconnect(self):
        pass
