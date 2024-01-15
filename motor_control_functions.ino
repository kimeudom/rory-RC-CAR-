#include <AFMotor.h>

AF_DCMotor motor1(1, MOTOR12_64KHZ); // create motor #2, 64KHz pwm
AF_DCMotor motor2(2, MOTOR12_64KHZ);
AF_DCMotor motor3(3, MOTOR12_64KHZ);
AF_DCMotor motor4(4, MOTOR12_64KHZ);

void moveforward()
{
  motor1.setSpeed(255);     // set the speed to 200/255
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255);

  motor1.run(FORWARD);      
  motor2.run(FORWARD);      
  motor3.run(FORWARD);      
  motor4.run(FORWARD); 
}
void turnleft()
{
  motor1.setSpeed(255);     // set the speed to 200/255
  motor2.setSpeed(112);
  motor3.setSpeed(255);
  motor4.setSpeed(255); 

  motor1.run(FORWARD);      
  motor2.run(FORWARD);      
  motor3.run(FORWARD);      
  motor4.run(FORWARD); 
}
void turnright()
{
  motor1.setSpeed(112);     // set the speed to 200/255
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255); 

  motor1.run(FORWARD);      
  motor2.run(FORWARD);      
  motor3.run(FORWARD);      
  motor4.run(FORWARD);  
}

void movebackward()
{
  motor1.setSpeed(255);     // set the speed to 200/255
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255); 

  motor1.run(BACKWARD);       
  motor2.run(BACKWARD);      
  motor3.run(BACKWARD);     
  motor4.run(BACKWARD); 
}

void stopMovement()
{
   motor1.run(RELEASE);      // stopped
   motor2.run(RELEASE);      // stopped
   motor3.run(RELEASE);      // stopped
   motor4.run(RELEASE);      // stopped  
}


void setup() {

}


void loop() {  
  moveforward();
  delay(10000);

  turnright();
  delay(10000);

  turnleft();
  delay(30000);
}