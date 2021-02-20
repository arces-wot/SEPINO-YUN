# SEPINO-YUN
SEPINO-Yun is a part of SEPINO project that aims to interface the Arduino family with the SEPA server, creating an environment that uses all the benefit from each of the two technologies. Thanks to this project it will be possible to use the SEPA server in IoT projects based on Arduino microcontrollers.

In this repository is presented how to interface the Arduino Yùn Rev. 2 with SEPA server:
1. There's the Arduino sketch that writes and runs a script on the Atheros 9331R using a Python module named SEPA
2. Thanks to Bridge Arduino receive data produced from the Python process and print them on the serial monitor.


In this repository is also presented a Python class named "SEPA" that using the configuration parameters contained in the JSAP file, implements all of the three SEPA server's fundamental operations that are Query, Update and Subscribe.

You just have to import the module and the JSAP file (like it's shown in the dashboard example file), then you can invoke one of the three methods to implement the operation that you want to obtain.

Moreover in the Arduino Sketch is possible to find out a piece of code referring to PIN 9 an PIN 13. In fact this sketch has been used to realize a DEMO. 
In this DEMO it has been realised a sensor network in witch there are two sensor nodes:
1. The first one is an Arduino Uno that, thanks to an ESP8266 and to a DHT11, measures Temperature and Humidity, then it uploads these values to a graph to witch is subscribed the second sensor node.
2. The second one is an Arduino Yun Rev 2 that receives notification with Temperature and Humidity values and, if they're higher than a treshold, it activates two LEDs (a red one for temperature and a green one per humidity).
