#include <FileIO.h>
#include <Bridge.h>

Process myscript;
Process p;
Process chmod;

String path_to_file = //insert the path to the script file


// This function writes a Script in the path specified as input and make it executable 
void uploadScript() {

  File script = FileSystem.open(path_to_file, FILE_WRITE);

  script.print("#!/bin/python\n");
  script.print("\n");
  script.print("import sys\n");
  script.print("sys.path.insert(0, '/mnt/sda1/SEPA')\n");
  script.print("from SEPINO import SEPA\n");
  script.print("from JSAP import JSAP_file\n");
  script.print("SEPA(JSAP_file).Subscribe('select * from <http://demoSEPINO> where { ?s ?p ?o }')");
  script.close();  // close the file


  chmod.begin("chmod");                               // chmod: change mode
  chmod.addParameter("755");                       
  chmod.addParameter(path_to_file);    // path fino al file al quale è riferito il processo
  chmod.run();
}


// This function run the scripts written before 

void runScript() {

  myscript.begin("python" );
  myscript.addParameter("path_to_file);
  myscript.addParameter("-u");
  myscript.runAsynchronously();

}

void setup() {


  // First we delete last script to rewrite another one new
  p.begin("rm" + path_to_file);

  // Initialising  PIN 9 and  13 setting them as  OUTPUT
  pinMode(13,OUTPUT);
  pinMode(9,OUTPUT);

  // Initialising Bridge and FileSystem communication 
  Bridge.begin();
  Serial.begin(9600);
  while (!Serial); // wait for Serial port to connect.
  FileSystem.begin();

  // Uploading and running the script specified before 
  uploadScript();
  runScript();

}

void loop() {

  // While there are data produced from the script, we stock them in a string and print it on serial monitor 
  while (myscript.available() > 0) {
    String c = myscript.readString();
    Serial.print(c);
    // In this particular example, we check the temperature and humidity values contained in the notification messages: 
    // if they are higher than a treshold, arduino turns on alert LED, in particular a red LED on PIN 13 id it's too warm,
    // a green LED on PIN 9 if it's too wet.
    
    if (c.indexOf("caldo") > 0) {
      digitalWrite(13, HIGH);
      delay(5000);
      digitalWrite(13, LOW);
    }
    if (c.indexOf("umido") > 0) {
      digitalWrite(9, HIGH);
      delay(5000);
      digitalWrite(9, LOW);
    }
  }

// If there aren't incoming data from the script, we print dots on serial monitor 
Serial.println(".");

// we continue flushing buffer to make them empty and ready to receive data from the script 

Serial.flush();
delay(3000);
}