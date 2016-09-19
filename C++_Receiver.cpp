#include "btbee.h"
#include <algorithm>
#include "m3pi.h"

//Kevin Butler and Brent Marieb

//Define arrays for different directions
const char no_keys[1] = {0};
const char r[1] = {1};
const char l[1] = {2};
const char rl[1] = {3};
const char b[1] = {4};
const char br[1] = {5};
const char bl[1] = {6};

const char f[1] = {8};
const char fr[1] = {9};
const char fl[1] = {10};

const char fb[1] = {12};

int main()
{
    btbee mybtbee;
    
    //Define variable for read_all function
    char array[1];
    int a = 0;
    int *chars_read = &a;
    float speed = .25;
    float correction = 0.20;
    bool changed = false;
    
    m3pi m3pi;
    
    while(true)
    {
        while(mybtbee.readable())
        {
            //Read the byte array sent from python
            while(mybtbee.read_all(array, sizeof(array), chars_read))
            {
                 //Go through if/else if statements to find which keys have been pressed
                 //Move robot in direction indicated
                 if(array[0] == no_keys[0])
                 {
                     m3pi.printf("Stop");
                     m3pi.stop();
                 }
                 else if(array[0] == r[0])
                 {
                     m3pi.printf("Right");
                     m3pi.right_motor(speed);
                     m3pi.left_motor(0);
                 }
                else if(array[0] == l[0])
                 {
                     m3pi.printf("Left");
                     m3pi.left_motor(speed);
                     m3pi.right_motor(0);
                     
                 }
                
                 else if(array[0] == b[0])
                 {
                     m3pi.printf("backwards");
                     m3pi.backward(speed);
                 }
                 else if(array[0] == br[0])
                 {
                     m3pi.printf("back/right");
                      m3pi.right_motor(-speed);
                     m3pi.left_motor(-speed + correction);
                    
                 }
                 else if(array[0] == bl[0])
                 {
                     m3pi.printf("back/left");
                   
                    m3pi.left_motor(-speed);
                     m3pi.right_motor(-speed+ correction);
                 }
                 else if(array[0] == f[0])
                 {
                     m3pi.printf ("forward");
                     m3pi.forward(speed);
                 }
                 else if(array[0] == fr[0])
                 {
                    m3pi.right_motor(speed);
                     m3pi.left_motor(speed - correction);
                 }
                 else if(array[0] == fl[0])
                 {
                     
                      m3pi.right_motor(speed - correction);
                     m3pi.left_motor(speed);
                 }
                 else if(array[0] == fb[0])
                 {
                     m3pi.stop();
                 }
                 if(array[0] == 0)
                 {
                     changed = false;
                 }
                 else if(array[0] == 13 and changed == false)
                 {
                     speed += .05;
                     correction += .02;
                     changed = true;
                 }
                 else if(array[0] == 14 and changed == false)
                 {
                     speed -= .05;
                     correction -= .02;
                     changed = true;
                 }
            }
        }
    }
}
