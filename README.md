KickBoard return judging Module
===

<p align="center">
</p>

킥보드 return judging 시스템을 위한 code와 mp3 파일을 포함하고 있습니다.
저희가 구현한 것은 반납 시스템 전부가 아니라 
지정된 구역 안에 주차되었는지 판별하는 시스템입니다.
지정구역은 파란색으로 색칠되어 있다고 가정합니다.

## 시스템 설명
* 원래 kakao T 에서 제공하는 어플을 사용하면 킥보드를 반납 구역에 주차하고 앱에서 반납 버튼을 누릅니다
* 반납 구역에 주차하지 않는다면 계속 사용 요금이 올라가므로 Client는 반드시 반납을 지정 주차 구역에 해야 합니다
* 이 Module은 어플에서 제공하는 지정 주차구역(GPS라서 세부적인 주차구역은 판별 불가능) 뿐만 아니라 우리 학교에 있는 킥보드 지정주차 구역도 감지할 수 있습니다
* 색감지 Arduino 모듈을 사용하여 judging을 수행합니다



## Easy to find
* [Models](#models)
* [Setup](#install)
* [Set Usb port](#setting)
* [Explanation](#explain)
* [How to Use](#method)
* [Reference](#reference)
* 


<a name="models"></a>
## Models

파이썬 코드를 통해 UI를 구현하고 반납 버튼을 누른다면 RGB와 GPS 센서에서 값을 불러옵니다.
JUDGING 클래스에서 이를 처리하고 반납 여부를 알려줍니다.


<a name="install"></a>
## Setup
0. SET Virtualbox USB
  * Arduino 보드를 컴퓨터와 연결합니다 (using USB port)
  * Virtualbox 에 들어갑니다
  * Ubuntu 설정 -> USB --> Usb 필터 추가 --> Arduino 클릭
  * Ubuntu 실행 

1. Module과 python 버전
  * python = 3.10.9
  * pygame = 2.5.2
  * tkinter = 8.6
  * numpy = 1.23.5
  * serial= 3.5

## Ubuntu 20.04 기준 설치 방법
## !!Conda 가상환경 설치되어있다고 가정합니다!!

2. Create Virtual Environment 
 ```
  conda create -name <name> python=3.10.9
  ```

```
conda activate <name>
```

3. Install Module
  * install pygame, pyserial numpy tk.
  ```
  conda install pygame=2.5.2
```
```
conda install pyserial=3.5
```
```
conda install numpy=1.23.5
```

```
conda install tk=8.6
```
if there is any error, then just install tk. Just like this
```
conda install tk
```
if pygame is not installed, then please write this code

```
conda install -c conda-forge <package name>
```

4. Get git clone
   ```
   mkdir mk
   cd mk
   git clone https://github.com/keep1617/KickBoard.git
   username: keep1617 <or your username>
   password: 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
   ```


<a name="setting"></a>
## Set USB Port
 * Connect Arduino Module to Ubuntu through USB port
 * 파일을 실행하기 전에, usb port에 대한 권한을 할당해야 합니다
   ```
   sudo usermod -a -G dialout <username>
   <your password>
   sudo chmod a+rw /dev/ttyACM0
   ```

## Then, execute main.py
   ``` cd KickBoard
      python main.py
```

<a name="explain"></a>
## 코드 설명
1. 반납
* python에서 코드를 실행합니다
* 반납 버튼을 누르면 show_result 함수가 실행됩니다  
* Arduino 객체가 생성됩니다
* 5개의 센서 data list 값을 받습니다
* data list에서 중간값을 가져옵니다
* Judge 객체가 call 됩니다
* judging을 수행하고 UI self.bool에 결과를 저장합니다
* self.bool 이 true라면 반납 완료를 보여주고 반납되었음을 말해주는 play_success 함수가 실행됩니다

2. 반납 실패
    반납이 실패되면 다시 반납 버튼을 누르고 위 반납 과정을 반복합니다 


<a name="method"></a>
## 실행 방법
1. 기기를 노트북에 연결한다
2. Setup 부분을 참고하여 install 한다
3. GPS가 위성과  connect 할 때까지 야외에서 기다린다(gps불이 깜빡거리면 위성과 연결이 되었단 것이다)
4. 주차 구역에 module을 가지고 간다
5. main.py를 실행한다
6. 반납 버튼을 누른다
7. 확인한다
8. 실패한다면 다시 반납하기 누른다.


<a name="reference"></a>
## Reference
* tkinter 모듈 사용법으로 기본적 코드 구현
  [how to use](https://proprogramming.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B8%B0%EB%B3%B8%ED%8C%A8%ED%82%A4%EC%A7%80-Tkinter%EC%82%AC%EC%9A%A9%EB%B2%95)
  


   

   
     

   


