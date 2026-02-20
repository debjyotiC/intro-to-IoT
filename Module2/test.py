from serial_class import espData

myEsp = espData(esp_port = '/dev/cu.usbmodem1101', esp_baud = 9600)
myEsp.initSerial()
myEsp.readSerial(num_data_points=20)
myEsp.writeCSV(csv_file='test.csv')

