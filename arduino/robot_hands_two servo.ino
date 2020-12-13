// 아두이노 우노 보드의 하드웨어 시리얼 포트(0, 1)를 사용합니다. 

#include <Servo.h>

Servo finger1;  
Servo finger2;


void setup() {
  finger1.attach(11);  
  finger2.attach(10);
  Serial.begin(9600);

  //initialize
  finger1.write(0);
  finger2.write(0);
  delay(100); 
}



void loop() {  
  if (Serial.available()) {
    char input = Serial.read();
    
    if (input == 'a') {
      paper();
    } else if (input == 'b') {
      scissors();
    } else if (input == 'c') {
      rock();
    }
  }
}


void rock() {
  finger1.write(0);
  finger2.write(0);
  delay(100);  
}

void paper() {
  finger1.write(180);
  finger2.write(180);
  delay(100);  
}

void scissors() {
  finger1.write(0);
  finger2.write(180);
  delay(100);  
}
