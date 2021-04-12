import serial
from time import sleep
import numpy as np
import pandas as pd


class ArduinoComm:
    sensor_data = []  # list to store sensor data
    count_arr = []  # count list

    def __init__(self, serialPort, baudRate):
        self.serialPort = serialPort
        self.baudRate = baudRate

    def connectWith(self, number, delay=1):
        ser = serial.Serial(self.serialPort, self.baudRate)
        for itr in range(0, number):
            self.sensor_data.append(float(ser.read(7).decode().strip()))
            self.count_arr.append(itr)
            print('.', end='')
            sleep(delay)
        print('\n')

    def calculateAverage(self):
        return np.average(self.sensor_data)

    def writeCSV(self, fileName):
        values = {"Count": self.count_arr, "Sensor_data": self.sensor_data}
        df_w = pd.DataFrame(values, columns=["Count", "Sensor_data"])
        df_w.to_csv(fileName, index=None, header=True)
