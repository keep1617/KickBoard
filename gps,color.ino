#include <SoftwareSerial.h>
#include <TinyGPS.h>

const int s0 = 8;  
const int s1 = 9;  
const int s2 = 12;  
const int s3 = 11;  
const int out = 10;   
// LED pins connected to Arduino
int redLed = 2;  
int greenLed = 3;  
int blueLed = 4;
// Variables  
int red = 0;  
int green = 0;  
int blue = 0;  

TinyGPS gps;
SoftwareSerial ss(4, 3);

void color()  
{    
  digitalWrite(s2, LOW);  
  digitalWrite(s3, LOW);  
  //count OUT, pRed, RED  
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s3, HIGH);  
  //count OUT, pBLUE, BLUE  
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s2, HIGH);  
  //count OUT, pGreen, GREEN  
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
}

void setup()
{
  Serial.begin(115200);
  ss.begin(4800);
  
  pinMode(s0, OUTPUT);  
  pinMode(s1, OUTPUT);  
  pinMode(s2, OUTPUT);  
  pinMode(s3, OUTPUT);  
  pinMode(out, INPUT);  
  pinMode(redLed, OUTPUT);  
  pinMode(greenLed, OUTPUT);  
  pinMode(blueLed, OUTPUT);  
  digitalWrite(s0, HIGH);  
  digitalWrite(s1, HIGH);  
}

void loop()
{
  bool gpsNewData = false;
  bool rgbNewData = false;
  unsigned long gpsChars, rgbChars;
  unsigned short gpsSentences, rgbSentences, gpsFailed, rgbFailed;

  // For one second we parse GPS data and RGB data
  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    // Parse GPS data
    while (ss.available())
    {
      char c = ss.read();
      if (gps.encode(c))
        gpsNewData = true;
    }

    // Parse RGB data
    color();
    rgbNewData = true;
  }

  // Print GPS data
  if (true)
  {
    float flat, flon;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);
    // Serial.print("GPS: LAT=");
    Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    Serial.print(',');
    // Serial.print(" LON=");
    Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial.print(',');
    // Serial.print(" SAT=");
    // Serial.print(gps.satellites() == TinyGPS::GPS_INVALID_SATELLITES ? 0 : gps.satellites());
    // Serial.print(',');
    // // Serial.print(" PREC=");
    // Serial.print(gps.hdop() == TinyGPS::GPS_INVALID_HDOP ? 0 : gps.hdop());
    // Serial.print(',');
  }
  
  // Print RGB data
  // Serial.print(" RGB: R=");
  Serial.print(red);
  Serial.print(',');
  // Serial.print(" G=");
  Serial.print(green);
  Serial.print(',');
  // Serial.print(" B=");
  Serial.print(blue);
  
/*
  gps.stats(&gpsChars, &gpsSentences, &gpsFailed);
  Serial.print(" GPS CHARS=");
  Serial.print(gpsChars);
  Serial.print(" SENTENCES=");
  Serial.print(gpsSentences);
  Serial.print(" CSUM ERR=");
  Serial.print(gpsFailed);
*/
  Serial.println();  // End the line
/*
  if (gpsChars == 0)
    Serial.println("** No characters received from GPS: check wiring **");
*/
  delay(300);   
  digitalWrite(redLed, LOW);  
  digitalWrite(greenLed, LOW);  
  digitalWrite(blueLed, LOW);
