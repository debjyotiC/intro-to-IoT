#include <ConsentiumThings.h>

double get_MPU_temp_data(){
  unsigned int wADC;
  double t;
  ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
  ADCSRA |= _BV(ADEN);  
  delay(20);            
  ADCSRA |= _BV(ADSC);  
  while (bit_is_set(ADCSRA,ADSC));
  wADC = ADCW;
  t = (wADC - 324.31 ) / 1.22;
  return t;
}
void connectWiFi(String ssid, String password){
  String cmd="AT+CWJAP=\"";//join access point
  cmd+=ssid;
  cmd+="\",\"";
  cmd+=password;
  cmd+="\"";
  Serial.println(cmd);
  delay(1000); //it takes some time to connect to WiFi and get an IP address
}

bool sendAT(String command,char response[]){
  Serial.println(command);
  delay(1000);
  if(Serial.find(response)){
    return true;
    }
  else
    return false;  
}

