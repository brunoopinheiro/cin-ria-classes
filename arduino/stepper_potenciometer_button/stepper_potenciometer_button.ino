#include <Stepper.h>

const int potPin = A5;
const int MOTOR = 9;
const int buttonPin = 11;
const int halfStepRevolution = 32;
Stepper myStepper(halfStepRevolution, 8, 10, 9, 11);  // pinos?
int sensorValue = 0;
int buttonState = LOW;
int convertedValue = 0;
int direction = 1;

void swapDirection() {
  if (direction == 1) {
    direction = -1;
  } else {
    direction = 1;
  }
}

void giraMotor(int sentido) {
  for (int i = 0; i<64; i++) {
    myStepper.step(halfStepRevolution * sentido);
  }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(potPin, INPUT);
  pinMode(buttonPin, INPUT);
  pinMode(MOTOR, OUTPUT);
  myStepper.setSpeed(120);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    swapDirection();
  }
  sensorValue = analogRead(potPin);
  convertedValue = map(sensorValue, 0, 1023, 0, 255);  // 0-255 padrao PWM
  myStepper.setSpeed(convertedValue);
  giraMotor(direction);
}
