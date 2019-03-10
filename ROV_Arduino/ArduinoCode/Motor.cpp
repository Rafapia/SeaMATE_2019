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

    // Store direction;
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

    // Store pins to private variables.
    _pinA = 0;
    _pinB = 0;
    _pinPWM = 0;

    // Store direction;
    _inverted = NORMAL;
}


// ##################################################################################################################################

// Define setDirection method.
void Motor::setDirection(bool direction) {

    if (direction==FORWARD) {
        digitalWrite(_pinA, _inverted);
        digitalWrite(_pinB, !_inverted);
    } else if (direction==BACKWARD) {
        digitalWrite(_pinA, !_inverted);
        digitalWrite(_pinB, _inverted);
    }
}


// ##################################################################################################################################

// Define setSpeed method.
void Motor::setSpeed(float speed) {

    _speed = constrain(speed, -1, 1) * 255;

    if (_speed > 0) {
        setDirection(FORWARD);
        analogWrite(_pinPWM, abs(_speed));
    } else if (_speed < 0) {
        setDirection(BACKWARD);
        analogWrite(_pinPWM, abs(_speed));
    } else {
        stop();
    }
}


// ##################################################################################################################################

// Define setSpeed method.
void Motor::stop() {

    _speed = 0;

    digitalWrite(_pinA, HIGH);
    digitalWrite(_pinB, HIGH);
    analogWrite(_pinPWM, 0);
}


// ##################################################################################################################################

// Define getSpeed method.
float Motor::getSpeed() {

    return _speed;
}
