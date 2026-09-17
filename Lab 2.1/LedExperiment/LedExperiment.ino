void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  double TotalVoltageIn = analogRead(A0) * 5.0/1023;
  double DiodeVoltageIn = analogRead(A1) * 5.0/1023;


  double VoltageDropResistor = (TotalVoltageIn - DiodeVoltageIn);
  double CurrentAcrossResistor = VoltageDropResistor * 1000 / 330;
  
  Serial.print("TotalVoltageIn:");
  Serial.print(TotalVoltageIn);
  Serial.print(",");
  Serial.print("DiodeVoltageIn:");
  Serial.print(DiodeVoltageIn);
  Serial.print(",");
  Serial.print("CurrentAcrossResistor:");
  Serial.println(CurrentAcrossResistor);
  delay(100);
}
