#include "MovementController.h"
// #include "PID_v1.h"
// #include "Adafruit_BNO055.h"
// #include "Adafruit_Sensor.h"


// Instantiate a MotorController object.
MovementController robot = MovementController(2,3,4,5,6,7,8,9,10,11,12,13);

void setup() {
    
    Serial.begin(9600);

}

void loop(){

    // Read commands from Serial input.
    if (Serial.available() > 0) {

        
        String str = Serial.readString();           // Read the incoming data as a String.
        int str_len = str.length() + 1;             // Length (with one extra character for the null terminator)
        char char_array[str_len];                   // Prepare the character array (the buffer)
        str.toCharArray(char_array, str_len);       // Copy it over 
        char command = char_array[0];               // Get first char.

        // Apply command to motors.
        robot.move(command);
     }
}
