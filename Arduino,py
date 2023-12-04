import serial
import time

class Arduino:
    def __init__(self, port='COM10', baud_rate=115200, timeout=None):
        
        self.ser = serial.Serial(port, baud_rate, timeout=timeout)
        

    def get_sen(self):
        self.data = self.ser.readline().decode('utf-8').strip()

        self.data_list = [float(value) for value in self.data.split(',') if value]

        self.GPS_read(self.data_list)
        self.color_sensor(self.data_list)
        print(self.data)


    def GPS_read(self, list):
        
        self.a = list[0:2]


    def color_sensor(self,list):
        
        self.b = list[2:5]


x = Arduino()
x.get_sen()
print(x.b)
