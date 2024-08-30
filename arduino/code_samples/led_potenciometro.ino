const int ledPin = 9;
const int sensorPin = A0;
int sensorValue = 0;

int returnPotValue(int value) {
  return map(value, 0, 1023, 0, 255);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(sensorPin);
  const int sensorPot = returnPotValue(sensorValue);
  analogWrite(ledPin, sensorPot);
}
