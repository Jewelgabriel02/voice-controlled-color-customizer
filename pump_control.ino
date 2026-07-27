int m1 = 11; // Motor for Red paint
int m2 = 10; // Motor for Green paint
int m3 = 9;  // Motor for Blue paint
int m4 = 12;  // Motor for mixing paint

void setup() {
  Serial.begin(9600); // Start serial communication

  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(m3, OUTPUT);
  pinMode(m4, OUTPUT);

  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
}
void loop() {
  // Check if data is available on the serial port
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); // Read the serial data until newline
    data.trim(); // Remove any leading/trailing whitespace

    if (data.startsWith("red:")) {
      pumpPaint(m1, "Red", data.substring(4).toInt());
    } else if (data.startsWith("green:")) {
      pumpPaint(m2, "Green", data.substring(6).toInt());
    } else if (data.startsWith("blue:")) {
      pumpPaint(m3, "Blue", data.substring(5).toInt());
    } else {
      Serial.println("Invalid command");
    }
  }
}

void pumpPaint(int motorPin, String color, int amount) {
//  Serial.print("Pumping ");
//  Serial.print(color);
//  Serial.print(" paint: ");
//  Serial.print(amount);
//  Serial.println(" ml");

  // Calculate duration to pump the specified amount (5 ml in 3 seconds => 0.6 seconds/ml)
  int pumpTime = amount * 1000; // Time in milliseconds

  digitalWrite(motorPin, HIGH); // Turn on the motor
  delay(pumpTime);              // Wait for the required time
  digitalWrite(motorPin, LOW);  // Turn off the motor
  
  //mixing paint
  digitalWrite(m4, HIGH); // Turn on the motor
  delay(5000); 
  digitalWrite(m4, LOW);  // Turn off the motor
  
  Serial.println("Successfully pumped paint");
}







        
