const int red = 13;
const int blue = 12;
const int green = 11;


void setup() {
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char input = Serial.read();
    
    if (input == 'a') {
      digitalWrite(red, HIGH);
      delay(100);
      digitalWrite(red, LOW);
    } else if (input == 'b') {
      digitalWrite(blue, HIGH);
      delay(100);
      digitalWrite(blue, LOW);
    } else if (input == 'c') {
      digitalWrite(green, HIGH);
      delay(100);
      digitalWrite(green, LOW);
    }
  }
}
