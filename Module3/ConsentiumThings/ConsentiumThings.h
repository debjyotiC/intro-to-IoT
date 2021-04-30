#ifndef ConsentiumThings_h
#define ConsentiumThings_h

#include <Arduino.h>          

double get_MPU_temp_data();
void connectWiFi(String ssid, String password);
bool sendAT(String command,char response[]);

#endif


