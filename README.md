KickBoard return judging System
===

<p align="center">
</p>

킥보드 return judging 시스템을 위한 code와 mp3 파일을 포함하고 있습니다.
저희가 구현한 것은 반납 시스템 전부가 아니라 
지정된 구역 안에 주차되었는지 판별하는 시스템입니다.
지정구역은 파란색으로 색칠되어 있다고 가정합니다.




* [Models](#models)
* [Setup](#install)
* [Set Usb port](#setting)
* [Reference](#reference)

<a name="models"></a>
## Models

파이썬 코드를 통해 UI를 구현하고 반납 버튼을 누른다면 RGB와 GPS 센서에서 값을 불러옵니다.
JUDGING 클래스에서 이를 처리하고 반납 여부를 알려줍니다.


<a name="install"></a>
## Setup
0. SET Virtualbox USB
  * Arduino 보드를 컴퓨터와 연결합니다 
  * Virtualbox 에 들어갑니다
  * Ubuntu 설정 -> USB --> Usb 필터 추가 --> Arduino 클릭
  * Ubuntu 실행 

1. Module과 python 버전
  * python = 3.10.9
  * pygame = 2.5.2
  * tkinter = 8.6
  * numpy =1.23.5
  * serial=3.5

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



<a name="reference"></a>

* tkinter 모듈 사용법으로 기본적 코드 구현
  [how to use](https://proprogramming.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B8%B0%EB%B3%B8%ED%8C%A8%ED%82%A4%EC%A7%80-Tkinter%EC%82%AC%EC%9A%A9%EB%B2%95)
  


   

   
     

   


