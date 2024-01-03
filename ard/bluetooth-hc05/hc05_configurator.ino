// Filename: hc05_configurator.ino
// This code enables the HC05 bluetooth module to be configured using AT commands
// Refer to the AT command list in the same directory folder for more information
// Also see the markdown file in the same directory to see how the module has been configured

/*
 *
 * Auth: Kimeu Dominic
 * Date: 2023-12-21
 * Desc: Configures the HC05 bluetooth module
 * github: kimeudom
 *
 */

#include <SoftwareSerial.h>
//HCO5 address: 98D3:71:F6EFD1
// +CMODE:1 (One to One)
// +ROLE:0 (Slave)
// +NAME:HC05
// +ADDR:98D3:71:F6EFD1
// Set the UART Rx and Tx pins

SoftwareSerial BTSerial(10, 11); // Tx, Rx

void setup()
{
  pinMode(9, OUTPUT); // Setting the enable pin high to configure and debug the module
  digitalWrite(9, HIGH);

  // 38.4k baud rate is the default baud rate for the HC05 module
  Serial.begin(38400);   // Setting the baud rate for the serial monitor
  BTSerial.begin(38400); // Setting the baud rate for the HC05 module

  Serial.println("Starting configuration of HC05 module");
  Serial.println("Enter AT Commands: ");
}

void loop()
{

  // Send from Computer -> HC05
  if (Serial.available())
  {
    BTSerial.write(Serial.read());
  }

  // Send from HC05 -> Computer
  if (BTSerial.available())
  {
    Serial.write(BTSerial.read());
  }
}