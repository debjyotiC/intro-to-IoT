int lm_35 = A0;  // sensor Pin
int led_pin = 13;  // lED pin 

void setup() {
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int val = 0, val_avg = 0;
  
  for(register int i = 0; i<=10; i++){
    val = val + analogRead(lm_35);
  }
  val_avg = val/10;
  
  float mv = (val_avg/1023.0)*5;
  float temp_C = mv/0.01;
  
  Serial.println(temp_C);
  
  if(temp_C > 35){
    digitalWrite(led_pin, HIGH);
    Serial.println("LED on");
  }
  else{
    digitalWrite(led_pin, LOW);
    Serial.println("LED off");
  }
  
  delay(1000);   // 1s delay
}
