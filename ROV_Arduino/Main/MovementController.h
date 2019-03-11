/* 
 *  MovementController.h - Controls the behavior of all motors to achieve a specific movement.
 *  Written by Rafael Piacsek.
 *  Mar 7, 2019.
 *  
 *  This class is responsible for handling all motors to achieve a desired move.
 *  
 */


 #ifndef MovementController_h
 #define MovementController_h


#include "Arduino.h"
#include "Motor.h"

// Define the MovementController class.
class MovementController {

    private:

        // The array that holds all of the Motor objects.
        Motor motors[4];

        

    public:

        // Definitions.
        #define FL_MOTOR 0
        #define FR_MOTOR 1
        #define BL_MOTOR 2
        #define BR_MOTOR 3
//        #define TL_MOTOR 4
//        #define TR_Motor 5

        // Constructor method.
        MovementController(byte FL_A, byte FL_B, byte FL_PWM, byte FR_A, byte FR_B, byte FR_PWM, byte BL_A, byte BL_B, byte BL_PWM, byte BR_A, byte BR_B, byte BR_PWM);


        // Methods.
        void move(char dir);            // Triggers the movement of all motors accordingly.
        void stopAll();                 // Brakes all motors.
    
};


 #endif
