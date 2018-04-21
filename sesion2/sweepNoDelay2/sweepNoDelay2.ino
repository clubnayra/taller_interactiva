#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 

Servo myservo2;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 

int pos = 0;    // variable to store the servo position 
long previous = 0;
long interval = 15;


int pos2 = 0;    // variable to store the servo position 
long previous2 = 0;
long interval2 = 25;

int sentido = HIGH;
int sentido2 = HIGH;

void setup() 
{ 
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object 
  myservo2.attach(4);  // attaches the servo on pin 9 to the servo object 
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
    if(current - previous2 > interval2)
    {
        previous2 = current;
        if(sentido2)
        {
            pos2++;
            if(pos2 >= 180)
            {
                sentido2 = !sentido2;
            }
        }
        else
        {
            pos2--;
            if(pos2 <= 0)
            {
                sentido2 = !sentido2;
            }
        }
        myservo2.write(pos2);
    } 
} 
