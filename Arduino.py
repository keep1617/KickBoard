#include <TinyGPS.h>

const int s0 = 8;  
const int s1 = 9;  
const int s2 = 12;  
const int s3 = 11;  
const int out = 10;   
int red = 0;  
int green = 0;  
int blue = 0;  

TinyGPS gps;

void color()  
{    
  digitalWrite(s2, LOW);  
  digitalWrite(s3, LOW);  
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s3, HIGH);  
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s2, HIGH);  
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
}


void setup()
{
  Serial.begin(115200);
  Serial1.begin(9600);
  
  pinMode(s0, OUTPUT);  
  pinMode(s1, OUTPUT);  
  pinMode(s2, OUTPUT);  
  pinMode(s3, OUTPUT);  
  pinMode(out, INPUT);  
  digitalWrite(s0, HIGH);  
  digitalWrite(s1, HIGH);  
}


void loop()
{
  bool gpsNewData = false;
  bool rgbNewData = false;
  unsigned long gpsChars, rgbChars;
  unsigned short gpsSentences, rgbSentences, gpsFailed, rgbFailed;

  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    while (Serial1.available())
    {
      char c = Serial1.read();
      if (gps.encode(c))
        gpsNewData = true;
    }

    color();
    rgbNewData = true;
  }


  if (true)
  {
    float flat, flon;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);
    Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    Serial.print(',');
    Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial.print(',');
  }
  
  Serial.print(red);
  Serial.print(',');
  Serial.print(green);
  Serial.print(',');
  Serial.print(blue);
  
  Serial.println();
  delay(300);   }
