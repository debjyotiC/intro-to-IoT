from Module2.serial_class import ArduinoComm

myObj = ArduinoComm(serialPort='', baudRate=115200)
myObj.connectWith(number=7, delay=2)

print("The avg. is: {avg:.2f}".format(avg=myObj.calculateAverage()))

myObj.writeCSV('results.csv')
