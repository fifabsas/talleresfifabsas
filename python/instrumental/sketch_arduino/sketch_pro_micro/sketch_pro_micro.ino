#define NUM_READINGS 128
#define STEP_PIN 10
#define SENSOR_PIN A0

uint32_t times[NUM_READINGS];
uint16_t values[NUM_READINGS];
uint16_t refValues[NUM_READINGS];

void setup() {
 //ADCSRA=(ADCSRA&0xF80)|0x05; //Permite tener más muestras por segundo
 analogWrite(STEP_PIN, 127);
 Serial.begin(9600);
}

void loop() {
  uint32_t startTime = micros();
  digitalWrite(STEP_PIN, HIGH);
  
  int i = 0;
  for(; i < NUM_READINGS / 2; i++) {
    times[i] = micros() - startTime;
    values[i] = analogRead(SENSOR_PIN);
  }
  digitalWrite(STEP_PIN, LOW);
  for(; i < NUM_READINGS; i++) {
    times[i] = micros() - startTime;
    values[i] = analogRead(SENSOR_PIN);;
  }
   if (Serial.available() > 0) {
    Serial.read();
    for(int i = 0; i < NUM_READINGS; i++) {
      Serial.print(times[i]);
      Serial.print("\t");
      Serial.println(values[i]);
    }
   }

}
