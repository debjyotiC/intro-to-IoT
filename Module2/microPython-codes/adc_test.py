import machine
import utime
 
analog_value = machine.ADC(28)
 
while True:
    reading = (analog_value.read_u16()/65025)*(3.3*1000)/10    
    print("ADC: ",reading)
    utime.sleep(0.2)