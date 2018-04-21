#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
long previous = 0;
long interval = 15;

int sentido = HIGH;
void setup() 
{ 
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object 
} 
 
 
void loop() 
{ 

    unsigned long current = millis();
    if(current - previous > interval)
    {
        previous = current;
        if(sentido)
        {
            pos++;
            if(pos >= 180)
            {
                sentido = !sentido;
            }
        }
        else
        {
            pos--;
            if(pos <= 0)
            {
                sentido = !sentido;
            }
        }
        myservo.write(pos);
    } 
} 
