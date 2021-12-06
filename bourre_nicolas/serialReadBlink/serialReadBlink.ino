#include "SafeString.h"

// constants won't change. Used here to set a pin number:
const int ledPin =  LED_BUILTIN;// the number of the LED pin

createSafeString(szSerial, 16);
bool stringComplete = false;  // whether the string is complete
bool blinking = false;

// Variables will change:
int ledState = LOW;             // ledState used to set the LED

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time LED was updated

// constants won't change:
const long interval = 500;           // interval at which to blink (milliseconds)

void setup() {
  // set the digital pin as output:
  Serial.begin(9600);
  SafeString::setOutput(Serial);
  
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  // timestamp;ax;ay;az;gx;gy;gz;mx;my;mz
  
  if (blinking) {

    if (currentMillis - previousMillis >= interval) {
      // save the last time you blinked the LED
      previousMillis = currentMillis;
  
      // if the LED is off turn it on and vice-versa:
      if (ledState == LOW) {
        ledState = HIGH;
      } else {
        ledState = LOW;
      }
  
      // set the LED with the ledState of the variable:
      digitalWrite(ledPin, ledState);
    }
  }

  if (stringComplete) {
    Serial.println(szSerial);

    if (szSerial == "a") {
      blinking = !blinking;

      if (!blinking) {
        Serial.print("Not ");
      }
      Serial.println("blinking");
        
    }
    
    // clear the string:
    szSerial = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      break;
    }

    // add it to the inputString:
    szSerial += inChar;
  }
}
