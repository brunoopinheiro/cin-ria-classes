const int ledPin = 8;
const int buttonIncrease = 2;
const int buttonDecrease = 4;
int delayTime = 500;
int increase = 0;
int decrease = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonIncrease, INPUT);
  pinMode(buttonDecrease, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  increase = digitalRead(buttonIncrease);
  decrease = digitalRead(buttonDecrease);
  if (increase == 1 && delayTime <= 2500) {
    delayTime = delayTime + 500;
  } else if (decrease == 1 && delayTime >= 1000) {
    delayTime = delayTime - 500;
  }
  Serial.println(delayTime);
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin, LOW);
  delay(delayTime);
}
