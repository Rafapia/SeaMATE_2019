/* 
 *  Motor.h - Individual motor controller class.
 *  Written by Rafael Piacsek.
 *  Mar 7, 2019.
 */


 #include "Arduino.h"
 #include "Motor.h"



// ##################################################################################################################################

// Define contructor method.
Motor::Motor(byte pinA, byte pinB, byte pinPWM, bool inverted) {

    // Store pins to private variables.
    _pinA = pinA;
    _pinB = pinB;
    _pinPWM = pinPWM;

    // Store default direction;
    _inverted = inverted;

    // Set the pinModes for all of them.
    pinMode(_pinA, OUTPUT);
    pinMode(_pinB, OUTPUT);
    pinMode(_pinPWM, OUTPUT);

    // Set initial direction to FORWARD.
    setDirection(FORWARD);
    
}


// ##################################################################################################################################

// Define default contructor method.
Motor::Motor() {

    // Don't do anything for default constructor.
}


// ##################################################################################################################################

// Define setDirection method.
void Motor::setDirection(bool direction) {

    if (direction==FORWARD) {                   // Set pins A and B for FORWARD motion.
        digitalWrite(_pinA, _inverted);
        digitalWrite(_pinB, !_inverted);
    } else if (direction==BACKWARD) {           // Set pins A and B for BACKWARD motion.
        digitalWrite(_pinA, !_inverted);
        digitalWrite(_pinB, _inverted);
    }
}


// ##################################################################################################################################

// Define setSpeed method.
void Motor::setSpeed(float speed) {

    _speed = constrain(speed, -1, 1) * 255;     // Input should range between -1 and 1. Nevertheless, constrain the value and rescale to -255 to 255 for PWM.

    if (_speed > 0) {                           // Forward.
        setDirection(FORWARD);
        analogWrite(_pinPWM, abs(_speed));
    } else if (_speed < 0) {                    // Backward.
        setDirection(BACKWARD);
        analogWrite(_pinPWM, abs(_speed));
    } else {                                    // Brake.
        stop();
    }
}


// ##################################################################################################################################

// Define setSpeed method.
void Motor::stop() {

    _speed = 0;                                 // Reset _speed variable.

    digitalWrite(_pinA, HIGH);                  // Brake motor.
    digitalWrite(_pinB, HIGH);
    analogWrite(_pinPWM, 0);                    // Reset PWM.
}


// ##################################################################################################################################

// Define getSpeed method.
float Motor::getSpeed() {

    return _speed;
}
