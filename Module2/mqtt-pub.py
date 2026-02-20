# import paho.mqtt.client as mqtt
#
# client = mqtt.Client()
# client.connect("broker.hivemq.com", 1883, 60)
# sensor_data_temp = 24.3
# client.publish('topic/test/temp', sensor_data_temp)
# client.disconnect()


class Employee:
  def __init__(self, name, phone, emp_code):
    self.name = name
    self.phone = phone
    self.emp_code = emp_code

  def __str__(self):
    return f"Employee name {self.name}"

emp1 = Employee("Deb", 993344, 400)
emp2 = Employee("Alice", 898989, 401)

print(emp1)
print(emp2)
