from serial import Serial
import pandas as pd

class espData:
    def __init__(self, esp_port, esp_baud):
        self.__sr = None
        self.__esp_port = esp_port
        self.__esp_baud = esp_baud
        self.__esp_data_list, self.__esp_data_pos = [], []

    def initSerial(self):
        self.__sr = Serial(self.__esp_port, self.__esp_baud)

    def readSerial(self, num_data_points=10):
        for i in range(num_data_points):
            esp_data = float(self.__sr.readline().strip().decode())
            self.__esp_data_list.append(esp_data)
            self.__esp_data_pos.append(i)
            print(f"Sensor data at pos {i}:", esp_data)

    def writeCSV(self, csv_file="esp_data.csv"):
        data_frame = {"Count": self.__esp_data_pos, "Data": self.__esp_data_list}
        df = pd.DataFrame(data_frame, index=None, columns=["Count", "Data"])
        df.to_csv(csv_file)
        print("Saved csv file!")
