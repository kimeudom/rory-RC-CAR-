#include <AFMotor.h>

// Motors
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup()
{
  // initialise communication
  Serial.begin(115200)
}

void loop()
{
  // Check for incoming serial data
  if (Serial.available() > 0)
  {
    incomingData = Serial.read();

    if (incomingData == 'F')
    {
      // Run foward function
      Serial.println("Foward")
    }
    if (incomingData == 'S')
    {
      // Run foward function
      Serial.println("Stop")
    }
    if (incomingData == 'L')
    {
      // Run foward function
      Serial.println("Foward")
    }
    if (incomingData == 'F')
    {
      // Run foward function
      Serial.println("Foward")
    }
  }
}