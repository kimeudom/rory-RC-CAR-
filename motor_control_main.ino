#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX, TX pins respectively

void setup()
{
  Serial.begin(38400);   // Baud rate for the serial monitor
  BTSerial.begin(38400); // Baud rate for the HC05 module
  pinMode(4, OUTPUT);    // Motor pin for forward movement
  pinMode(5, OUTPUT);    // Motor pin for left movement
  pinMode(6, OUTPUT);    // Motor pin for right movement
  pinMode(7, OUTPUT);    // Motor pin for stopping
}

void loop()
{
  if (BTSerial.available())
  {
    String instruction = BTSerial.readStringUntil('\n'); // Read the incoming data from Bluetooth

    // Perform actions based on the received instructions
    if (instruction == "forward")
    {
      moveForward();
    }
    else if (instruction == "left")
    {
      moveLeft();
    }
    else if (instruction == "right")
    {
      moveRight();
    }
    else if (instruction == "stop")
    {
      stopMovement();
    }
  }
}

// Functions to perform respective actions
void moveForward()
{
  // Impliment code here
  Serial.println("Moving forward");
}

void moveLeft()
{
  Serial.println("Moving left");
}

void moveRight()
{
  Serial.println("Moving right");
}

void stopMovement()
{
  Serial.println("Stopping movement");
}
