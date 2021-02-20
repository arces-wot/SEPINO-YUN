# SEPINO-YUN
SEPINO-Yun is a part of SEPINO project that aims to interface the Arduino family with the SEPA server, creating an environment that uses all the benefit from each of the two technologies. Thanks to this project it will be possible to use the SEPA server in IoT projects based on Arduino microcontrollers.

In this repository is presented how to interface the Arduino Yùn Rev. 2 with SEPA server:
1. There's the Arduino sketch that writes and runs a script on the Atheros 9331R using a Python module named SEPA
2. Thanks to Bridge Arduino receive data produced from the Python process and print them on the serial monitor.


In this repository is also presented a Python class named "SEPA" that using the configuration parameters contained in the JSAP file, implements all of the three SEPA server's fundamental operations that are Query, Update and Subscribe.

You just have to import the module and the JSAP file (like it's shown in the dashboard example file), then you can invoke one of the three methods to implement the operation that you want to obtain.
