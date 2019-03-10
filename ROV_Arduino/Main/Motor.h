/* 
 *  Motor.h - Individual motor controller class.
 *  Written by Rafael Piacsek.
 *  Mar 7, 2019.
 */

 #ifndef Motor_h
 #define Motor_h

 #include "Arduino.h"


 // Define the class.
 class Motor {

    private:

        byte _pinA, _pinB, _pinPWM;         // Holds the ports for each H-Bridge.
        float _speed;                        // Holds the speed at which the motor shuold be running (0-1).
        bool _inverted;

    public:

        // Definitions.
        #define FORWARD true
        #define BACKWARD false
        #define NORMAL false
        #define INVERTED true

        // Constructor.
        Motor();
        Motor(byte pinA, byte pinB, byte pinPWM, bool inverted);

        // Methods.
        void setDirection(bool direction);
        void setSpeed(float speed);
        void stop();

        float getSpeed();
 };

 #endif
