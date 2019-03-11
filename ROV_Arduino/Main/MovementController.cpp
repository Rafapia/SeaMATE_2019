/* 
 *  MovementController.cpp - Controls the behavior of all motors to achieve a specific movement.
 *  Written by Rafael Piacsek.
 *  Mar 7, 2019.
 */


 #include "Arduino.h"
 #include "MovementController.h"
 #include "Motor.h"


// ##################################################################################################################################

// Define contructor method.
MovementController::MovementController(byte FL_A, byte FL_B, byte FL_PWM, byte FR_A, byte FR_B, byte FR_PWM, byte BL_A, byte BL_B, byte BL_PWM, byte BR_A, byte BR_B, byte BR_PWM) {

    // Create one Motor object instance per motor and place them into the motors array.
    motors[0] = Motor(FL_A, FL_B, FL_PWM, NORMAL);
    motors[1] = Motor(FR_A, FR_B, FR_PWM, NORMAL);
    motors[2] = Motor(BL_A, BL_B, BL_PWM, NORMAL);
    motors[3] = Motor(BR_A, BR_B, BR_PWM, NORMAL);
    
}


// ##################################################################################################################################

// Define move method.
void MovementController::move(char dir) {


    // For the prototype, controls are limited to W A S D movements, and turns with Q (counterclockwise) and E (clockwise).
    switch (dir) {

        case 'w':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Forward");
            break;

        case 'a':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Left");
            break;

        case 's':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Backward");
            break;

        case 'd':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Right");
            break;

        case 'q':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Right");
            break;

        case 'e':
            motors[FL_MOTOR].setSpeed(1);
            motors[FR_MOTOR].setSpeed(1);
            motors[BL_MOTOR].setSpeed(1);
            motors[BR_MOTOR].setSpeed(1);
            Serial.println("Right");
            break;

        default:
            motors[FL_MOTOR].stop();
            motors[FR_MOTOR].stop();
            motors[BL_MOTOR].stop();
            motors[BR_MOTOR].stop();
            Serial.println("Stop");
            break;
    }
    
}
