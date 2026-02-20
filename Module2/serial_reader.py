from serial import Serial
import pandas as pd

esp_port = '/dev/cu.usbmodem1101'
esp_baud = 9600
num_data_points = 10
esp_data_file = "esp_data.csv"

esp_data_list, esp_data_pos = [], []

sr = Serial(esp_port, esp_baud)

for i in range(num_data_points):
    esp_data = float(sr.readline().strip().decode())
    esp_data_list.append(esp_data)
    esp_data_pos.append(i)
    # print(f"Sensor data at pos {i}:", esp_data)
    # print("=", end=">")

data_frame = {"Count": esp_data_pos, "Data": esp_data_list}

df = pd.DataFrame(data_frame)

df.to_csv(esp_data_file)

print("Saved csv file!")
