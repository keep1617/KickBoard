/*아두이노를 사용하여 GPS모듈과 색감지 센서를 활용하여 위치정보와 지면의 RGB값을 시리얼 통신을 통해 출력하는 프로그램*/

#include <TinyGPS.h>  /*TinyGPS 라이브러리 포함*/

const int s0 = 8;     /* 색감지 센서의 핀 설정*/
const int s1 = 9;  
const int s2 = 12;  
const int s3 = 11;  
const int out = 10;   

int red = 0;          /* 색감지 센서의 RGB값 저장을 위한 변수 선언*/
int green = 0;  
int blue = 0;  


TinyGPS gps;          /* TinyGPS 객체 생성*/


void color()          /* pulseIn 함수를 사용하여 색감지 센서 출력 핀에서 신호를 읽어와 RGB값을 측정*/
{    
  digitalWrite(s2, LOW);  
  digitalWrite(s3, LOW);  
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s3, HIGH);  
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  
  digitalWrite(s2, HIGH);  
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
}




void setup()          /* 시리얼 통신을 초기화하고, GPS 모듈과 색감지 센서의 핀을 설정*/
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
      if (gps.encode(c))        /* gps.encode(c)를 통해 GPS 모듈로부터 데이터를 읽어옴*/
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
  
  float scaledRed = map(red, 0, 255, 0, 500);       /* map 함수를 사용하여 0부터 255까지의 범위를 0부터 500까지의 범위로 확대*/ 
  float scaledGreen = map(green, 0, 255, 0, 500);
  float scaledBlue = map(blue, 0, 255, 0, 500);
  float sum = scaledRed + scaledGreen + scaledBlue;
  
  
  Serial.print(scaledRed/sum*100);                 /* 변환된 RGB 값을 통해 각 색상의 백분율 값을 계산하여 출력 */
  Serial.print(',');
  Serial.print(scaledGreen/sum*100);
  Serial.print(',');
  Serial.print(scaledBlue/sum*100);
  
  Serial.println();
    }
