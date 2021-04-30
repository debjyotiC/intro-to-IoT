#include <ConsentiumThings.h>
#include "secrets.h"

#define AP_SSID "" // type in your SSID
#define AP_PASS "" // type in your password

void setup(){
  Serial.begin(115200); //baud rate for ESP8266 and Serial Monitor
  sendAT("AT","OK");
  sendAT("AT+CWMODE=3","OK");
  connectWiFi(AP_SSID,AP_PASS);
}

void loop(){
  sendAT("AT+CIPSTART=\"TCP\",\"192.168.1.6\",5000", "OK"); 

  double sensor_data = get_MPU_temp_data();
  String data_url = "GET /update?api_key="+write_key+"&field1="+String(sensor_data)+"\r\n\r\n";

  bool rstatus = sendAT("AT+CIPSEND="+String(data_url.length()),">");
  if(rstatus=true){
    sendAT(data_url,"OK");   
  }
  else{
    Serial.println("AT+CIPSEND error!");
  }
  sendAT("AT+CIPCLOSE=0","OK");
  delay(5000);
}
