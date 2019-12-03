import serial
import time
from math import pi
from threading import Thread
class mySerial(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.encoder = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=3.0)
        self.iden = open('datos.txt', 'w')
        self.setpoint = 0
        self.pulsos = 0
        self.tiempo = 0
        print('Estuve en el constructor')
    def data (self):
        return self.pulsos / 100, self.setpoint / 100
    
    def sendData(self, myData):
        self.encoder.write(myData.to_bytes(2, byteorder='little'))
    def stop(self):
        self.iden.close()
        self.encoder.close()
    def run(self):
       #while self.encoder.inWaiting:
       while True:
       
            DATA = []
            incoming = self.encoder.readline(3)
            incomings = str(incoming)
            self.tiempo = self.tiempo + 0.01
            if incomings == "b'FFF'":
                for i in range (2):
                    DATA.append(self.encoder.readline(2))
                self.setpoint = int.from_bytes(DATA[0], byteorder='little', signed = False)
                self.pulsos = int.from_bytes(DATA[1], byteorder='little', signed = False)
                #error = int.from_bytes(DATA[1], byteorder='big', signed = False)
                #PID_value = int.from_bytes(DATA[2], byteorder='big', signed = False)
                #tiempo = 5 * (int.from_bytes(DATA[3], byteorder='big', signed = False))
                #setpoint = int.from_bytes(DATA[4], byteorder='big', signed = False)
 
                #print(incoming)
                print(self.setpoint / 100, self.pulsos / 100)
                #if tiempo * 5 > 5:
                self.iden.write("{0:.2f}".format(self.tiempo))
                self.iden.write("\t")
                self.iden.write("{0:.2f}".format(self.setpoint / 100))
                self.iden.write("\t")
                #iden.write("\t")
                self.iden.write("{0:.2f}".format(self.pulsos / 100))
                self.iden.write("\t")
                self.iden.write("{0:.2f}".format(self.setpoint - self.pulsos))
                self.iden.write("\t")
                #iden.write("\t")
                #iden.write("\t")
                #iden.write("{0:.4f}".format(esc * pulsos))
                #iden.write("\t")
                #iden.write("\t")
                self.iden.write("\n")
