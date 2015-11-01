#define DIFF
#ifdef INT
  #define STEP_PIN 23
  #define SENSOR_PIN 22
  #define SENSOR_STEP_PIN 21
#endif

#ifdef DIFF
  #define STEP_PIN 20
  #define SENSOR_PIN 19
  #define SENSOR_STEP_PIN 18
#endif

#define NUM_READINGS 100

uint16_t valuesC[NUM_READINGS];
uint16_t valuesR[NUM_READINGS];
uint32_t times[NUM_READINGS];


void setup() {
  Serial.begin(115200);
  analogWriteFrequency(STEP_PIN, 1000); 
  analogWrite(STEP_PIN, 127);
  
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  for (int i = 0; i < NUM_READINGS; i++) {

    valuesC[i] = analogRead(SENSOR_PIN);
    valuesR[i] = analogRead(SENSOR_STEP_PIN);
    times[i] = micros();
  }
  if (Serial.available() > 0) {
    Serial.read();
    for (int i = 0; i < NUM_READINGS; i++) {
      uint16_t valueC = analogRead(SENSOR_PIN);
      uint16_t valueR = analogRead(SENSOR_STEP_PIN);
      Serial.print(micros());
      Serial.print("\t");
      Serial.print(valueR);
      Serial.print("\t");
      Serial.println(valueC);
    }
  }

}


