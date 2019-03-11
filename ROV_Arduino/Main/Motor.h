/* 
 *  Motor.h - Individual motor controller class.
 *  Written by Rafael Piacsek.
 *  Mar 7, 2019.
 *
 *  This class is responsible for controlling one Brushed DC Motor through an H-Bridge.
 * 
 */

 #ifndef Motor_h
 #define Motor_h

 #include "Arduino.h"


 // Define the class.
 class Motor {

    private:

        byte _pinA, _pinB, _pinPWM;         // Holds the ports for each H-Bridge.
        float _speed;                       // Holds the speed at which the motor shuold be running (0-1).
        bool _inverted;                     // Holds whether the motor is inverted or not.

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
        void setDirection(bool direction);          // Sets the appropriate direction of the motor, as PWM signals only have positive values.
        void setSpeed(float speed);                 // Sets the PWM signal after switching to appropriate direction.
        void stop();                                // Brakes the motor.

        float getSpeed();                           // Getter for the _speed variable.
 };

 #endif
